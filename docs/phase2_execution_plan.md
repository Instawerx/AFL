# AFL Phase 2 Execution Plan

## Goal

Move AFL from validated repo structure into repeatable execution scaffolds.

## Scope

This phase adds:
- Unreal BuildGraph invocation wrapper
- EOS environment preflight
- Queue to reward dry-run harness
- CI entrypoint for runtime checks

## Out of Scope

This phase does not claim to:
- ship a full playable Unreal dedicated server
- provision real EOS credentials
- validate real network matchmaking
- issue real economy writes to production services

## Success Criteria

- Runtime scripts exist in repo root
- EOS preflight can fail clearly on missing config
- Queue-reward harness can validate a scenario file and emit result JSON
- GitHub Actions can run the harness on push or dispatch
