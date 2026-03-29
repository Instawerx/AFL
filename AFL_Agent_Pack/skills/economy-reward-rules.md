# Economy Reward Rules

## Purpose
Grant Coins, Tickets, and XP consistently and safely.

## Rules
- rewards are server-authoritative
- private and internal tests do not receive full competitive payouts
- AFK participants fail payout thresholds
- duplicate grant protection is mandatory

## Required event inputs
- session class
- match completion state
- round results
- objective participation
- denial events
- AFK flags

## Procedure
1. Load payout table for session class.
2. Verify match completion.
3. Apply anti-abuse filters.
4. Grant Coins/Tickets/XP atomically.
5. Emit audit log.

## Validation
- repeated grant attempt is rejected
- payout table contains required fields
- missing audit log is treated as failure
