# AFL Unreal Build Constitution v1

## Purpose
This document is the binding internal rulebook for building **Avatar Fight League** in Unreal.

Its job is to prevent:
- architecture drift
- AI-generated chaos
- inconsistent asset organization
- unreadable arenas
- weak online/economy authority
- generic UI that ignores the robotics identity

This constitution is not a pitch document.  
It is the **production law** for the AFL Unreal project.

---

# 1. Core Identity Rules

## 1.1 AFL is a robotics-centric sports-combat platform
AFL is not a generic shooter, not a fantasy brawler, and not a military sim.

Everything built must reinforce:
- humanoid robot competition
- teleoperation / machine intelligence feel
- broadcast-ready sports spectacle
- readable competitive gameplay
- modular support for multiple combat families

## 1.2 AFL supports multiple combat families
The project must be built to support:
- **Melee / Tackle / Impact**
- **Hitscan / Laser Tag**
- **Projectile / Paintball / Splat**

No system may be hardcoded as “Assault-only” unless it is intentionally owned by `AFLModeAssault`.

## 1.3 Lyra is a chassis, not the product identity
Lyra systems may be reused, abstracted, or adapted.

Lyra sample identity must not bleed into AFL.

### Keep
- input patterns
- GAS patterns
- ranged combat foundations
- multiplayer-safe framework
- useful equipment/inventory patterns
- reusable camera and state structure

### Remove or isolate
- sample maps
- dead demo content
- irrelevant UI
- unused cosmetics/emotes
- unused sample experiences
- placeholder content that does not serve AFL modes

---

# 2. Non-Negotiable Production Laws

## 2.1 No feature enters production without ownership
Every feature must answer:
1. Which module owns it?
2. Which mode uses it?
3. Which arena events trigger it?
4. What UI/broadcast state does it affect?
5. What validation or test proves it works?

If those answers do not exist, the feature is not ready.

## 2.2 No compile-only success
A build is not considered good because it compiles.

A build is only acceptable when it passes:
- content validation
- logic validation
- automated tests
- packaged smoke checks
- protected-zone review when relevant

## 2.3 AI is an accelerator, not the authority
Claude and NeoStack may accelerate development.

They do not own:
- reward truth
- session truth
- security/auth
- anti-abuse logic
- final merge authority
- replication-critical rules without review

## 2.4 Arena readability outranks visual clutter
Every arena object must justify itself through at least one of:
- gameplay value
- readability value
- broadcast/camera value

If it does none of these, it does not belong in the first pass.

## 2.5 Robotics identity is mandatory in UI
AFL UI must feel like:
- a command center
- a teleoperation HUD
- a robotics diagnostics system
- a competitive machine sport broadcast

It must not feel like:
- fantasy game HUD
- generic neon sci-fi UI with no purpose
- cartoon esports overlay
- military shooter clone menus

---

# 3. Project Structure Law

## 3.1 Top-level module structure
```text
AFL/
├─ Source/
│  ├─ AFLCore/
│  ├─ AFLCombatCore/
│  ├─ AFLCombatMelee/
│  ├─ AFLCombatHitscan/
│  ├─ AFLCombatProjectile/
│  ├─ AFLArena/
│  ├─ AFLModeAssault/
│  ├─ AFLModeLaserTag/
│  ├─ AFLModePaintball/
│  ├─ AFLMatchmaking/
│  ├─ AFLEconomy/
│  ├─ AFLProgression/
│  ├─ AFLBroadcast/
│  ├─ AFLAudio/
│  ├─ AFLUI/
│  ├─ AFLNet/
│  └─ AFLTools/
├─ Plugins/
│  ├─ AFLGameFeatures/
│  ├─ AFLAutomation/
│  ├─ AFLCargoPipeline/
│  ├─ AFLElevenImport/
│  └─ AFLDevValidation/
├─ Content/
│  ├─ AFL/
│  ├─ Arenas/
│  ├─ Robots/
│  ├─ UI/
│  ├─ Audio/
│  ├─ Broadcast/
│  └─ Prototype/
└─ Docs/
   └─ AFL/
```

