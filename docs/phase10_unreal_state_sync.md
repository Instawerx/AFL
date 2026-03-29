# AFL Phase 10 — Unreal Real-Time State Sync

## Purpose

Introduce a local state packet broadcaster that mirrors authoritative AFL state into a format Unreal can consume.

## Transport

- UDP for local demo speed and simplicity

## Outputs

- overlay_payload.json
- state_packet_seed.json
- spectator_packets.json

## Why this matters

This is the first AFL layer that turns server authority into a visual/broadcast-friendly stream for an investor-readable Unreal demo.
