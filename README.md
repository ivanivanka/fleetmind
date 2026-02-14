# FleetMind AI - Warehouse Robot Fleet Orchestration

AI-powered warehouse fleet orchestration platform. FleetMind coordinates autonomous robot teams in simulation - real-time task routing, battery-aware scheduling, collision avoidance, and operator dashboards.

Built for warehouse ops teams who need to manage 10-100+ robots without hiring robotics engineers.

## Features

- **2D Warehouse Simulation** - Configurable warehouse layouts with shelves, aisles, charging stations
- **Autonomous Fleet Control** - A* pathfinding, collision avoidance, battery management
- **Smart Task Routing** - Priority-based order assignment matching nearest available robots
- **Gemini AI Integration** - Intelligent task prioritization and anomaly detection
- **Real-time Dashboard** - Live fleet status, task queues, metrics, alerts via WebSocket
- **Operator Controls** - Manual task creation, emergency stop, alert management

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

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8000` | Server port |
| `FLEET_SIZE` | `12` | Number of robots |
| `TASK_RATE` | `3.0` | Seconds between new tasks |
| `GEMINI_API_KEY` | - | Google Gemini API key (optional, falls back to rule-based AI) |
| `GEMINI_MODEL` | `gemini-flash-latest` | Gemini model name (only used if `GEMINI_API_KEY` is set) |

## Docker

```bash
docker build -t fleetmind .
docker run -p 8000:8000 -e GEMINI_API_KEY=your-key fleetmind
```

## Tech Stack

- **Backend**: Python FastAPI + WebSocket
- **AI**: Google Gemini 2.0 Flash
- **Simulation**: Custom engine with A* pathfinding
- **Frontend**: HTML5 Canvas + vanilla JavaScript
- **Deployment**: Docker on Vultr VM

## Built for lablab.ai Hackathon

Track 1: Autonomous Robotics Control in Simulation

Team: Markster FleetMind

## License

MIT
