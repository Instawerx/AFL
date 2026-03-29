# Performance Budget Checks

## Purpose
Catch regressions before visual polish hides them.

## Minimum tracked metrics
- map load time
- frame time in arena hotspot
- memory growth after one match
- actor count in Crash Site Omega
- draw call trend where available
- log completeness

## Procedure
1. Capture baseline from first playable build.
2. Compare each new build against baseline or prior candidate.
3. Flag regressions above agreed thresholds.
4. Attach logs and screenshots.

## Validation
- performance report is generated every candidate build
- regressions are visible to orchestrator before promotion
