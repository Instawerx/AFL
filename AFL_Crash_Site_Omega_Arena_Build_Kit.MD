Crash Site Omega — Arena Build Kit v1
Purpose

This build kit transforms the Crash Site Omega concept into a concrete Unreal level. It provides the visual map, lane breakdowns, landmark placement, phased build tasks and implementation order needed to construct a playable Assault arena for Avatar Fight League. Use this document as a checklist to block out, iterate and polish the map while preserving readability and gameplay flow.

1. Top‑Down Builder Map

The diagram below shows the arena layout in plain text. It highlights the major lanes, midfield wreck zone and objective core. This is your reference when placing lanes and cover in Unreal.

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DEPLOYMENT BAY ALPHA                                         │
│                                                                                              │
│   [Spawn Tunnel A]               [Launch Gate A]                 [Side Exit A]              │
│                                                                                              │
├───────────────────────────┬───────────────────────────────────────┬──────────────────────────┤
│                           │                                       │                          │
│       LEFT FLANK          │         CENTRAL ASSAULT LANE          │       RIGHT FLANK        │
│                           │                                       │                          │
│   [Low Cover Cluster]     │     [Cover Cluster A]                │   [Low Cover Cluster]    │
│   [Side Route Access]     │     [Forward Push Cover]             │   [Side Route Access]    │
│   [Industrial Debris]     │     [Ship Hull Entry Fragment]       │   [Radar/Antenna Debris] │
│                           │                                       │                          │
├───────────────────────────┼───────────────────────────────────────┼──────────────────────────┤
│                           │                                       │                          │
│      LEFT ROTATION        │         MIDFIELD WRECK ZONE           │      RIGHT ROTATION      │
│                           │                                       │                          │
│   [Flank Cover Node]      │   [Satellite Spine Landmark]          │   [Flank Cover Node]     │
│   [Broken Drone Area]     │   [Primary Combat Hotspot]            │   [Tower Debris Area]    │
│   [Retreat / Re‑entry]    │   [Collapsed Catwalk Fragment]        │   [Retreat / Re‑entry]   │
│                           │   [Turbine Debris Cluster]            │                          │
│                           │                                       │                          │
├───────────────────────────┼───────────────────────────────────────┼──────────────────────────┤
│                           │                                       │                          │
│    LEFT PUSH CHANNEL      │     OBJECTIVE APPROACH PRESSURE       │    RIGHT PUSH CHANNEL    │
│                           │                                       │                          │
│   [Advance Cover]         │   [Final Cover Cluster]              │   [Advance Cover]        │
│   [Pressure Angle]        │   [Objective Barrier]                │   [Pressure Angle]       │
│   [Reposition Point]      │   [Last Contest Zone]                │   [Reposition Point]     │
│                           │                                       │                          │
├───────────────────────────┴───────────────────────────────────────┴──────────────────────────┤
│                                                                                              │
│                                      OBJECTIVE CORE                                          │
│                                                                                              │
│                    [Crash Site Uplink Tower / Primary Score Zone]                           │
│                                                                                              │
│                    [Score Ring / Capture Radius / Final Contest Area]                       │
│                                                                                              │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│                                 DEPLOYMENT BAY OMEGA                                         │
│                                                                                              │
│   [Spawn Tunnel B]              [Launch Gate B]                  [Fallback Exit B]          │
│                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
2. Lane Identity Guide
A. Central Assault Lane

The main push route. It should be wide and dramatic with large cover blocks and clear forward pressure. This lane hosts the most collisions and is the centrepiece for spectators.

B. Left Flank Lane

A safer, tactical route with lower cover and industrial debris. Use it for repositioning and flanking but keep it readable.

C. Right Flank Lane

Mirrors the left flank but can feature radar towers and antenna debris to differentiate the silhouette. Ensure fairness with distinct visual flavour.

3. Major Landmarks
Crashed Ship Hull – A shattered hull fragment anchoring the midfield. Place it as one of the first props and use it to block line‑of‑sight and create movement choices.
Satellite Spine – A broken satellite spine forms the midfield wreck landmark. Use it to separate lanes and frame the central fight.
Collapsed Catwalk – A collapsed scaffold or bridge segment adds vertical drama but should not dominate play.
Objective Uplink Tower – The scoring structure at the far end of the map. It must be immediately recognizable and visible from the center lane.
Deployment Tunnels – Armoured spawn bays that introduce robots to the arena. They reinforce the broadcast fantasy with faction signage and launch gates.
4. Builder Task Phases
Phase 0 – Project Prep
Create the CrashSiteOmega map and necessary subfolders (Blockout, Props, Lighting, FX, Audio).
Set up Data Layers (Geo_Blockout, Gameplay, Objective, Broadcast, Lighting, FX, Audio).
Place temporary spawn markers.
Phase 1 – Macro Blockout
Block in the arena footprint with simple shapes, marking lane widths and overall dimensions.
Build deployment bays and clearly define centre and flank exits.
Sketch the central assault lane with major cover and hull placeholders.
Outline the left and right flanks with low walls and clean traversal.
Rough in the objective core with a stand‑in tower.
Phase 2 – Gameplay Flow Pass
Flesh out the midfield wreck zone with satellite spine and turbine debris. Create a natural collision hotspot.
Validate centre, left and right route flows end‑to‑end. Remove dead zones and confusing obstacles.
Adjust cover pieces to enforce purposeful movement. Every cover block must serve a tactical function.
Check readability from spectator camera angles and adjust lane width as needed.
Phase 3 – Landmark & Identity Pass
Replace placeholders with hero cargo props: the crashed hull, satellite spine and catwalk fragments.
Add AFL branding: holographic score pylons, banners, lane markers, faction signage.
Introduce broadcast structures: camera towers, floodlights and digital boards.
Phase 4 – Secondary Environment Pass
Add supporting props (broken drones, antenna towers, turbines) only where they enhance gameplay framing.
Dress the space sparingly with cables, crates and signage decals. Avoid clutter.
Phase 5 – FX & Lighting
Layer in steam vents, smoke plumes, sparks and warning strobes to heighten spectacle.
Implement lane lighting logic: spawn, midfield, objective highlight and broadcast accents.
Keep FX and lighting secondary to readability.
Phase 6 – First Review Package
Capture multiple top‑down and hero screenshots.
Record short clips of centre lane clash, midfield engagement and final objective push.
Assemble an internal review deck with notes on route flow, readability and broadcast value.
5. Unreal Implementation Order
Create the map and Data Layers. Use OFPA (One File Per Actor) workflow to avoid collisions.
Rough blockout using simple cubes and volumes to establish the playable area.
Test lane widths with robot capsule proxies to ensure enough room for collisions and flanking.
Replace placeholders with high‑fidelity Cargo assets for the hero props and major barriers.
Add gameplay anchors: spawn volumes, objective volumes, lane markers and camera anchors.
Integrate AFL branding and scoreboard structures for broadcast feel.
Add sound staging: prepare visual cues (lights, beacons) at key audio trigger locations.
Playtest for flow and readability. Do not proceed to heavy polish until the core loop is solid.

By following this build kit, you ensure that Crash Site Omega emerges as a readable, playable and broadcast‑worthy arena that embodies the AFL identity from the first pass.
