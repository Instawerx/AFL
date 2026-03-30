# AFL Phase 14 — Lyra Demo Map Wiring

## Purpose

Define the startup and binding flow for a single AFL demo map inside Unreal.

## Startup sequence

- spawn runtime bridge actor
- spawn spectator controller
- load widget binding map
- load camera binding manifest
- start JSON polling
- apply scene playback manifest

## Next upgrade target

- Blueprint class implementation
- UMG widget construction
- in-engine Sequencer binding
- live runtime polling inside Unreal
