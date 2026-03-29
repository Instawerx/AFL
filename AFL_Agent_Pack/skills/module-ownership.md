# Module Ownership

## Purpose
Stop feature sprawl by assigning one home for every system.

## Rules
- Shared robot state lives in AFLCore.
- Shared combat vocabulary lives in AFLCombatCore.
- Tackle/knockback logic lives in AFLCombatMelee.
- Hitscan lives in AFLCombatHitscan.
- Projectile and splat logic live in AFLCombatProjectile.
- Arena match state lives in AFLArena.
- Assault-only rules live in AFLModeAssault.
- Queue/lobby/session logic lives in AFLMatchmaking.
- Coins/Tickets/XP live in AFLEconomy and AFLProgression.
- Spectator and overlays live in AFLBroadcast and AFLUI.

## Procedure
1. For a proposed feature, identify whether it is shared or mode-specific.
2. Map it to one owner module.
3. List any interfaces it consumes from other modules.
4. Reject the task if it attempts to bypass the owner module.

## Deliverables
- owner module
- interface list
- touched paths

## Validation
- no duplicated shared logic in a mode module
- no UI authority logic in economy or matchmaking
