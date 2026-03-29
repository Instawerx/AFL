# AFL Phase 5 — Live Unreal Hook + Match Playback Loop

This pack upgrades AFL from hybrid telemetry into a **live Unreal hook + playback loop**.

It adds:

- a live file watcher for Unreal-emitted event logs
- a playback runner for recorded match event streams
- a unified live hook controller
- replay-ready artifact generation
- a simple event timeline builder
- PowerShell runners for live hook and playback mode
- CI workflow for playback validation

This is still demo-safe:
- no real robots
- no live arena
- no real money
- no production EOS requirement

It is the correct bridge between:
- Unreal gameplay events
- AFL runtime ingestion
- official result/reward generation
- later live network transport
