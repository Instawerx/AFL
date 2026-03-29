# Cargo Import Rules

## Purpose
Standardize KitBash Cargo asset intake.

## Rules
- import macro landmarks before clutter
- place assets in arena-specific folders
- assign collision policy on import
- apply Nanite or LOD rules consistently
- tag props by role: landmark, blocker, dressing, broadcast

## Procedure
1. Import to `Content/Arenas/<ArenaName>/Props/`.
2. Rename to AFL conventions.
3. Apply collision profile.
4. Record source pack and intended role.
5. Reject imports with missing material references.

## Validation
- no raw download names remain
- hero props are not imported into prototype folders
