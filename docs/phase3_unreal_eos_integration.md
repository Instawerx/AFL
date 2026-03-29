# AFL Phase 3 Unreal + EOS Integration

## Purpose

Introduce the first Unreal + EOS integration boundary for AFL runtime automation.

## Included layers

- Unreal server adapter
- EOS smoke adapter
- session model
- result contract validator
- reward service boundary
- CI workflow

## Immediate goals

- validate EOS config presence
- validate session result shape
- isolate reward logic from harness logic
- prepare for real local Unreal process integration

## Next step after this pack

Replace EOS config-validation smoke with real:
- session creation
- join flow
- reconnect handling
- result ingestion from Unreal runtime
