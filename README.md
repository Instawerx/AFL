# AFL Phase 11 — HUD / Broadcast Overlay Pack

This pack upgrades AFL from raw broadcast/state output into a **watchable spectator overlay layer**.

It adds:

- scoreboard packet builder
- lower-third / player card payload builder
- announcer event feed builder
- match director state controller
- camera packet scaffold
- PowerShell runners for overlay generation
- CI workflow for overlay smoke checks

## What this pack does

This pack can:

- turn authoritative/broadcast state into HUD-ready JSON
- generate overlay packets for scoreboard, player cards, and event callouts
- build a simple match director state file
- emit camera packet scaffolds for future Unreal consumption
- provide investor/demo-facing broadcast artifacts

## What this pack does not claim

This pack does not provide:
- final Unreal UMG widgets
- production broadcast graphics
- live replay compositor
- final commentary AI
- final camera automation logic

It is the correct next layer to make AFL visually legible and pitch-ready.