## 3.2 No feature code in random locations
New feature logic may not be buried in:
- unrelated Blueprints
- widgets
- map Level Blueprints unless explicitly approved
- temporary sample folders
- test folders that quietly became production

---

# 4. Module Ownership Law

## 4.1 AFLCore
Owns:
- robot base pawn
- shared robot state
- structure/health/stamina/energy baseline
- team/shared enums
- shared gameplay tags
- shared structs
- base interaction rules

## 4.2 AFLCombatCore
Owns:
- shared combat vocabulary
- hit event interfaces
- combat data assets
- combat routing
- common telemetry events

## 4.3 AFLCombatMelee
Owns:
- tackles
- collisions
- impact rules
- knockback
- clear-outs
- denial-impact interactions

## 4.4 AFLCombatHitscan
Owns:
- beam/laser tracing
- tag confirmation
- hitscan scoring impacts
- laser-specific weapon behavior

## 4.5 AFLCombatProjectile
Owns:
- projectile spawning
- travel behavior
- splat/paint logic
- projectile hit resolution

## 4.6 AFLArena
Owns:
- round manager
- spawn zones
- objective zones
- overtime
- win conditions
- arena-local hazard hooks
- arena camera anchors
- arena event anchors

## 4.7 Mode modules
`AFLModeAssault`, `AFLModeLaserTag`, and `AFLModePaintball` own only their mode-specific rules.

They must not become dumping grounds for shared combat systems.

## 4.8 AFLMatchmaking
Owns:
- queue logic
- parties/lobbies
- session handoff
- reconnect flow
- hidden MMR hooks
- session-type metadata

## 4.9 AFLEconomy
Owns:
- Coins
- Tickets
- payouts
- reward rules
- reward anti-abuse checks
- entry consumption

## 4.10 AFLProgression
Owns:
- XP
- mastery
- rank metadata
- seasonal or account progression shells

## 4.11 AFLBroadcast
Owns:
- spectator cameras
- overlays
- replay hooks
- event callout hooks
- lower-third style logic
- presentation metadata

## 4.12 AFLAudio
Owns:
- imported voice assets
- event cue routing
- announcer trigger mapping
- stingers
- robotic voice event categories

## 4.13 AFLUI
Owns:
- menus
- queue flow
- wallet/progression views
- HUD
- telemetry panels
- match summary panels

## 4.14 AFLTools
Owns:
- validators
- dev commands
- automation hooks
- debug visualizers
- arena verification helpers

---

# 5. Naming Convention Law

## 5.1 General asset prefixes
Use strict prefixes.

```text
BP_   Blueprint
ABP_  Animation Blueprint
WBP_  Widget Blueprint
GA_   Gameplay Ability
GE_   Gameplay Effect
GCN_  Gameplay Cue Notify
DA_   Data Asset
DT_   Data Table
MI_   Material Instance
M_    Master Material
SM_   Static Mesh
SK_   Skeletal Mesh
T_    Texture
SFX_  Sound effect
VO_   Voice asset
SC_   Sound Cue
MS_   MetaSound
FX_   Niagara/visual FX
MAP_  Map name
GM_   Game Mode
GS_   Game State
PS_   Player State
PC_   Player Controller
BFL_  Blueprint Function Library
E_    Enum
ST_   Struct
IF_   Interface
```

## 5.2 Arena naming
```text
MAP_CrashSiteOmega
MAP_LaserTag_01
MAP_Paintball_01
```

## 5.3 Widget naming
HUD widgets must make their purpose obvious.

Examples:
```text
WBP_HUD_TelemetryCore
WBP_HUD_ObjectiveStatus
WBP_HUD_RobotVitals
WBP_Menu_QueueSelect
WBP_Menu_MatchSummary
```

