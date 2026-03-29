# AFL Phase 6 — Multiplayer Orchestrator + Real Match Sessions

This pack upgrades AFL from live event playback into a local multiplayer orchestration layer.

It adds:

- session registry
- lobby simulator
- multiplayer match coordinator
- session-backed orchestrator
- PowerShell runners
- sample multiplayer scenarios
- CI workflow for multiplayer simulation

## What this pack does

This pack can:

- create deterministic session IDs
- assemble players into lobbies
- validate minimum player count
- start a simulated multiplayer match session
- emit session, match, and reward artifacts
- support repeatable local end-to-end session testing

## What this pack does not claim

This pack does not provide:
- real dedicated network replication
- production EOS matchmaking
- production persistence
- anti-cheat
- live robot control

It is the correct next layer after Phase 5 so AFL can test session-backed multiplayer flows locally.
