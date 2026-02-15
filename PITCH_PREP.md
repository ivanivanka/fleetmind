# FleetMind Pitch Prep — lablab.ai AI x Robotics Finals

## Event Details
- **Date:** Feb 15, 2026 — 10:30 AM
- **Location:** MindsDB SF office
- **Format:** 5 min pitch + 1 audience question
- **Context:** 15 finalists out of 4,410 submissions

## Judges
- **Paul Ruiz** — Google DeepMind, Embodied AI DevRel Lead
- **Rob Dahal** — AWS, Agentic AI Developer Advocate
- **David Yam** — Alibaba Cloud
- **Anton Kiselev** — judge (gave demo feedback)
- **Nathan Kay** — already sold on Ivan, gave strategic advice
- **Sanem Avcil** — gave review feedback

## Judge Feedback Summary (from submission round)

| Dimension | Paul | Sanem | Pattern |
|-----------|------|-------|---------|
| Tech | 5/5 | 5/5 | Locked in |
| Presentation | 4/5 | 4/5 | Solid |
| Business value | 3/5 | 4/5 | Improving |
| **Originality** | **3/5** | **3/5** | **THE weakness** |

### Anton's feedback
- Loved concept
- Demo "looks like hard-coded workflow of dots" — FIXED
- Collisions — FIXED
- "Adding tasks does not show anything useful" — FIXED

### Sanem's feedback
- "Very similar to FleetBridge, OmniPath, FleetMind (same idea)"
- "Less innovative than top tier"

## Nathan Kay's Strategic Advice
- Emphasize: 59 agents, 0 employees, six-figure ARR, 7M company database
- Don't mention Surge/tokens in pitch
- Don't oversell hackathon project — use it as proof of execution speed
- Pawel (lablab CEO) said Ivan should be "talking to his investors, not him"

## Robert Lee's Insight
- "Most warehouses have no visibility on how their robot fleets impact inventory turns"
- 15-year warehouse operations veteran

## Differentiation Strategy (must address originality 3/5)
1. **SMB-first** — everyone else sells enterprise. Ivan targets 10-100 robot operators.
2. **Physical intelligence** — embodied AI approach, not rules-based routing. Speaks to DeepMind's vision.
3. **Vendor-agnostic** — works across manufacturers. No lock-in.
4. **Founder parallel** — runs 59 AI agents with 0 employees. Same orchestration problem, different scale.

## Founder Credibility Markers (VERIFIED)
- 59 AI agents, 0 employees
- Six-figure ARR (NO exact number)
- 7M company database
- Partnerships: Microsoft, ElevenLabs
- Accelerated by: Plug & Play, Antler, 500 Global
- 7 exits
- CES Best Startup Award
- Red Dot Design Award
- Patented methodology
- ~~YC S25 callback~~ — NOT TRUE, removed
- ~~$250K ARR~~ — don't use exact figure

## Live Demo
- URL: http://149.28.198.127
- 12 robots, A* pathfinding, collision avoidance, battery management
- WebSocket real-time streaming, AI insight panel
- Task creation with visual flash feedback
- E-Stop capability
- Cost Saved metric (NOTE: $7.80/task figure is made up — consider removing or replacing)

## Code Changes Made This Session
1. `feat(ui)` — 60fps smooth movement, rounded rectangle robots, animated paths, zone labels
2. `fix(sim)` — Re-path blocked robots around obstacles
3. `fix(sim+ui)` — Claimed target cells, post-move safety net, visual separation
4. `feat(ui)` — Task flash overlay, cost metric, AI panel upgrade
5. `fix(ui)` — Canvas fills available space, metrics bar single row

## Pending / MUST FIX
- [ ] Build pitch deck in Gamma (use slide content below)
- [x] Remove fake cost saved metric from demo — DONE (replaced with Avg Task Time)
- [ ] Q&A cheat sheet
- [ ] Demo click sequence
- [ ] Verify demo speaker notes match what actually works (Add Task flash? AI Insight? E-Stop?)
- [ ] "500,000 robots" — NEEDS FRESH DATA, probably much higher. Web search needed.
- [ ] Name competitors explicitly (FleetBridge, OmniPath) and say WHY FleetMind is different
- [ ] VERIFY which achievements are Ivan's vs Attila's — some may be Attila's (CES? Red Dot?)
- [ ] Not all jury criticism addressed in deck — re-read feedback and cross-check

