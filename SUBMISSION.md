# Markster FleetMind AI (AI Meets Robotics) Submission Notes

## What It Is

Markster FleetMind AI is a simulation-first fleet orchestration platform for warehouse robots:

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

## Hackathon Submission Checklist (from event page)

Required fields / assets:
- Basic info:
  - Project Title
  - Short Description
  - Long Description
  - Technology & Category Tags
  - Final Submission Video Link (X/Twitter) **required for prize eligibility**
- Media:
  - Cover Image
  - Video Presentation
  - Slide Presentation
- Hosting / code:
  - Public GitHub Repository
  - Demo Application Platform (Vultr VM)
  - Application URL (public)

Status:
- Public GitHub repo: ✅ `https://github.com/ivanivanka/fleetmind`
- Vultr VM backend deployed: ✅ `http://149.28.198.127/` (health: `/healthz`)
- Public demo URL accessible in browser: ✅
- Recorded demo video: ⏳ (create + upload)
- Final submission video posted on X + tags + link pasted into form: ⏳
- Cover image + slide deck: ⏳

## Copy/Paste Text

Project title:
- **Markster FleetMind AI — Warehouse Robot Fleet Orchestration (Simulation-First)**

Short description (1–2 lines):
- Markster FleetMind AI is a simulation-first control plane for warehouse robot fleets: real-time task assignment, collision-aware routing, battery/charging management, and an ops dashboard with AI insights.

Long description (suggested):
- Markster FleetMind AI helps warehouse operations teams run 10–100+ robots without needing a robotics engineering team. It provides a centralized backend for planning, coordination, and execution in a simulated warehouse environment (simulation-first is encouraged by the event). The system assigns tasks to robots based on priority and proximity, routes robots through aisles using A* pathfinding with collision avoidance, manages battery/charging behavior, and surfaces live metrics (throughput, utilization, queue depth) and alerts in a web dashboard via WebSocket. An optional Gemini integration generates concise operational insights and can re-prioritize queued tasks.

Suggested tags:
- Robotics
- Warehouse
- Logistics
- Simulation
- Digital Twin
- Fleet Orchestration
- FastAPI
- WebSocket
- Vultr
- Gemini
