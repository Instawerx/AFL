# Gauntlet Smoke Tests

## Purpose
Prove packaged AFL builds can perform the core queue-to-match-to-reward loop.

## Minimum scenarios
1. Launch client and server.
2. Load Crash Site Omega.
3. Start Assault Core.
4. Complete one objective cycle.
5. Resolve round end.
6. Exit to menu.

## Expanded scenarios
- private lobby join
- reconnect after disconnect
- no reward for AFK
- overtime contest resolution

## Procedure
1. Keep each scenario short and deterministic.
2. Log expected milestones.
3. Fail on missing milestones, crashes, or hangs.
4. Archive logs and screenshots on failure.

## Validation
- each scenario has a pass/fail signal
- failures preserve artifacts
