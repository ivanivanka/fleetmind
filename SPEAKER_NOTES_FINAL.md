# FleetMind Speaker Notes (Final)

## SLIDE 1 - TITLE (~20 sec)

- I'm Ivan from Markster
- FleetMind: fleet orchestration for warehouse robots from different manufacturers
- Powered by Gemini Robotics-ER 1.5
- Problem, product, live demo

## SLIDE 2 - PROBLEM (~45 sec)

- You're an ops manager
- Bought Locus pickers last year, MiR transporters this year, Fetch forklifts just arrived
- Three vendors, three dashboards, three support contracts
- Your picker sits idle while a transporter blocks Aisle 7, neither system knows
- Enterprise platforms solve this: InOrbit, GreyOrange, Locus, 6 River
- But they cost half a million and take six months
- Mid-size operators get nothing
- That's who we build for

## SLIDE 3 - TECHNOLOGY (~55 sec)

- Gemini Robotics-ER 1.5
- DeepMind's embodied reasoning model
- In public preview right now via Google AI Studio
- State-of-the-art on 15 embodied reasoning benchmarks
- The key for us: **function calling**
- We define each manufacturer's robot API as a callable function
- ER 1.5 plans the task and calls the right robot
- Not an adapter layer, the model itself orchestrates across manufacturers
- **Spatial understanding**: processes camera/sensor feeds, detects congestion, zone awareness
- **Temporal reasoning**: why did throughput drop at 2pm? which charging pattern causes bottlenecks?
- **Multi-step planning**: "fulfill order" becomes locate, dispatch, route, pick, transport, verify
- Today's demo: standard Gemini API + rules-based pathfinding
- Production path: ER 1.5 replaces rules with embodied reasoning
- That's the difference between automation and intelligence

## SLIDE 4 - DEMO (~90 sec)

**Simulation** *(open http://149.28.198.127)*
- Live on a VM right now
- Twelve robots, three manufacturers
- Watch the collision avoidance, they re-route around each other
- *(click + Add Task)* Nearest robot with enough battery gets dispatched
- Path lights up from pickup to dropoff
- *(point to cost counter)* 48 cents saved per optimized pick
- Based on Fulfillment Advisor's survey of 600+ warehouses
- Semi-automated baseline is 60 cents per pick
- *(click AI Insight)* Gemini analyzing fleet patterns
- *(click E-Stop)* Emergency stop, everything halts, tasks re-queue on resume

**Platform** *(open http://149.28.198.127/platform/dashboard)*
- This is what the ops manager actually works with
- 47 robots across 3 warehouses, single interface
- *(click Analytics)* Six months of historical data
- Picks per hour up 60%
- Cost per pick down from 58 cents to 14
- Error rate from 2.1% to 0.3%
- *(click Insights)* AI recommendations powered by ER 1.5
- Predictive maintenance, throughput anomalies, fleet rebalancing
- Built in six hours, from zero to everything you just saw

## SLIDE 5 - TEAM (~45 sec)

**Ivan (me):**
- Orchestrate 59 AI agents every day
- Routing, prioritization, conflict resolution, resource allocation
- Zero employees, six-figure ARR
- That's fleet orchestration at a different layer
- 4 agency exits across Hungary, Scandinavia, UK, North America
- 500 Global, Plug and Play

**Attila (co-founder):**
- Co-founded Airtame: wireless streaming hardware + software
- Ten years as CTO
- Four founders to 120 people
- Half a million hardware units shipped
- Reverse-engineered streaming protocols when WiFi couldn't handle video
- Making heterogeneous hardware work through a software intelligence layer
- That's what he's been doing for a decade
- Red Dot Design Award, Best Startup CES 2014
- MSc Embedded Systems, DTU

**Together:**
- Known each other eight years
- Both code daily
- Both exited founders

## SLIDE 6 - VISION (~40 sec)

- Phase 1: connect to real hardware through ROS2
- Pilot with a mid-size warehouse
- Phase 2 is where it gets big
- Every pick generates consumption data
- The fleet is a sensor network
- We turn that into a replenishment API
- Vendors see what you're burning through in real time
- Ship just-in-time instead of safety stock
- Customers see fulfillment live
- Pay invoices faster
- Less inventory on shelves, less cash tied up
- Faster turns at every level of the value chain
- $150/robot/month SaaS
- 20,000 US warehousing businesses, mid-size underserved
- The fleet is the sensor network, FleetMind is the intelligence
- Demo is live. Thank you.
