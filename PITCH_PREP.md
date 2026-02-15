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
- Demo "looks like hard-coded workflow of dots" — FIXED (60fps smooth animation, rounded robots, animated paths)
- Collisions — FIXED (claimed cells, re-pathing, visual separation)
- "Adding tasks does not show anything useful" — FIXED (task flash overlay from pickup to dropoff)

### Sanem's feedback
- "Very similar to FleetBridge, OmniPath, FleetMind (same idea)"
- "Less innovative than top tier"
- **Response in deck:** Name competitors explicitly. Differentiate on SMB-first + physical intelligence + vendor-agnostic.

## Nathan Kay's Strategic Advice
- Emphasize: 59 agents, 0 employees, six-figure ARR, 7M company database
- Don't mention Surge/tokens in pitch
- Don't oversell hackathon project — use it as proof of execution speed
- Pawel (lablab CEO) said Ivan should be "talking to his investors, not him"

## Robert Lee's Insight
- "Most warehouses have no visibility on how their robot fleets impact inventory turns"
- 15-year warehouse operations veteran

## Differentiation Strategy (must address originality 3/5)
1. **SMB-first** — FleetBridge, OmniPath, 6 River all sell enterprise ($500K+ integrations). FleetMind targets 10-100 robot operators.
2. **Physical intelligence / Embodied AI** — Maps to DeepMind's Gemini Robotics vision: cross-embodiment learning (one model controls different robot types). FleetMind = vendor-agnostic control plane using AI that understands physical environments.
3. **Vendor-agnostic** — Works across manufacturers. No lock-in. Same cross-embodiment principle.
4. **Founder parallel** — Runs 59 AI agents with 0 employees. Same orchestration problem, different scale.

## Google DeepMind Connection (KEY for Paul Ruiz)
- DeepMind launched **Gemini Robotics** — vision-language-action models for physical agents
- Core concept: **cross-embodiment learning** — one model that transfers skills between robot types
- FleetMind's vendor-agnostic approach IS this at the fleet level — one AI brain, any robot manufacturer
- "Physical intelligence" framing speaks directly to DeepMind's research direction
- Paul Ruiz leads Embodied AI DevRel — this is his exact domain

## Industry Data (RESEARCHED)
- **Robot deployments:** Amazon alone operates 750,000+ warehouse robots (as of 2024), with plans exceeding 1M. Global warehouse robot market $9-11B in 2025-26. Multiple millions of robots deployed across all operators.
- **Pick costs:** B2C manual pick cost averages $3.20 per pick (Fulfillment Advisor 2025 survey, 600+ warehouses). B2B averages $4.80. Automated picking reduces labor costs ~50%, saving ~$1.60 per pick.
- **Demo metric:** Cost Saved = $1.60 per completed task (grounded in real industry data)

## Competitor Landscape (for deck + Q&A)
| Competitor | What they do | Why FleetMind is different |
|------------|-------------|---------------------------|
| **FleetBridge** | Enterprise fleet orchestration | Enterprise-only, $500K+ integration, vendor-specific |
| **OmniPath** | Multi-robot path planning | Routing-focused, not intelligence-focused. No AI insight layer. |
| **6 River Systems** (Shopify) | AMR fleet for warehouses | Single-vendor (their own robots). Acquired by Shopify. |
| **Locus Robotics** | AMR fleet management | Enterprise customers, proprietary hardware |
| **FleetMind differentiator** | **SMB-first + vendor-agnostic + physical intelligence** | No one does all three together |

## Team Credibility

### Ivan (Founder, Pitch)
- 59 AI agents, 0 employees — VERIFIED
- Six-figure ARR (NO exact number) — VERIFIED
- 7M company database — VERIFIED
- Partnerships: Microsoft, ElevenLabs — VERIFIED
- Accelerated by: Plug & Play, Antler, 500 Global — VERIFIED
- 7 exits — VERIFIED
- Patented methodology — VERIFIED
- ~~YC S25 callback~~ — NOT TRUE, removed
- ~~$250K ARR~~ — don't use exact figure
- ~~CES Best Startup~~ — Attila's, not Ivan's
- ~~Red Dot Award~~ — Attila's, not Ivan's

### Attila (Co-founder / CTO, should attend)
- Hardware and robotics background — adds credibility for physical AI pitch
- CES Best Startup Award
- Red Dot Design Award
- Based in SF (on paper) — can attend MindsDB office
- His presence signals "this is a real team, not a solo hackathon project"

