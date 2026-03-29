# AFL Phase 2.5 Real Runtime

## Purpose

Upgrade AFL from dry-run harnesses into a local executable runtime scaffold.

## Runtime Modes

- real_exe: launches the configured AFL_SERVER_EXE
- stub_server: launches the included Python stub server when no real executable is configured

## Why stub mode exists

Stub mode is intentional. It keeps the repo executable on any machine while the real Unreal dedicated server path is still being wired.

## Next upgrade target

Replace the simulated queue/session/match result code in orchestrator.py with:
- real dedicated server bring-up
- real session creation hooks
- real match result ingestion
- real reward service writes in a non-production environment
