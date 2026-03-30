# Phase 16 — Level Bootflow

## Demo Map
- `CrashSiteOmega_Demo`

## BeginPlay Order
1. Level loads
2. Spawn `BP_AFL_RuntimeBridge`
3. Load `BP_AFL_SpectatorController`
4. Spectator controller creates widgets
5. Runtime bridge starts polling JSON
6. Runtime bridge dispatches widget + camera state
7. Demo loop begins