---

## FINAL DECK — 6 Slides for Gamma

### SLIDE 1 — HOOK

**On slide:**
- FleetMind AI
- Physical intelligence for warehouse robot fleets.
- Ivan Ivanka | Markster

**Speaker notes:**
Hey everyone, I'm Ivan from Markster. FleetMind is a control plane for warehouse robot fleets — but not the kind you've seen before. Let me show you why.

---

### SLIDE 2 — THE GAP

**On slide:**
- 500,000 robots deployed. Zero intelligence for the small operator.
- Enterprise platforms: $500K+ | Dedicated robotics teams | Vendor-locked
- Mid-size warehouse (10-100 robots): No cross-fleet visibility. No intelligence.
- "Most warehouses have zero visibility on how their robot fleets impact inventory turns." — Robert Lee, 15yr warehouse ops

**Speaker notes:**
There are over half a million warehouse robots deployed globally. The orchestration market exists — FleetBridge, OmniPath, they're out there. But they all build for the same customer: mega-warehouses with dedicated robotics teams and half-million dollar integration budgets. The fastest-growing robot buyer is the mid-size warehouse running 10 to 100 robots from multiple vendors. And they get nothing. A warehouse ops veteran told me this week most operators have zero visibility on how their fleets actually impact inventory turns. The gap isn't routing — it's intelligence.

---

### SLIDE 3 — WHAT'S DIFFERENT

**On slide:**
- One AI brain. Any vendor. Any scale.
- Vendor-agnostic — 3 robot manufacturers, 1 control plane
- Physical intelligence — AI that understands why throughput dropped, not just if/then rules
- Built for operators — No robotics engineers required

**Speaker notes:**
FleetMind does three things no existing platform does together. First — vendor-agnostic. Your fleet has robots from three different manufacturers? One screen. No $200K integration project. Second — physical intelligence. The system watches your fleet in real-time and tells you why utilization dropped, which robots to rebalance, when to pre-charge. This is the embodied AI approach — intelligence that understands the physical environment. Not rules-based routing. Third — built for operators, not PhD teams. An operations manager opens it and runs their fleet.

---

### SLIDE 4 — LIVE DEMO

**On slide:**
- Live Demo
- http://149.28.198.127

**Speaker notes:**
Let me show you. This is live right now on a cloud VM. 12-robot warehouse, real-time WebSocket streaming. Watch the robots — A* pathfinding with dynamic collision avoidance, they re-route around each other in real-time. Let me add tasks — see how priority-based dispatch assigns the nearest available robot instantly. See the path light up from pickup to dropoff. Now the AI insight — the intelligence layer analyzing fleet patterns and giving operational recommendations. And watch — E-Stop. Every robot halts. In-flight tasks re-queue. Resume and they pick right back up. Battery-aware scheduling too — low battery robots auto-route to charge before they die mid-task.

---

### SLIDE 5 — WHY ME

**On slide:**
- 59 AI agents | 0 employees | Six-figure ARR
- Microsoft & ElevenLabs partnerships | 7M company database
- Plug & Play | Antler | 500 Global | 7 exits
- CES Best Startup | Red Dot Award | Patented methodology
- "I orchestrate autonomous agents at scale. This is the same problem."

**Speaker notes:**
I run Markster, an AI-native agency. 59 autonomous AI agents, zero employees, six-figure revenue. Partnerships with Microsoft and ElevenLabs. 7 million company database. Accelerated by Plug & Play, Antler, and 500 Global. Seven exits, CES Best Startup, Red Dot Award, patented methodology. Every day I solve the exact same problem FleetMind solves — routing, prioritization, collision avoidance, resource management — for AI agents instead of physical robots. This working demo — built in days because the engineering is the same problem at a different layer.

---

### SLIDE 6 — WHAT'S NEXT

**On slide:**
- From simulation to production fleet control.
- Now: Working orchestration + AI intelligence + live dashboard
- Next: ROS2 bridge → Vendor APIs → Real hardware telemetry
- Live demo: http://149.28.198.127
- ivan@markster.ai | +1 212 718 1149

**Speaker notes:**
The roadmap is clear. ROS2 hardware bridge, vendor API connectors, real telemetry ingestion. The mid-size warehouse market is underserved and growing fast. We're building the control plane they can actually use. Demo is live, code is open source. Thank you.