## 5.4 Data Assets
Never use vague names like:
- `DA_Test`
- `DA_NewData`
- `DA_Values`

Use:
```text
DA_AssaultCore_ScoreRules
DA_CrashSiteOmega_ObjectiveConfig
DA_Economy_PayoutRules_QuickMatch
DA_UI_TelemetryStyle_Primary
```

---

# 6. Content Folder Law

## 6.1 Arena folder structure
Each arena must have a clean internal structure.

```text
Content/Arenas/CrashSiteOmega/
├─ Maps/
├─ Geometry/
├─ Materials/
├─ Props/
├─ Gameplay/
├─ Audio/
├─ Lighting/
├─ FX/
├─ Broadcast/
└─ UIRefs/
```

## 6.2 Robot folder structure
```text
Content/Robots/
├─ Base/
├─ Variants/
├─ Animations/
├─ Audio/
├─ Materials/
├─ UI/
└─ Data/
```

## 6.3 No dumping into Prototype forever
Prototype folders are temporary.

Anything that graduates to production must be moved into correct production folders before merge.

---

# 7. Arena Build Law

## 7.1 Every arena must start from a reference pack
No arena enters serious production without:
- hero key art
- top-down tactical map
- builder board
- gameplay flow overlay
- objective detail sheet
- spawn/deployment detail sheet

## 7.2 Macro before micro
Builder passes must be:
1. footprint/blockout
2. lane flow/readability
3. gameplay anchors
4. identity landmarks
5. secondary props
6. FX/polish

No heavy dressing before route quality is proven.

## 7.3 Arena layout rules
Every competitive arena must clearly define:
- spawn/deployment spaces
- primary route
- alternative routes
- collision hotspots
- objective approach
- objective climax zone
- broadcast camera value

## 7.4 Arena Data Layers
All production arenas should separate at minimum:
```text
DL_Geo_Blockout
DL_Geo_Final
DL_Gameplay
DL_Objective
DL_Broadcast
DL_Lighting
DL_FX
DL_Audio
```

---

# 8. HUD / Telemetry Design Constitution

## 8.1 AFL UI style mandate
All player-facing control surfaces must feel like robotics command and telemetry systems first, game UI second.

### Visual principles
- diagnostic clarity over decoration
- machine-state readability over abstract style
- functional panel logic
- tactical overlays
- layered telemetry
- camera-feed / control-room energy
- premium robotic sport broadcast polish

## 8.2 Mandatory HUD identity
The default AFL HUD language must include some or all of:
- robot vitals
- actuator/structure status
- energy/stamina
- objective state
- signal/lock/target state where applicable
- team telemetry
- lane/objective indicators
- impact alerts
- command confirmations
- mode-specific weapon or tackle system state

## 8.3 UI should resemble
- vehicle telemetry
- robotics lab dashboards
- teleop pilot systems
- futuristic control rooms
- live machine diagnostics
- esports broadcast overlays fused with robotics readouts

## 8.4 UI should not resemble
- fantasy RPG HUDs
- soft bubbly mobile UI
- generic glass-only sci-fi panels with no operational meaning
- arcade toy UI lacking machine-state depth

## 8.5 HUD layer model
```text
Layer 1 = Critical robot status
Layer 2 = Objective and match state
Layer 3 = Combat state
Layer 4 = Tactical/broadcast enhancements
Layer 5 = Alerts and replay/event messaging
```

## 8.6 Default telemetry panels
At minimum, AFL competitive HUD must support:
- robot vitals panel
- structure/stamina/energy panel
- objective/capture progress panel
- match timer and score panel
- mode-appropriate weapon or tackle readiness panel
- directional tactical event alerts
- connection/signal state if relevant to fantasy/teleop framing

