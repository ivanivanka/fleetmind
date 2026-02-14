# Markster FleetMind AI Pitch Deck Brief (Sequoia-Style)

This is a copy/paste-ready brief for building a standard Sequoia-style pitch deck.
It’s written to be honest about the current MVP (simulation-first) while still
telling a credible product story.

## Slide 0: Cover (Title + Links)

**Title:** Markster FleetMind AI

**Subtitle:** Control plane for warehouse robot fleets (simulation-first)

**Links (put in small text):**
- Live demo: `http://149.28.198.127/`
- GitHub: `https://github.com/ivanivanka/fleetmind`

**Contact (put in footer):**
- Ivan Ivanka (Founder, Markster)
- LinkedIn: `https://www.linkedin.com/in/ivanivanka/`
- WhatsApp: `+1 212 718 1149`

---

## Slide 1: Company Purpose

**Title (one line):** Markster FleetMind AI is the control plane for warehouse robot fleets.

**What to show:**
- Product screenshot (dashboard + simulation canvas)
- 1–2 “outcomes” bullets (throughput, utilization, fewer alerts)

**One-liner:**
- “We help warehouse ops teams run 10–100+ robots like a single system, starting in simulation and extending to real fleets.”

---

## Slide 2: Problem

**Core problem:**
- Robot fleets are growing, but fleet operations are still brittle: routing conflicts, charging bottlenecks, task queue chaos, and constant human babysitting.
- Most solutions are siloed (robot-vendor tools) or too high-level (WMS/WES) to do real-time fleet orchestration.

**Proof points to cite:**
- E-commerce increases operational pressure on warehouses (e.g., share of retail).
- Warehousing is a big labor category with chronic churn; automation is the only scalable lever.
- Logistics robots shipments are meaningful and rising (fleet complexity is inevitable).

**Talk track (10–15s):**
- “Warehouses are becoming robot-dense environments, but the software to coordinate them is still fragmented. Ops teams need a real-time, vendor-neutral orchestration layer.”

---

## Slide 3: Solution

**What Markster FleetMind AI is:**
- A centralized orchestration backend + ops dashboard that:
  - assigns tasks
  - routes robots safely
  - manages battery/charging behavior
  - monitors throughput/utilization/alerts
  - provides an AI “ops copilot” for insights and prioritization

**What’s real today (MVP):**
- Live web app with:
  - multi-robot 2D simulation (A* routing + collision avoidance)
  - battery-aware scheduling + charging
  - priority-based task router
  - WebSocket real-time ops dashboard
  - Gemini AI insight endpoint + AI task reprioritization endpoint (optional)

**What becomes real next (post-hackathon):**
- Robot connectors: ROS2 / vendor APIs, map import, real telemetry
- Policy engine: zone rules, speed limits, safety constraints, SLA targets
- Optimization: batching, charging strategies, congestion-aware routing

---

## Optional Slide: How It Works (Architecture + Deployment)

**One sentence:** Web ops dashboard + centralized backend orchestrator deployed on Vultr.

**Block diagram (simple):**
- Browser UI (canvas + ops panels)
- WebSocket stream (live state) + REST endpoints (actions)
- Vultr VM (FastAPI):
  - simulation engine (robot state machine + A* routing + collision checks)
  - scheduler/dispatcher (priority + nearest-robot assignment)
  - battery/charging management
  - metrics + alerts
  - optional Gemini “ops copilot”

**Deployment notes (1–2 bullets):**
- Docker Compose on Vultr VM, public URL in any browser
- Simulation-first by design; same backend pattern extends to real robots via connectors

---

## Slide 4: Why Now

**Tailwinds:**
- Robotics adoption in logistics is accelerating and moving toward “fleets”, not single-purpose automation.
- RaaS is normalizing “subscribe to robots”, which increases fleet heterogeneity and operational complexity.
- Orchestration layers are emerging as a category because integration time and reliability are now board-level concerns.

**Evidence ideas:**
- Logistics robot shipment growth + RaaS growth.
- 3PL and enterprise logistics providers publicly talking about orchestration and deployment speed.

---

## Slide 5: Market Potential

