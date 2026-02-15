"""Markster FleetMind AI - Warehouse Robot Fleet Orchestration Platform."""

import asyncio
import json
import logging
import os
import time

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from simulation import WarehouseSimulation
from gemini_client import FleetMindAI
from models import WarehouseConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Markster FleetMind AI", version="1.0.0")

# Global simulation instance
sim: WarehouseSimulation = None
ai: FleetMindAI = None
sim_task: asyncio.Task = None
watchdog_task: asyncio.Task = None

_ai_insight_cache: dict[str, object] = {
    "ts": 0.0,
    "insight": "Initializing fleet intelligence...",
    "source": "rules",
    "error": None,
}
_ai_insight_lock = asyncio.Lock()


@app.on_event("startup")
async def startup():
    global sim, ai, sim_task, watchdog_task
    config = WarehouseConfig(
        num_robots=int(os.environ.get("FLEET_SIZE", "12")),
        task_generation_rate=float(os.environ.get("TASK_RATE", "3.0")),
        max_queued_tasks=int(os.environ.get("MAX_QUEUED_TASKS", "25")),
        max_total_tasks=int(os.environ.get("MAX_TOTAL_TASKS", "2000")),
    )
    sim = WarehouseSimulation(config)
    ai = FleetMindAI()
    sim_task = asyncio.create_task(sim.run(tick_interval=0.3))
    watchdog_task = asyncio.create_task(_watchdog_loop())
    logger.info(f"FleetMind started with {config.num_robots} robots")


@app.on_event("shutdown")
async def shutdown():
    global watchdog_task
    if sim:
        sim.stop()
    if sim_task:
        sim_task.cancel()
    if watchdog_task:
        watchdog_task.cancel()


async def _watchdog_loop():
    """Keep the public demo healthy over long runtimes.

    If the sim stops making observable progress (no movement / no completions)
    for an extended period, auto-reset to restore activity.
    """
    last_completed = 0
    last_distance = 0.0
    no_progress_s = 0
    interval_s = 20
    reset_after_s = 180

    while True:
        await asyncio.sleep(interval_s)
        if not sim:
            continue
        if getattr(sim, "paused", False):
            no_progress_s = 0
            continue

        try:
            metrics = sim.get_metrics()
            completed = int(metrics.tasks_completed)
            distance = float(metrics.total_distance)

            progressed = (completed > last_completed) or (distance > last_distance)
            last_completed = completed
            last_distance = distance

            if progressed:
                no_progress_s = 0
                continue

            no_progress_s += interval_s
            if no_progress_s >= reset_after_s:
                logger.warning("Watchdog: no progress detected; auto-resetting demo")
                await sim.reset()
                no_progress_s = 0
        except Exception as e:
            logger.warning(f"Watchdog error: {e}")


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/healthz")
async def healthz():
    return {"ok": True, "sim": bool(sim)}


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    queue = sim.subscribe()
    try:
        # Send initial state immediately
        state = sim.get_state()
        await ws.send_json(state)

        while True:
            try:
                data = await asyncio.wait_for(queue.get(), timeout=5.0)
                await ws.send_json(data)
            except asyncio.TimeoutError:
                # Send heartbeat
                await ws.send_json({"type": "heartbeat"})
    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.warning(f"WebSocket error: {e}")
    finally:
        sim.unsubscribe(queue)


@app.get("/api/metrics")
async def get_metrics():
    return JSONResponse(content=sim.get_metrics().model_dump())


@app.get("/api/metrics/history")
async def get_metrics_history():
    return JSONResponse(content=[m.model_dump() for m in sim.metrics_history[-60:]])


@app.get("/api/robots")
async def get_robots():
    state = sim.get_state()
    return JSONResponse(content=state["robots"])


@app.get("/api/tasks")
async def get_tasks():
    state = sim.get_state()
    return JSONResponse(content=state["tasks"])


@app.get("/api/alerts")
async def get_alerts():
    return JSONResponse(content=[
        {
            "id": a.id,
            "type": a.type,
            "message": a.message,
            "robot_id": a.robot_id,
            "timestamp": a.timestamp,
        }
        for a in sim.alerts[-20:]
        if not a.acknowledged
    ])


@app.post("/api/alerts/{alert_id}/acknowledge")
async def acknowledge_alert(alert_id: str):
    if sim.acknowledge_alert(alert_id):
        return {"status": "acknowledged"}
    return JSONResponse(status_code=404, content={"error": "Alert not found"})


@app.post("/api/robots/{robot_id}/stop")
async def stop_robot(robot_id: str):
    if sim.emergency_stop_robot(robot_id):
        return {"status": "stopped", "robot_id": robot_id}
    return JSONResponse(status_code=404, content={"error": "Robot not found"})

@app.post("/api/sim/pause")
async def pause_sim():
    sim.pause()
    # E-stop should be obvious: stop robots and re-queue in-flight tasks.
    for r in list(sim.robots.values()):
        sim.emergency_stop_robot(r.id)
    return {"paused": True}


@app.post("/api/sim/resume")
async def resume_sim():
    sim.resume()
    return {"paused": False}


@app.post("/api/sim/reset")
async def reset_sim():
    await sim.reset()
    return {"status": "reset"}


@app.post("/api/tasks/create")
async def create_task(pickup_x: int = 2, pickup_y: int = 2, dropoff_x: int = 37, dropoff_y: int = 2, priority: str = "normal"):
    task = sim.add_manual_task(pickup_x, pickup_y, dropoff_x, dropoff_y, priority)
    if task:
        return {"status": "created", "task_id": task.id}
    return JSONResponse(status_code=400, content={"error": "Failed to create task"})


@app.get("/api/ai/insight")
async def get_ai_insight(mode: str = "rules"):
    metrics = sim.get_metrics().model_dump()

    # Default mode is a rules-based insight (no Gemini call). Gemini is opt-in.
    if mode != "gemini":
        return {"insight": ai.rules_insight(metrics), "source": "rules", "cached": True}

    # Cache Gemini calls to avoid blowing through free-tier quotas when multiple clients are connected.
    ttl_s = 300
    now = time.time()
    if now - float(_ai_insight_cache["ts"]) < ttl_s:
        return {
            "insight": _ai_insight_cache["insight"],
            "source": _ai_insight_cache["source"],
            "error": _ai_insight_cache["error"],
            "cached": True,
        }

    async with _ai_insight_lock:
        now = time.time()
        if now - float(_ai_insight_cache["ts"]) < ttl_s:
            return {
                "insight": _ai_insight_cache["insight"],
                "source": _ai_insight_cache["source"],
                "error": _ai_insight_cache["error"],
                "cached": True,
            }

        result = await ai.generate_insight(metrics)
        _ai_insight_cache["ts"] = now
        _ai_insight_cache["insight"] = result.get("insight")
        _ai_insight_cache["source"] = result.get("source")
        _ai_insight_cache["error"] = result.get("error")
        return {**result, "cached": False}


@app.get("/api/ai/prioritize")
async def ai_prioritize():
    state = sim.get_state()
    queued_tasks = [t for t in state["tasks"] if t["status"] == "queued"]
    result = await ai.prioritize_tasks(queued_tasks, state["robots"], state["metrics"])
    return {"prioritized_tasks": result}


@app.get("/api/config")
async def get_config():
    return JSONResponse(content=sim.config.model_dump())


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