## 8.7 Color law
Base AFL UI tones should prioritize:
- dark steel / charcoal / black foundations
- electric cyan / cool white / tactical green accents
- amber/warning orange for faults or alert states
- controlled red for critical failure states

The UI may be stylish, but every color must carry meaning.

## 8.8 Typography law
Use typography that feels:
- technical
- broadcast legible
- clean
- machine-operational

Avoid playful or whimsical typography.

## 8.9 Motion law
UI animation should feel like:
- calibration
- signal acquisition
- system alerts
- scan sweeps
- mode changes
- robotic confirmation

Avoid floaty meaningless animation.

---

# 9. Matchmaking and Economy Law

## 9.1 Session classes
All matches must belong to one of these:
```text
PublicCompetitive
PrivateLobby
SkillsChallenge
SpectatorOnly
InternalTest
```

## 9.2 Reward truth
Economy rewards are never client-authoritative.

All reward grants must resolve through protected server-side or trusted backend authority.

## 9.3 Reduced-reward law
Private and InternalTest sessions must not quietly grant full competitive rewards.

## 9.4 No gambling framing
All monetized or tension-driving competitive structures must use safe non-cash framing:
- skills challenge
- tickets
- progression
- cosmetics
- rewards
- leagues
- events

---

# 10. AI Use Constitution

## 10.1 Claude role
Claude is used for:
- architecture planning
- system breakdown
- C++ scaffolding
- BuildGraph/UAT/Gauntlet support
- validation logic
- docs/specs
- test plan generation

## 10.2 NeoStack role
NeoStack is used for:
- in-editor implementation help
- Blueprint organization
- editor-side repetitive tasks
- arena/blockout assistance
- placement and setup help

## 10.3 AI writable zones
AI may auto-edit in approved areas such as:
- non-authoritative Blueprints
- data assets
- UI widgets
- validation scripts
- build scripts
- arena blockout branches
- import scripts
- test configs

## 10.4 Protected zones
AI must not auto-merge or auto-own:
- reward grant authority
- anti-abuse systems
- auth/session security
- hidden MMR truth
- persistence truth
- replication-critical authority logic
- release branch decisions

## 10.5 AI branch rule
AI-generated edits belong in:
- feature branches
- ai branches
- review branches
- arena experiment branches

Never direct-to-main.

---

# 11. Source Control and Promotion Law

## 11.1 Preferred structure
Unreal content should be treated as **Perforce-first**.  
Scripts, backend, and docs may also live in Git where appropriate.

## 11.2 Branch categories
```text
main
integration
release/*
feature/*
arena/*
mode/*
ai/*
```

## 11.3 Promotion ladder
```text
dev
validated
playable
candidate
release
```

## 11.4 Promotion meaning
### dev
Compiles or saves successfully.

### validated
Passes content validation and fast tests.

### playable
Passes packaged smoke tests.

### candidate
Passes end-to-end flow checks, including queue/reward loops.

### release
Manually approved after review.

---

# 12. Validation Law

## 12.1 Mandatory validation categories
Validation should fail for:
- bad naming
- wrong folder placement
- missing collision
- missing tags
- missing objective anchors
- missing broadcast anchors
- invalid Data Asset fields
- unapproved texture sizes
- missing audio event metadata
- wrong arena layer usage
- invalid reward tables
- unapproved prototype dependencies

## 12.2 No silent exceptions
If a validation rule is broken, it must either:
- fail the build
- or require an explicit approved waiver path

No “everyone knows that one is broken” culture.

---

# 13. Testing Law

## 13.1 Three-tier test model
### Tier 1 — fast editor tests
Used for:
- logic
- score rules
- tags
- data sanity
- validators
- reward table checks

### Tier 2 — packaged smoke tests
Used for:
- map load
- objective completion
- score resolution
- return-to-menu flow
- client/server packaging health

### Tier 3 — end-to-end scenario tests
Used for:
- queue to match to reward
- reconnect
- overtime
- denial payout
- AFK no-reward
- private lobby reward restrictions
- spectator join flow

