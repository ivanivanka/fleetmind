# FleetMind Pitch — Claim Verification Sheet

Every number in the deck with its source link. Read before pitching.

---

## SLIDE 2 — THE PROBLEM

| Claim | Source | Link | Status |
|-------|--------|------|--------|
| $10.9B warehouse robotics market in 2026 | Mordor Intelligence | [mordorintelligence.com](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) | VERIFIED |
| 17.5% CAGR → $24.55B by 2031 | Mordor Intelligence (same report) | [mordorintelligence.com](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) | VERIFIED |
| Amazon 750,000+ robots (2024), crossed 1M in 2025 | About Amazon official blog | [aboutamazon.com](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) | VERIFIED |
| $500K+ enterprise integration cost | Industry standard for WMS/fleet software full deployment — multiple sources reference this range | [Interact Analysis](https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/) | DIRECTIONAL — common industry figure, no single source |
| ~20,000 warehousing businesses in US | Statista (2021 data, latest available) | [statista.com](https://www.statista.com/statistics/873492/total-number-of-warehouses-united-states/) | VERIFIED (but 2021 — likely higher in 2026) |
| Robert Lee quote | Conversation with Ivan (not published) | N/A — personal source | UNVERIFIABLE by judges |

### IMPORTANT: "FleetBridge" and "OmniPath" ARE NOT REAL COMPANIES
Sanem referenced these in her feedback — they are likely **other hackathon submissions**, not established players. Do NOT name them as competitors in the pitch. The real multi-vendor fleet orchestration competitors are:
- **InOrbit** — [inorbit.ai](https://www.inorbit.ai/) — cloud-based, vendor-agnostic fleet management
- **GreyOrange (GreyMatter)** — [greyorange.com](https://www.greyorange.com/) — hardware-agnostic orchestration platform
- **CoEvolution** — multi-agent orchestration, no own hardware
- **KINEXON** — [kinexon.com](https://kinexon.com/solutions/amr-agv-fleet-management) — AMR/AGV fleet management
- **Roboteon** — [roboteon.com](https://www.roboteon.com/orchestration) — warehouse robotics orchestration
- **6 River Systems** (Shopify) — single-vendor (their own robots)
- **Locus Robotics** — enterprise, proprietary hardware

---

## SLIDE 3 — THE PRODUCT (Gemini Robotics)

| Claim | Source | Link | Status |
|-------|--------|------|--------|
| Gemini Robotics-ER 1.5 exists | Google DeepMind official | [deepmind.google](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/) | VERIFIED |
| Available in public preview via Google AI Studio | Google AI for Developers docs | [ai.google.dev](https://ai.google.dev/gemini-api/docs/robotics-overview) | VERIFIED |
| Task decomposition capability | DeepMind: "Deconstructs natural language commands into subtasks" | [deepmind.google](https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) | VERIFIED |
| Spatial understanding capability | DeepMind: "advanced spatial understanding to perceive and understand the surrounding environment" | [deepmind.google](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/) | VERIFIED |
| Function calling for robot APIs | Google AI docs: extensive examples of custom function definitions | [ai.google.dev](https://ai.google.dev/gemini-api/docs/robotics-overview) | VERIFIED |
| Temporal reasoning capability | DeepMind: "Reason spatially and temporally" | [deepmind.google](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/) | VERIFIED |
| "In preview" (not GA) | Model ID: `gemini-robotics-er-1.5-preview` | [ai.google.dev](https://ai.google.dev/gemini-api/docs/robotics-overview) | VERIFIED — be honest about preview status |
| State-of-the-art on 15 embodied reasoning benchmarks | DeepMind blog | [deepmind.google](https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) | VERIFIED |

---

## SLIDE 4 — LIVE DEMO

| Claim | Source | Link | Status |
|-------|--------|------|--------|
| Built in ~6 hours | Ivan's hackathon build time | N/A — your claim, be accurate | SELF-REPORTED |
| $0.48 saved per optimized pick | Derived: semi-auto $0.60 avg → optimized $0.12 = $0.48 savings | See cost breakdown below | DERIVED — math checks out |
| Manual pick cost $3.18 B2C | Fulfillment Advisor 2025 survey (600+ warehouses) | [thefulfillmentadvisor.com](https://www.thefulfillmentadvisor.com/2025-warehousing-market-report/) | VERIFIED |
| Manual pick cost $4.80 B2B | Same survey | [thefulfillmentadvisor.com](https://www.thefulfillmentadvisor.com/2025-warehousing-market-report/) | VERIFIED |
| Semi-automated: $0.45-$0.75/pick | Atomoving warehouse picking performance report | [atomoving.com](https://atomoving.com/blog/order-picker/warehouse-picking-performance-setting-and-hitting-the-right-targets-16012026-upgrade/) | VERIFIED |
| Fully automated: $0.25-$0.45/pick | Same source | [atomoving.com](https://atomoving.com/blog/order-picker/warehouse-picking-performance-setting-and-hitting-the-right-targets-16012026-upgrade/) | VERIFIED |

### Cost Metric Math
- Semi-automated average: ($0.45 + $0.75) / 2 = **$0.60/pick**
- Fully automated average: ($0.25 + $0.45) / 2 = **$0.35/pick**
- FleetMind-optimized target: $0.12/pick (optimistic — at top of fully automated range)
- **$0.48 savings = $0.60 - $0.12**
- NOTE: The $0.12 target is aspirational. More conservative: $0.60 - $0.35 = $0.25 savings per pick. Consider using $0.25 if you want to be bulletproof.

---

## SLIDE 5 — WHY US

| Claim | Source | Status |
|-------|--------|--------|
| Ivan: 59 AI agents, 0 employees | Ivan self-reported, verified in previous sessions | VERIFIED |
| Six-figure ARR | Ivan confirmed (no exact number) | VERIFIED — don't say exact amount |
| 7M company database | Ivan confirmed | VERIFIED |
| Partnerships: Microsoft, ElevenLabs | Ivan confirmed | VERIFIED |
| Accelerated by: Plug & Play, Antler, 500 Global | Ivan confirmed | VERIFIED |
| 7 exits | Ivan confirmed | VERIFIED |
| Patented methodology | Ivan confirmed | VERIFIED |
| Attila: 8-figure exit (AI hardware team) | Ivan stated this session | VERIFY WITH ATTILA |
| Attila: CES Best Startup Award | Ivan confirmed (Attila's, not Ivan's) | VERIFIED as Attila's |
| Attila: Red Dot Design Award | Ivan confirmed (Attila's, not Ivan's) | VERIFIED as Attila's |

---

## SLIDE 6 — WHAT'S NEXT

| Claim | Source | Link | Status |
|-------|--------|------|--------|
| $150/robot/month pricing | Ivan's pricing model | N/A — your business decision | SELF-SET |
| ~20,000 US warehousing businesses | Statista 2021 | [statista.com](https://www.statista.com/statistics/873492/total-number-of-warehouses-united-states/) | VERIFIED (2021 data) |
| AMR transport: $25K-$40K/unit | Qviro 2025 AMR cost analysis | [qviro.com](https://qviro.com/blog/cost-of-autonomous-mobile-robots/) | VERIFIED |
| Mobile picking robot: $50K-$60K | Qviro (same source) | [qviro.com](https://qviro.com/blog/cost-of-autonomous-mobile-robots/) | VERIFIED |
| Manual pick error rate 4% vs automated 0.04% | Multiple industry sources | [atomoving.com](https://atomoving.com/blog/order-picker/warehouse-picking-performance-setting-and-hitting-the-right-targets-16012026-upgrade/) | VERIFIED |
| 50% of large warehouses deploy robots by end 2025 | Industry analysis | [mordorintelligence.com](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) | VERIFIED |
| Multi-fleet orchestration growing 138% CAGR | Interact Analysis | [interactanalysis.com](https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/) | VERIFIED |

---

## Q&A BACKUP DATA

| If asked about... | Key number | Source |
|-------------------|-----------|--------|
| Market size | $10.9B in 2026 | [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) |
| Growth rate | 17.5% CAGR to $24.55B by 2031 | [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) |
| Orchestration segment growth | 138% CAGR 2021-2027 | [Interact Analysis](https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/) |
| Amazon robots | 750K (2024) → 1M+ (2025) | [About Amazon](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) |
| Manual pick cost | $3.18-$3.20 B2C, $4.79-$4.80 B2B | [Fulfillment Advisor 2025](https://www.thefulfillmentadvisor.com/2025-warehousing-market-report/) |
| Automated pick cost | $0.25-$0.45 fully auto, $0.45-$0.75 semi-auto | [Atomoving](https://atomoving.com/blog/order-picker/warehouse-picking-performance-setting-and-hitting-the-right-targets-16012026-upgrade/) |
| Picks per hour | Manual 80-120, robot-assisted 200-300 | [Atomoving](https://atomoving.com/blog/order-picker/warehouse-picking-performance-setting-and-hitting-the-right-targets-16012026-upgrade/) |
| AMR unit cost | $25K-$100K depending on type | [Qviro](https://qviro.com/blog/cost-of-autonomous-mobile-robots/) |
| Fleet mgmt software cost | $5K-$15K/robot | [Qviro](https://qviro.com/blog/cost-of-autonomous-mobile-robots/) |
| US warehouses | ~20,000 businesses (2021) | [Statista](https://www.statista.com/statistics/873492/total-number-of-warehouses-united-states/) |
| 50% large adopt by 2025 | Mordor Intelligence | [mordorintelligence.com](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market) |
| Gartner: 50% deploy orchestration by 2026 | Gartner via Robotics 24/7 | [robotics247.com](https://www.robotics247.com/article/multiagent_orchestration_platforms_directs_warehouse_robot_fleets_predicts_gartner_research) |
| Gemini Robotics-ER 1.5 | DeepMind official | [deepmind.google](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/) |
| ER 1.5 API docs | Google AI for Developers | [ai.google.dev](https://ai.google.dev/gemini-api/docs/robotics-overview) |
| Real competitors | InOrbit, GreyOrange, CoEvolution, KINEXON, Roboteon | See links above |
