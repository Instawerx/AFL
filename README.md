# AFL Phase 8 — State Sync Engine + Match Authority

This pack upgrades AFL from a local network session scaffold into an **authoritative state sync layer**.

It adds:

- authoritative match server
- state tick broadcaster
- client action validator
- client state sync simulator
- authority result emitter
- PowerShell runners
- CI workflow for state sync smoke checks

## What this pack does

This pack can:

- start an authoritative local session server
- maintain a match state model
- accept player actions
- validate allowed actions
- advance the match through server ticks
- broadcast state snapshots to clients
- emit authoritative match result artifacts

## What this pack does not claim

This pack does not provide:
- production Unreal replication
- production anti-cheat
- internet-scale networking
- full rollback netcode
- production persistence

It is the correct next layer after Phase 7 so AFL can move from connected sessions into **authoritative server-driven match state**.
