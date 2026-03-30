# AFL Phase 14 — Unreal Runtime Integration Pack

This pack upgrades AFL from Unreal-facing demo payloads into a **runtime integration blueprint layer**.

It adds:

- Unreal Blueprint binding contracts
- UMG widget data bridge descriptors
- Sequencer/camera binding manifest
- Lyra-compatible demo map wiring plan
- runtime JSON polling bridge
- PowerShell runners
- seed integration data
- CI workflow for runtime integration smoke checks

## What this pack does

This pack can:

- assemble Unreal-ready runtime bridge artifacts
- define widget binding maps for scoreboard, lower-thirds, announcer, and phase widgets
- define camera binding manifests for Sequencer/Blueprint usage
- emit a demo map runtime manifest for a single AFL arena flow
- provide a clean implementation contract for Lyra-compatible Unreal integration

## What this pack does not claim

This pack does not provide:
- compiled Unreal Blueprints
- final UMG art assets
- final in-engine code plugin
- production multiplayer replication inside Unreal

It is the correct next layer to move AFL from external runtime simulation into actual Unreal implementation guidance and runtime bridge artifacts.
