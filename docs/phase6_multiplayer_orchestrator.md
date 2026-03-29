# AFL Phase 6 — Multiplayer Orchestrator

## Purpose

Introduce a real session-backed local multiplayer orchestration layer.

## Included pieces

- session registry
- lobby readiness simulation
- multiplayer match coordinator
- session-backed artifact generation

## Outputs

- multiplayer_session.json
- multiplayer_match_result.json
- multiplayer_reward_result.json

## Why this matters

This is the first AFL layer where match IDs, sessions, and player grouping become explicit runtime artifacts.
