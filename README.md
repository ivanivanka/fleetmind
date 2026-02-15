# Markster FleetMind AI - Warehouse Robot Fleet Orchestration

AI-powered warehouse fleet orchestration platform. Markster FleetMind AI coordinates autonomous robot teams in simulation - real-time task routing, battery-aware scheduling, collision avoidance, and operator dashboards.

Built for warehouse ops teams who need to manage 10-100+ robots without hiring robotics engineers.

## Features

- **2D Warehouse Simulation** - Configurable warehouse layouts with shelves, aisles, charging stations
- **Autonomous Fleet Control** - A* pathfinding, collision avoidance, battery management
- **Smart Task Routing** - Priority-based order assignment matching nearest available robots
- **Gemini AI Integration (Optional)** - On-demand ops insights with a safe rules-based fallback (cached)
- **Real-time Dashboard** - Live fleet status, task queues, metrics, alerts via WebSocket
- **Operator Controls** - Manual task creation, E-stop (pause/resume), and **Reset Demo** (fresh seed data)

## Architecture

```
Browser (Dashboard + Canvas Simulation)
    |
    WebSocket + REST API
    |
Vultr VM (FastAPI)
    |
    +-- Simulation Engine (A* pathfinding, robot state machine)
    +-- Task Router (priority queue, nearest-robot assignment)
    +-- Gemini AI (task prioritization, anomaly detection)
    +-- Metrics Engine (throughput, utilization, battery tracking)
```

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Open http://localhost:8000

## Docker (Recommended)

```bash
# Optional: export GEMINI_API_KEY=...
docker compose up -d --build
```

Open http://localhost:8000

## Deploy To Vultr (VM + Docker)

### Option A: One-command provision + deploy

```bash
# Requires: VULTR_API_KEY (Vultr v2 API token). GEMINI_API_KEY is optional.
./scripts/vultr_provision_and_deploy.sh
```

### Option B: Manual deploy (existing VM)

```bash
apt-get update -y && apt-get install -y curl git
curl -fsSL https://get.docker.com | sh

git clone https://github.com/ivanivanka/fleetmind.git /opt/fleetmind
cd /opt/fleetmind

cat > .env <<'EOF'
HOST_PORT=80
GEMINI_MODEL=gemini-flash-latest
GEMINI_API_KEY=your-key
EOF

docker compose up -d --build
```

Health check: `GET /healthz`

## Demo Controls

- `+ Add Task` creates a manual order and pushes it into the queue.
- `E-Stop All` toggles pause/resume (and re-queues in-flight tasks when pausing).
- `Reset Demo` restores a clean seed state (useful if the demo has been running a long time).

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8000` | Server port |
| `FLEET_SIZE` | `12` | Number of robots |
| `TASK_RATE` | `3.0` | Seconds between new tasks |
| `MAX_QUEUED_TASKS` | `25` | Soft cap on queued tasks (keeps the demo stable/legible) |
| `MAX_TOTAL_TASKS` | `2000` | Max task history retained in memory |
| `GEMINI_API_KEY` | - | Google Gemini API key (optional, falls back to rule-based AI) |
| `GEMINI_MODEL` | `gemini-flash-latest` | Gemini model name (only used if `GEMINI_API_KEY` is set) |

## Docker

```bash
docker build -t fleetmind .
docker run -p 8000:8000 -e GEMINI_API_KEY=your-key fleetmind
```

## Tech Stack

- **Backend**: Python FastAPI + WebSocket
- **AI**: Google Gemini (Flash model) + rules fallback
- **Simulation**: Custom engine with A* pathfinding
- **Frontend**: HTML5 Canvas + vanilla JavaScript
- **Deployment**: Docker on Vultr VM

## Built for lablab.ai Hackathon

Track 1: Autonomous Robotics Control in Simulation

Team: Markster FleetMind (Ivan @ Markster)

## License

MIT