**ICP (wedge):**
- Mid-market 3PLs and e-commerce warehouses running 10–200 AMRs (the “no robotics engineers on staff” segment).

**Expansion:**
- Enterprise DC networks (multi-site)
- System integrators and automation OEM partners

**TAM framing (bottoms-up, credible):**
- Price per robot per month (software control plane) + implementation.
- Use public data for annual logistics robot shipments as a proxy for “new fleet seats per year”.
- Add installed-base expansion over time.

**What to show:**
- 3 circles (Beachhead / Expand / Platform) with customer archetypes.

---

## Slide 6: Competition / Alternatives

**Alternatives buyers use today:**
- Robot-vendor fleet managers (work well but lock-in, limited cross-vendor coordination)
- WMS/WES modules (planning, not real-time orchestration)
- Simulation tools (great offline, not connected to live ops)

**Positioning wedge:**
- “Vendor-neutral orchestration + simulation-first validation + live ops UI.”

**Simple 2x2:**
- x-axis: “vendor-neutral” vs “vendor-specific”
- y-axis: “real-time ops control” vs “offline planning”

---

## Slide 7: Business Model

**Starting point:**
- SaaS priced per robot per month (plus onboarding/integration fee)
- Optional “AI ops copilot” tier

**Value levers (ROI):**
- Higher throughput (more tasks/hour)
- Higher utilization (less idle time)
- Fewer failures/alerts (less downtime)
- Faster deployments (lower integration cost)

---

## Slide 8: Go-To-Market

**Wedge motion (fastest to revenue):**
- Sell “simulation-first pilot”:
  - connect basic warehouse layout + order/task model
  - run scenarios
  - produce measurable improvement plan
  - then integrate with 1 real robot vendor

**Channels:**
- 3PL operations leaders
- system integrators (referrals + co-sell)
- robotics vendors that want an “ops layer” to reduce churn

---

## Slide 9: Team

**Angle:**
- “We build practical AI systems for operations, and we’re starting where customers can validate quickly: simulation + ops tooling.”

**Include:**
- Ivan Ivanka (Founder, Markster) — AI systems for operations + go-to-market execution
- Contact: LinkedIn `https://www.linkedin.com/in/ivanivanka/` | WhatsApp `+1 212 718 1149`

---

## Slide 10: Financials + Vision

**Financials (early-stage):**
- 12-month plan: pilot -> paid -> expand robots/sites
- Unit economics model (per-robot SaaS + integration margin)

**Vision (closing line):**
- “Markster FleetMind AI becomes the operating system for autonomous warehouse operations: planning, coordination, and continuous optimization across heterogeneous robot fleets.”

---

## Optional Slide: Demo + Submission Links (Drop-In)

Keep this as your final slide if you want judges to have everything in one place.

- Live demo: `http://149.28.198.127/`
- Health: `http://149.28.198.127/healthz`
- GitHub repo: `https://github.com/ivanivanka/fleetmind`
- Ops insight (rules): `GET /api/ai/insight`
- Ops insight (Gemini, cached): `GET /api/ai/insight?mode=gemini`

---

## Optional Slide: Background (Where We Fit In the Warehouse Stack)

Use this slide if the audience isn’t robotics-native (most investors aren’t).

**The stack (plain English):**
- **WMS** (Warehouse Management System): inventory + orders + planning (minutes/hours timescale)
- **WES/WCS** (Execution/Control): releases work + coordinates fixed automation (seconds/minutes)
- **RMS / Fleet managers**: robot-vendor-specific tools (seconds)
- **Markster FleetMind AI**: vendor-neutral orchestration + ops visibility across fleets (seconds) with simulation-first validation

**Why it matters:**
- The “planning layer” knows what should happen.
- The “fleet layer” decides what does happen in real time (routing, charging, congestion, failures).
- That real-time layer is increasingly the bottleneck as fleets scale.

**Visual:**
- Simple layered diagram with “Markster FleetMind AI” bridging WMS/WES <-> multi-vendor fleets.

---

## Optional Slide: Customer + Day-In-The-Life

