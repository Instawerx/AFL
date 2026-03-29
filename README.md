# AFL Phase 9 — Persistence Layer + Session History + Replay Index

This pack upgrades AFL from authoritative match state into a local persistence and replay index layer.

It adds:

- persistent session store
- persistent match store
- replay index builder
- artifact archive writer
- history query utility
- PowerShell runners
- CI workflow for persistence checks

## What this pack does

This pack can:

- save authoritative session artifacts into a local data store
- archive match results and reward results
- build a replay index from stored sessions
- query recent sessions and matches
- persist local history across repeated runs

## What this pack does not claim

This pack does not provide:
- production database replication
- cloud object storage
- large-scale analytics
- full replay rendering
- production identity linkage

It is the correct next layer after Phase 8 so AFL can move from authoritative runtime outputs into **persistent session history and replayable artifact management**.
