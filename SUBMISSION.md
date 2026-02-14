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
- **Markster FleetMind AI - Robot Fleet Orchestration** (49/50)

Short description (1–2 lines):
- Simulation-first warehouse robot fleet control plane: assigns tasks, routes robots with collision avoidance, manages charging/battery, and streams live metrics + alerts to a web ops dashboard. Deployed on Vultr with optional Gemini AI insights. (244/255)

Long description (suggested):
- Markster FleetMind AI is a simulation-first platform for orchestrating a warehouse robot fleet. It acts as the centralized backend for planning, coordination, and operations, and exposes a real-time web dashboard for operators.
-
- Problem: As fleets scale, ops teams fight congestion, charging bottlenecks, and brittle vendor-specific tooling. Small changes can break throughput and there is rarely a safe place to test policies.
-
- Solution: FleetMind runs an orchestration loop that (1) ingests or generates tasks, (2) assigns tasks to the nearest capable robot based on priority, (3) routes robots through aisles using A* pathfinding with collision avoidance, and (4) manages battery and charging behavior. The dashboard streams live robot state, tasks, KPIs (throughput, utilization, queue depth), and alerts via WebSocket. An optional Gemini integration produces concise operational insights and can re-prioritize the queued task list.
-
- Deployment: The backend and web app are deployed on a Vultr VM and are accessible in any browser. The current MVP is simulation-first (robots are virtual); the next step is ROS2/vendor connectors so the same control plane can run against real fleets.

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
