"""Gemini AI integration for intelligent task prioritization and anomaly detection."""

import asyncio
import json
import os
import logging

logger = logging.getLogger(__name__)

# Try to import google.generativeai, fall back to mock if not available
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logger.warning("google-generativeai not installed, using mock AI responses")


class FleetMindAI:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY", "")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
        self.model = None
        if GEMINI_AVAILABLE and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(self.model_name)
                logger.info(f"Gemini AI initialized successfully (model={self.model_name})")
            except Exception as e:
                logger.warning(f"Failed to initialize Gemini: {e}")

    async def prioritize_tasks(self, tasks: list[dict], robots: list[dict], metrics: dict) -> list[dict]:
        """Use Gemini to intelligently prioritize task queue based on warehouse state."""
        if not self.model:
            return self._fallback_prioritize(tasks)

        prompt = f"""You are an AI warehouse fleet orchestrator. Given the current warehouse state,
re-prioritize the task queue for optimal throughput.

Current metrics:
- Fleet utilization: {metrics.get('fleet_utilization', 0):.0%}
- Avg battery: {metrics.get('avg_battery', 0):.0f}%
- Tasks in queue: {metrics.get('tasks_in_queue', 0)}
- Throughput: {metrics.get('throughput_per_minute', 0):.1f} tasks/min

Pending tasks (id, priority, pickup, dropoff):
{json.dumps(tasks[:10], indent=2)}

Available robots (id, position, battery):
{json.dumps([{{'id': r['id'], 'x': r['x'], 'y': r['y'], 'battery': r['battery']}} for r in robots if r['state'] == 'idle'][:8], indent=2)}

Return a JSON array of task IDs in optimal execution order. Consider:
1. Critical/high priority tasks first
2. Minimize total robot travel distance
3. Cluster nearby pickups for efficiency
4. Avoid sending low-battery robots to far tasks

Return ONLY a JSON array of task IDs, nothing else."""

        try:
            response = await self._generate(prompt)
            task_ids = json.loads(response.strip())
            if isinstance(task_ids, list):
                return [{"task_id": tid, "ai_prioritized": True} for tid in task_ids]
        except Exception as e:
            logger.warning(f"Gemini prioritization failed: {e}")

        return self._fallback_prioritize(tasks)

    async def detect_anomalies(self, metrics_history: list[dict]) -> list[dict]:
        """Use Gemini to detect fleet anomalies and suggest corrections."""
        if not self.model or len(metrics_history) < 5:
            return []

        recent = metrics_history[-10:]
        prompt = f"""You are monitoring a warehouse robot fleet. Analyze these recent metrics snapshots
and identify any anomalies or concerning trends.

Recent metrics (newest first):
{json.dumps(recent, indent=2)}

For each anomaly found, return a JSON array of objects with:
- "type": one of "throughput_drop", "battery_issue", "utilization_low", "queue_buildup"
- "severity": "warning" or "critical"
- "message": brief human-readable description
- "suggestion": recommended action

Return ONLY a JSON array. If no anomalies, return []."""

        try:
            response = await self._generate(prompt)
            anomalies = json.loads(response.strip())
            if isinstance(anomalies, list):
                return anomalies
        except Exception as e:
            logger.warning(f"Gemini anomaly detection failed: {e}")

        return []

    def rules_insight(self, metrics: dict) -> str:
        return self._fallback_insight(metrics)

    async def generate_insight(self, metrics: dict) -> dict[str, object]:
        """Generate a brief operational insight for the dashboard."""
        if not self.model:
            return {"insight": self._fallback_insight(metrics), "source": "rules"}

        prompt = f"""You are a warehouse operations AI advisor. Based on these current fleet metrics,
provide ONE brief operational insight (1-2 sentences max).

Metrics:
- Tasks completed: {metrics.get('tasks_completed', 0)}
- Queue size: {metrics.get('tasks_in_queue', 0)}
- Throughput: {metrics.get('throughput_per_minute', 0):.1f}/min
- Fleet utilization: {metrics.get('fleet_utilization', 0):.0%}
- Avg battery: {metrics.get('avg_battery', 0):.0f}%
- Robots charging: {metrics.get('robots_charging', 0)}
- Robots idle: {metrics.get('robots_idle', 0)}
- Active alerts: {metrics.get('alerts_active', 0)}

Be specific and actionable. No fluff."""

        try:
            response = await self._generate(prompt)
            text = (response or "").strip()
            if not text:
                return {"insight": self._fallback_insight(metrics), "source": "rules", "error": "empty_response"}
            return {"insight": text[:200], "source": "gemini"}
        except Exception as e:
            msg = str(e)
            err = "quota_exceeded" if ("429" in msg or "quota" in msg.lower()) else "gemini_error"
            brief = msg.splitlines()[0][:200]
            logger.warning(f"Gemini insight generation failed ({err}): {brief}")
            return {"insight": self._fallback_insight(metrics), "source": "rules", "error": err}

    async def _generate(self, prompt: str) -> str:
        """Call Gemini API."""
        # google-generativeai is synchronous; run it in a thread to avoid blocking the event loop.
        response = await asyncio.to_thread(self.model.generate_content, prompt)
        return response.text or ""

    def _fallback_prioritize(self, tasks: list[dict]) -> list[dict]:
        """Simple priority-based fallback when Gemini is unavailable."""
        priority_order = {"critical": 0, "high": 1, "normal": 2, "low": 3}
        sorted_tasks = sorted(tasks, key=lambda t: priority_order.get(t.get("priority", "normal"), 2))
        return [{"task_id": t["id"], "ai_prioritized": False} for t in sorted_tasks]

    def _fallback_insight(self, metrics: dict) -> str:
        """Generate basic insight without AI."""
        util = metrics.get("fleet_utilization", 0)
        queue = metrics.get("tasks_in_queue", 0)
        battery = metrics.get("avg_battery", 0)

        if queue > 10:
            return f"Queue building up ({queue} pending). Consider adding more robots to the fleet."
        elif util < 0.3:
            return f"Low fleet utilization ({util:.0%}). Fleet is ready for higher order volume."
        elif battery < 40:
            return f"Average battery at {battery:.0f}%. Multiple robots may need charging soon."
        else:
            throughput = metrics.get("throughput_per_minute", 0)
            return f"Fleet operating normally. Throughput: {throughput:.1f} tasks/min, utilization: {util:.0%}."
