# FleetMind Demo Runbook

## Live Demo

- Open the dashboard in your browser.
- Confirm the status shows **Connected** and robots are moving.

## What To Show (2-3 minutes)

1. **Live digital twin**
   - Point out shelves, pickup zones (blue), dropoff zones (purple), charging stations (yellow).
   - Click robots to highlight their planned paths/targets.

2. **Autonomous orchestration**
   - Show tasks being generated and assigned automatically.
   - Show battery behavior: robots route to chargers when low.

3. **Operator controls**
   - Click **+ Add Task** a few times to create backlog.
   - Click **E-Stop All** to stop active robots (then watch tasks re-queue).

4. **Gemini AI insight**
   - Click **AI Insight** (and/or wait for auto-refresh).
   - Explain that Gemini produces an operational insight from live fleet metrics.

## Useful Endpoints

- `GET /healthz`
- `GET /api/ai/insight`
- `GET /api/metrics`
- `GET /api/robots`
- `GET /api/tasks`