**Persona:**
- Director of Operations / Warehouse GM / Automation Lead at a 3PL or e-commerce DC

**What they care about:**
- On-time SLA, throughput, and downtime
- “Why is the queue building?” and “Which aisle is congested?”
- Robot downtime + charging bottlenecks

**Current reality (pain):**
- Alerts are noisy and reactive (you find out after throughput drops)
- Vendor dashboards don’t explain cross-fleet bottlenecks
- Every change feels risky without a sandbox

**How we win (wedge):**
- Start with simulation-first modeling of a facility and workload
- Prove improvement in metrics, then integrate with 1 live fleet

---

## Optional Slide: Product Today vs Roadmap

**Today (built MVP):**
- Simulation-first “digital twin-ish” environment
- Real-time orchestration loop: tasks -> assign -> route -> charge -> metrics/alerts
- Live ops dashboard (WebSocket)
- AI ops insight (optional) + AI reprioritization endpoint (optional)

**Next 30–90 days (credible next steps):**
- Robot connectors: ROS2 + 1–2 common AMR vendor APIs
- Real telemetry ingestion: positions, battery, task states
- Policy engine: zones, speed limits, safety constraints, SLAs
- Optimization: batching, congestion-aware routing, charging strategy tuning

**Next 6–12 months (platform):**
- Multi-site fleet ops, user management, audit logs
- Integrations: WMS/WES events in, KPI exports out
- Learnable policies: data-driven routing/charging heuristics

---

## Optional Slide: Moat / Defensibility

Keep this grounded and technical.

**Defensibility sources:**
- **Connectors**: hard-earned integrations across robot vendors + warehouse stacks
- **Reliability playbooks**: failure modes, recovery strategies, safety guardrails
- **Data loop**: telemetry + outcomes -> better policies (routing, batching, charging)
- **Workflow lock-in**: ops teams live inside the dashboard; it becomes the system of record

**Not the moat:**
- “We have an LLM” (everyone does)

---

## Optional Slide: Pilot Plan + Success Metrics

**Pilot (2–4 weeks):**
- Import layout + define task model
- Replay workload in simulation
- Deliver KPI targets + integration plan

**Production pilot (4–8 weeks):**
- Connect to 1 robot fleet
- Shadow mode -> partial control -> full control for a zone

**Success metrics (choose 3):**
- Throughput (tasks/hour) up
- Robot utilization up
- Congestion events down
- Avg completion time down
- Charging bottlenecks reduced
- Alert volume reduced (and higher signal)

---

## Appendix: Hackathon Demo Narrative (2 minutes)

1. “Here’s the live ops dashboard.”
2. “Tasks arrive; fleet assigns and routes robots; you can see battery and collisions avoided.”
3. “We can manually inject tasks and handle alerts (ack + e-stop).”
4. “AI insight: one concise operational recommendation based on live metrics.”
5. “This is deployed on Vultr as the central backend; simulation and ops UI communicate via WebSocket.”

---

## Research Snippets (Footnote-Ready)

Use these as slide footnotes / credibility anchors:

- **Logistics robots adoption:** IFR reports **102,900 transportation & logistics** professional service robots sold in **2024** (+14%). (International Federation of Robotics)
- **RaaS tailwind:** IFR also highlights **Robot-as-a-Service** as a growing model in professional service robotics. (International Federation of Robotics)
- **Warehouse scale (US):** BLS reports **1,885,400 employees** and **20,455 establishments** in “Warehousing and storage” in **2024**. (U.S. Bureau of Labor Statistics)
- **E-commerce pressure (US):** U.S. Census reports e-commerce was **16.4% of total retail sales** in **Q3 2025**. (U.S. Census)
- **Category signal (RobOps + copilots):** InOrbit launched a “RobOps Copilot” (LLM-driven insights for robot fleet operations) at Automate 2024. (A3 Automate)
- **Enterprise operator signal:** DHL’s Logistics Trend Radar notes robotics adoption internally and projects significant growth in logistics robotics; DHL expects up to **30%** of its global material-handling equipment to use robotics automation by **2030**. (DHL)

Add the source links as slide footnotes when building the deck.
