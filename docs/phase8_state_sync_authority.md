# AFL Phase 8 — State Sync Engine + Match Authority

## Purpose

Introduce an authoritative server state model for AFL.

## Included pieces

- authoritative match server
- action validator
- client state sync simulator
- authority result emitter

## Outputs

- authoritative_state_snapshot.json
- authoritative_match_result.json
- authoritative_reward_result.json

## Why this matters

This is the first AFL layer where the server becomes the source of truth for match state, winner resolution, and reward emission.
