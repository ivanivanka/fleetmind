# FleetMind (AI Meets Robotics) Submission Notes

## What It Is

FleetMind is a simulation-first fleet orchestration platform for warehouse robots:

- Real-time robot routing (A* pathfinding) with collision avoidance
- Battery-aware scheduling with charging behavior
- Priority-based task assignment and live ops metrics
- Operator dashboard (WebSocket live view)
- Gemini-powered operational insight

## Links

- Repo: `https://github.com/ivanivanka/fleetmind`
- Demo URL (Vultr VM): `http://149.28.198.127/`
- Health check: `http://149.28.198.127/healthz`

## Tech

- Backend: FastAPI + WebSocket
- Simulation: custom Python engine
- AI: Google Gemini (via `google-generativeai`)
- Deployment: Docker Compose on Vultr VM
