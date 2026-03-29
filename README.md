# AFL Phase 10 — Unreal Real-Time State Sync + Spectator Broadcast Layer

This pack upgrades AFL from persistence/replay into a **visual investor-demo layer**.

It adds:

- a local UDP state broadcaster
- a spectator event overlay generator
- a state packet schema
- a spectator simulator
- PowerShell runners
- Unreal-facing integration docs
- CI workflow for broadcast smoke tests

## What this pack does

This pack can:

- stream authoritative state snapshots over UDP
- generate overlay-ready event payloads
- simulate a spectator client consuming the stream
- emit broadcast artifacts for HUD / overlay / replay systems

## What this pack does not claim

This pack does not provide:
- finished Unreal Blueprint integration
- production-quality net serialization
- final broadcast graphics package
- cloud relay infrastructure

It is the correct next layer for a gameplay-first, investor-readable AFL demo.