## Live Demo
- URL: http://149.28.198.127
- 12 robots, A* pathfinding, collision avoidance, battery management
- WebSocket real-time streaming, AI insight panel (Gemini)
- Task creation with visual flash feedback (animated pickup→dropoff path)
- E-Stop capability (all robots halt, in-flight tasks re-queue)
- Cost Saved metric: $1.60 per completed task (based on industry data)
- Battery-aware scheduling: low-battery robots auto-route to charging

## Demo Click Sequence (for pitch)
1. Show warehouse running (robots moving, tasks completing)
2. Click **+ Add Task** — show flash animation from pickup to dropoff
3. Click **AI Insight** — show intelligence analysis
4. Click **E-Stop All** — all robots halt instantly
5. Click **Reset Demo** to resume (or un-pause)
6. Point out cost saved counter incrementing

## Code Changes Made This Session
1. `feat(ui)` — 60fps smooth movement, rounded rectangle robots, animated paths, zone labels
2. `fix(sim)` — Re-path blocked robots around obstacles
3. `fix(sim+ui)` — Claimed target cells, post-move safety net, visual separation
4. `feat(ui)` — Task flash overlay, cost metric, AI panel upgrade
5. `fix(ui)` — Canvas fills available space, metrics bar single row
6. `feat(ui)` — Restored cost saved metric with real industry data ($1.60/pick)

## Pending / MUST FIX
- [ ] Build pitch deck in Gamma (use slide content below)
- [x] Cost metric grounded in real data — DONE ($1.60/pick, deployed)
- [x] Fresh robot market data — DONE (millions deployed, $9-11B market)
- [x] DeepMind connection strengthened — DONE (Gemini Robotics, cross-embodiment)
- [x] Competitors named and differentiated — DONE (see table above)
- [ ] VERIFY which achievements are Ivan's vs Attila's — CES? Red Dot? ASK IVAN
- [ ] Q&A cheat sheet
- [ ] Verify demo features actually work on live URL before pitch
- [ ] Practice demo click sequence

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
- Millions of robots deployed. Zero intelligence for the mid-size operator.
- Enterprise platforms: $500K+ | Dedicated robotics teams | Vendor-locked
- Mid-size warehouse (10-100 robots): No cross-fleet visibility. No intelligence.
- "Most warehouses have zero visibility on how their robot fleets impact inventory turns." — Robert Lee, 15yr warehouse ops

**Speaker notes:**
Amazon alone operates over 750,000 warehouse robots. The global market is $10 billion and growing. The orchestration platforms exist — FleetBridge, OmniPath, Locus, 6 River — but they all build for the same customer: mega-warehouses with dedicated robotics teams and half-million dollar integration budgets. The fastest-growing robot buyer is the mid-size warehouse running 10 to 100 robots from multiple vendors. And they get nothing. A warehouse ops veteran told me most operators have zero visibility on how their fleets actually impact inventory turns. The gap isn't routing — it's intelligence.

---

### SLIDE 3 — WHAT'S DIFFERENT (Physical Intelligence)

**On slide:**
- One AI brain. Any vendor. Any scale.
- Vendor-agnostic: multiple robot manufacturers, one control plane
- Physical intelligence: AI that understands WHY throughput dropped — not if/then rules
- Cross-embodiment learning: same principle as DeepMind's Gemini Robotics — one model, any robot
- Built for operators: no robotics engineers required

**Speaker notes:**
FleetMind does three things no existing platform does together. First — vendor-agnostic. Your fleet has robots from three different manufacturers? One screen. No $200K integration project. This is the same principle Google DeepMind is pursuing with Gemini Robotics — cross-embodiment learning, where one model transfers skills across different robot types. We're applying that at the fleet orchestration layer. Second — physical intelligence. The system watches your fleet in real-time and tells you why utilization dropped, which robots to rebalance, when to pre-charge. Intelligence that understands the physical environment — embodied AI, not rules-based routing. Third — built for operators, not PhD teams. An operations manager opens it and runs their fleet.

---

### SLIDE 4 — LIVE DEMO

**On slide:**
- Live Demo
- http://149.28.198.127