## 13.2 Test naming
Tests must reveal exactly what they prove.

Bad:
```text
Test_Arena
Test_Economy
```

Good:
```text
Test_AssaultCore_ObjectiveCaptureCompletes
Test_QuickMatch_RewardGrantBlockedWhenAFK
Test_CrashSiteOmega_BroadcastAnchorsPresent
```

---

# 14. Build Automation Law

## 14.1 Required automation spine
AFL automation must be built around:
- validation
- compile
- automated tests
- package
- runtime smoke
- promotion gates

## 14.2 Minimum build graph expectations
```text
Sync
-> Validate
-> Compile
-> FastTests
-> Cook
-> Package
-> RuntimeSmoke
-> EndToEndChecks
-> PublishArtifacts
-> PromoteIfApproved
```

## 14.3 Build workers
The pipeline should plan for:
- code workers
- cook/package workers
- GPU/perf workers
- multiplayer/runtime workers

## 14.4 Shared cache law
Shared DDC/caching is mandatory for team-scale efficiency.

No long-term reliance on isolated local-only derived data.

---

# 15. Performance Constitution

## 15.1 Performance is not a late-stage chore
Every playable build should track:
- load time
- actor count
- memory growth
- frame time
- key arena visual density
- UI overhead
- effect-heavy hotspots

## 15.2 Arena performance law
No arena may be polished into a state where:
- center-lane collisions become unreadable
- FX obscure objective states
- UI becomes noisy under pressure
- camera angles fail due to clutter

---

# 16. Broadcast Constitution

## 16.1 Broadcast is a first-class citizen
AFL is a watchable robotics sport.  
Broadcast support is not optional polish.

## 16.2 Required broadcast anchors
Each arena must support:
- hero intro shot
- center-lane clash shot
- midfield overview
- objective hero shot
- aerial or high tactical sweep

## 16.3 Event callouts
Gameplay systems must emit clean broadcast events for:
- objective started
- objective denied
- overtime active
- round won
- major impact play
- match end

---

# 17. Security and Authority Law

## 17.1 Dedicated authority zones
Truth must live in the right place.

### Client should not own
- rewards
- match result truth
- rating truth
- anti-abuse state
- final score authority

### Client may own
- local presentation
- local VFX/audio triggering from approved events
- local HUD representation
- non-authoritative prediction where approved

## 17.2 Anti-abuse rules exist from day one
At minimum, AFL must be able to suppress or flag:
- AFK farming
- repeated collusion
- suspicious private-lobby reward loops
- disconnect abuse
- reward duplication

---

# 18. Definition of Ready

A feature is ready to build when:
- ownership is defined
- folder destination is defined
- naming is defined
- validation expectations are defined
- tests are identified
- mode impact is identified
- UI/broadcast impact is identified if applicable

---

# 19. Definition of Done

A feature is done only when:
- implementation is in the correct owner module
- naming is compliant
- folders are compliant
- validation passes
- required tests pass
- protected-zone review is completed where relevant
- no prototype leftovers remain
- HUD/broadcast behavior is coherent
- the feature does not break future combat-family expansion

---

# 20. Immediate Constitution Addendum for Arena 01

## Crash Site Omega must prove:
- AFL can build a readable robotics-sport arena
- Assault Core can function end-to-end
- the HUD can feel like robot telemetry, not generic shooter UI
- queue and rewards can work safely
- automation can validate and re-test the slice cleanly

## Crash Site Omega must not become:
- an overdecorated concept map
- a one-off mode architecture trap
- a generic shooter reskin
- a UI style deviation from the robotics command-center identity

---

# 21. Final Standing Order

Every contributor, tool, agent, and builder working on AFL should operate under one constant question:

**Does this make AFL more robotic, more readable, more playable, more watchable, or more scalable?**

If the answer is no, it should not enter the build.
