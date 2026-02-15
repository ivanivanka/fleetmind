# Markster FleetMind AI Demo Runbook

## Live Demo

- Open the dashboard in your browser.
- Confirm the status shows **Connected** and robots are moving.
- The top bar includes attribution ("Demo by Ivan @ Markster") plus WhatsApp contact.

## What To Show (2-3 minutes)

1. **Live digital twin**
   - Point out shelves, pickup zones (blue), dropoff zones (purple), charging stations (yellow).
   - Click robots to highlight their planned paths/targets.

2. **Autonomous orchestration**
   - Show tasks being generated and assigned automatically.
   - Show battery behavior: robots route to chargers when low.

3. **Operator controls**
   - Click **+ Add Task** a few times to create backlog.
   - If the sim ever looks stuck (e.g., lots of error robots), click **Reset Demo** to restore seed data and a fresh fleet.
   - Click **E-Stop All** to pause the simulation and stop robots (tasks re-queue).
   - Click **Resume** to continue.

4. **Gemini AI insight**
   - Click **AI Insight** (and/or wait for auto-refresh).
   - Explain that Gemini produces an operational insight from live fleet metrics.

## Useful Endpoints

- `GET /healthz`
- `GET /api/ai/insight` (rules mode by default)
- `GET /api/ai/insight?mode=gemini` (attempt Gemini; cached)
- `GET /api/metrics`
- `GET /api/robots`
- `GET /api/tasks`
- `POST /api/sim/reset`
