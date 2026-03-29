# AFL Phase 7 — Network Layer + Live Player Connections

This pack upgrades AFL from local multiplayer orchestration into a **real-time network session scaffold**.

It adds:

- a lightweight TCP session server
- a live client connector for local players/bots
- match state sync scaffolding
- session event broadcast loop
- PowerShell runners for server and clients
- sample network scenarios
- CI workflow for local network smoke checks

## What this pack does

This pack can:

- start a local TCP session server
- accept multiple client connections
- process simple join / ready / state messages
- broadcast session state to all connected clients
- generate network session artifacts for AFL runtime validation

## What this pack does not claim

This pack does not provide:
- production-grade netcode
- finished Unreal replication
- production EOS transport
- anti-cheat
- internet-hosted matchmaking

It is the correct next layer so AFL can move from simulated multiplayer into **live local connected sessions**.