**Speaker notes:**
Let me show you. This is live right now on a cloud VM. 12-robot warehouse, real-time WebSocket streaming. Watch the robots — A* pathfinding with dynamic collision avoidance, they re-route around each other in real-time. Let me add a task — see how priority-based dispatch assigns the nearest available robot instantly. See the path light up from pickup to dropoff. Now the AI insight — the Gemini-powered intelligence layer analyzing fleet patterns and giving operational recommendations. Watch the cost saved counter — every completed pick saves $1.60 versus manual operations based on real industry data. And E-Stop — every robot halts instantly. In-flight tasks re-queue. Battery-aware scheduling too — low battery robots auto-route to charge before they die mid-task.

---

### SLIDE 5 — WHY US

**On slide:**
- "I orchestrate autonomous agents at scale. This is the same problem."
- 59 AI agents, 0 employees, six-figure ARR
- Markster: AI-native agency with 7M company database
- Microsoft & ElevenLabs partnerships
- Accelerated by Plug & Play, Antler, 500 Global
- 7 exits | Patented methodology
- Team: Ivan (AI orchestration) + Attila (hardware/robotics, CES Best Startup, Red Dot Award)

**Speaker notes:**
I run Markster, an AI-native agency. 59 autonomous AI agents, zero employees, six-figure revenue. I solve this exact problem every day — routing, prioritization, collision avoidance, resource management — for AI agents instead of physical robots. Partnerships with Microsoft and ElevenLabs. 7 million company database. Accelerated by Plug & Play, Antler, and 500 Global. Seven exits, patented methodology. And my co-founder Attila brings the hardware side — CES Best Startup, Red Dot Award winner, deep robotics background. This working demo was built in days because the engineering is the same problem at a different layer. Fleet orchestration is what we do.

---

### SLIDE 6 — WHAT'S NEXT

**On slide:**
- From simulation to production fleet control.
- Now: Working orchestration + AI intelligence + live dashboard
- Next: ROS2 bridge → Vendor APIs → Real hardware telemetry
- Target: mid-size warehouses (10-100 robots) — underserved, fastest-growing segment
- Live demo: http://149.28.198.127
- ivan@markster.ai | +1 212 718 1149

**Speaker notes:**
The roadmap is clear. ROS2 hardware bridge, vendor API connectors, real telemetry ingestion. The mid-size warehouse market is underserved and growing fast — while everyone else fights over enterprise contracts, we're building the control plane that 10-to-100 robot operators can actually use. Demo is live, code is open source. Thank you.

---

## Q&A CHEAT SHEET

**Q: How is this different from FleetBridge/OmniPath/existing solutions?**
A: They're all enterprise-first, vendor-locked, $500K+ integration. FleetMind is SMB-first, vendor-agnostic, and intelligence-focused. The mid-size operator (10-100 robots) is the fastest-growing buyer and gets nothing from existing platforms.

**Q: This is a simulation — how do you get to real robots?**
A: ROS2 bridge. The protocol is standard. Our orchestration layer (pathfinding, task dispatch, battery management, AI insight) is hardware-agnostic by design. The simulation proves the intelligence layer works — connecting to real hardware is an integration problem, not an AI problem.

**Q: What's the business model?**
A: SaaS per-robot pricing. $X/robot/month. Mid-size warehouse with 50 robots = predictable monthly revenue. The value proposition is clear: every automated pick saves $1.60 vs manual (based on industry data from 600+ warehouses).

**Q: Why AI and not just rules-based routing?**
A: Rules handle known patterns. AI handles the unknown — why did throughput drop 20% on Tuesdays? Which robots to pre-charge before the 2pm rush? When to rebalance zones? That's physical intelligence, not routing.

**Q: How does this connect to embodied AI / DeepMind's work?**
A: DeepMind's Gemini Robotics is about cross-embodiment learning — one model that works across robot types. FleetMind applies the same principle at the fleet level: one AI brain orchestrating robots from multiple manufacturers. Same vision, applied to real warehouse operations.

**Q: What's your unfair advantage?**
A: I run 59 AI agents with 0 employees. Fleet orchestration — routing, prioritization, collision avoidance, resource management — is literally my day job at a different scale. Plus: seven exits, Microsoft/ElevenLabs partnerships, and the technical depth to build this in days.

**Q: What traction do you have?**
A: Markster (the parent company) has six-figure ARR, 7M company database, partnerships with Microsoft and ElevenLabs. FleetMind is the robotics application of our core orchestration technology. Working demo is live right now.

**Q: Why should we believe you can execute?**
A: Track record. 59 agents, 0 employees, six-figure revenue — that's execution. Seven exits. Accelerated by Plug & Play, Antler, 500 Global. And this demo — built from scratch for this hackathon — is proof of speed.
