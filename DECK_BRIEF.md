# FleetMind Pitch Deck Brief (Sequoia-Style)

This is a copy/paste-ready brief for building a standard Sequoia-style pitch deck.
It’s written to be honest about the current MVP (simulation-first) while still
telling a credible product story.

## Slide 1: Company Purpose

**Title (one line):** FleetMind is the control plane for warehouse robot fleets.

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

**What FleetMind is:**
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
- Founder bio (ops + AI + systems)
- Any relevant prior wins (if available)

---

## Slide 10: Financials + Vision

**Financials (early-stage):**
- 12-month plan: pilot -> paid -> expand robots/sites
- Unit economics model (per-robot SaaS + integration margin)

**Vision (closing line):**
- “FleetMind becomes the operating system for autonomous warehouse operations: planning, coordination, and continuous optimization across heterogeneous robot fleets.”

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
