# AFL Phase 9 — Persistence + Replay Index

## Purpose

Persist authoritative AFL session outputs and build a replay index over them.

## Included pieces

- persistence store
- replay indexer
- history query utility

## Outputs

- data/afl/session_history.json
- data/afl/replay_index.json
- data/afl/sessions/*.json
- data/afl/archive/*.json

## Why this matters

This is the first AFL layer where sessions survive beyond a single runtime execution and can be queried and replay-indexed later.
