Crash Site Omega — Arena Gameplay Logic Board v1
Purpose

This document codifies the Assault Core ruleset for Crash Site Omega. It ensures that the mode is simple to understand, exciting to play and compelling to watch. Use this as a blueprint when implementing scoring, match flow, HUD elements and automated tests.

1. Design Intent

Crash Site Omega should feel like a televised robotic assault sport: robots advance through lanes, collide in midfield, contest an uplink tower and either score or deny at the last second. The rules are straightforward, emphasising aggression and readable momentum swings.

2. Sport Loop
Deploy → Advance → Collide → Contest Space → Control Approach → Press Objective → Score or Deny → Reset

This sequence repeats until the round timer expires. Every mechanic should reinforce these phases.

3. Match Structure
Three rounds per match.
Three‑minute rounds with a 30‑second pre‑round intro.
15‑second reset between rounds.
Best two of three wins the match.
4. Win Condition

Win a round by either:

Completing a full capture of the Uplink Tower (primary objective), or
Having the higher score when the timer expires.

Win the match by winning two rounds.

5. Primary Scoring
Objective Capture (Full Uplink completion) – 100 points.
Capture requires holding the objective uncontested for 10 seconds. During hold, defenders can contest to halt progress.
6. Support Scoring Events
Event	Points	Description
Objective Entry / Pressure Touch	5	Awarded when a robot enters the objective zone and begins pressure.
Objective Hold Tick (every 2 seconds)	3	Given while holding the objective uncontested.
Midfield Control Win	10	Optional: for teams that win a midfield checkpoint (if used).
Objective Denial Bonus	5	Awarded to defenders who break an active capture attempt.
Impact / Tackle Play (optional)	5	Reward high‑impact plays that meaningfully disrupt an enemy.

Support scoring ensures the scoreboard moves even during failed captures, encouraging constant pressure and denial.

7. Scoreboard Model

The scoreboard should clearly display:

Team scores.
Primary capture progress (percentage and countdown).
Round timer.
Round number and match series (e.g., Round 1 / Best of 3).
Overtime status if active.

Support points should be visible but should never eclipse the significance of a full capture.

8. Round Flow

Phase 1 – Deployment (0–10s)

Robots launch from deployment bays. Teams decide lane splits and position for the first clash.

Phase 2 – Midfield Clash (10–40s)

First collisions and tackle plays occur in the midfield wreck zone. Teams vie for map control and setup.

Phase 3 – Objective Pressure (40–120s)

Teams push toward the objective. Initial capture attempts happen. Denials generate drama.

Phase 4 – Late Round Tension (120–180s)

Urgent pushes, desperate defences and scoreboard awareness dominate. Overtime often triggers here.

The flow resets each round but should always be readable for both players and spectators.

9. Overtime System

Live Contest Overtime: if the objective is actively contested when the timer hits zero, the round continues until the contest resolves (capture or denial). This rule generates dramatic finishes and prevents anticlimactic endings.

10. Denial and Defence

Defending is about breaking pressure, not hiding. Denial bonuses reward players who clear the objective zone or reset capture progress. Defensive players should be encouraged to engage and disrupt rather than turtle.

11. Spawn and Respawn Rules
Teams respawn in their deployment bays.
Respawn timer: 6 seconds (subject to tuning).
Spawn zones feature short protected tunnels to prevent spawn camping.
Players must re‑enter the fight quickly but cannot instantly reappear in the objective.
12. Anti‑Stall Mechanics

Stalling is discouraged through:

Primary capture being the largest score event.
Support scoring rewarding forward movement and denial.
Overtime punishing teams who refuse to contest late pushes.
Arena geometry encouraging forward pressure and limited safe hiding spots.
13. Player Roles

Even without formal classes, Crash Site Omega naturally supports different playstyles:

Pusher – goes through the centre lane and pressures the objective.
Flanker – uses side lanes to reposition, disrupt and create crossfire.
Disruptor – focuses on tackles, knockbacks and denial plays.
Anchor – holds space, zones out opponents and supports pressure.

The scoring system should accommodate and reward each role appropriately.

14. Hallmarks of a Good AFL Moment

Great AFL highlights look like:

A last‑second denial with the objective at 98% capture.
A well‑timed tackle clearing the objective and forcing overtime.
A coordinated flank that breaks a strong defence.
A heroic push that completes a capture after sustained midfield control.
A clutch defensive stand that swings the match.

Systems (scoring, HUD, broadcast) should capture and celebrate these moments.

15. HUD and Broadcast Guidance
Display the round timer, team scores, capture progress and overtime clearly at all times.
Use telemetry panels to show robot vitals, stamina and weapon readiness.
Highlight contest status (contested, capturing, denied) with clear visuals and sound.
Overtime should have unique visual treatment and audio cues.
Denial bonuses and impact plays should generate on‑screen callouts and feed into replay systems.

Implementing this logic board will produce a mode that feels fair, dynamic and watchable, laying the groundwork for a compelling esports experience.
