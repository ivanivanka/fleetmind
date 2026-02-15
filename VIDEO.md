# Markster FleetMind AI — Submission Video (Script + Checklist)

Goal: produce a 2–2.5 minute video that clearly shows (1) what it is, (2) why it matters, (3) that it works live, and (4) where to click.

## Absolute Rules

- Do **not** show API keys, `.env`, terminal history, or dashboards with secrets.
- Keep it short and fast: minimal talking, maximum “it works” proof.
- Prefer one clean take + light trimming over heavy editing.

## Recording Setup (macOS)

Option A (fast): QuickTime Player
1. Open QuickTime Player → File → New Screen Recording.
2. Mic: select a microphone (or record silent + voiceover later).
3. Record the browser window only.

Option B (flex): OBS Studio (if you already have it)
- Capture browser window + mic; optionally add a small “Markster FleetMind AI” title overlay.

Recommended: 720p or 1080p, 30fps.

## Video Outline (2:10 target)

### 0:00–0:07 — Title card (or first line over the dashboard)
Say:
- “This is Markster FleetMind AI: a control plane for warehouse robot fleets.”

Show:
- Dashboard loaded at: `http://149.28.198.127/`

### 0:07–0:25 — Problem (1–2 sentences)
Say:
- “As robot fleets scale, ops teams deal with routing conflicts, charging bottlenecks, and brittle vendor-specific tooling.”
- “They need one place to dispatch work, monitor KPIs, and stop issues fast.”

### 0:25–1:35 — Live demo (the proof)
Do (on screen):
1. Point at the canvas: shelves, pickup/dropoff, charging stations, robots moving.
2. Point at KPIs: throughput, utilization, queue depth, battery.
3. Click `+ Add Task` 2–3 times.
   - Call out the on-screen confirmation: “Task created: …”
   - Show the new `MAN-xxxx` task in “Recent Tasks”.
   - If anything looks “stuck”, click `Reset Demo` (fresh fleet + seed tasks).
4. Click `E-Stop All`.
   - Call out: “Simulation paused” and robots stop.
5. Click `Resume`.
   - Call out: “Robots resume and tasks re-assign.”
6. Click `AI Insight`.
   - Call out: “Gemini generates an ops recommendation from live metrics.”

### 1:35–1:55 — How it works (1 slide worth of words)
Say:
- “The web dashboard streams state over WebSocket to a FastAPI backend running on a Vultr VM.”
- “The backend runs task assignment, A* pathfinding with collision avoidance, plus battery and charging behavior.”

Optional 3-second proof:
- Open `http://149.28.198.127/healthz` in a new tab and show `{ok:true}`.

### 1:55–2:10 — Close + links
Say:
- “Live demo and source are public. Simulation-first today; next step is ROS2/vendor connectors to run the same control plane on real fleets.”

Show (end card or just speak it):
- Demo: `http://149.28.198.127/`
- Repo: `https://github.com/ivanivanka/fleetmind`
- Contact: `https://www.linkedin.com/in/ivanivanka/` | WhatsApp `+1 212 718 1149`

## Posting on X (Prize Eligibility)

1. Post the final demo video on X.
2. In the same post, tag: `@lablabai` and `@Surgexyz_`.
3. Include the demo URL + GitHub URL in the post text.
4. Copy the link to that X post and paste it into the submission form’s “Final Submission Video Link”.

Suggested X post text:
- `Markster FleetMind AI: simulation-first control plane for warehouse robot fleets (task dispatch, routing, charging, live ops dashboard + Gemini insights). Demo: http://149.28.198.127/ Repo: https://github.com/ivanivanka/fleetmind @lablabai @Surgexyz_`
