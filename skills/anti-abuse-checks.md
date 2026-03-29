# Anti-Abuse Checks

## Purpose
Reduce exploitable reward behavior early.

## Minimum checks
- AFK detection
- suspicious repeated pairing
- disconnect loops near reward trigger
- impossible stat bursts
- duplicate payout attempts
- private-lobby farming

## Procedure
1. Define signals from gameplay and session logs.
2. Assign low/medium/high severity.
3. Gate payouts on high severity.
4. Persist flags for later review.

## Validation
- each check has a deterministic trigger definition
- reward flow can consume the check results
