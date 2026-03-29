# Lyra Prune

## Purpose
Retain Lyra systems that help AFL, and remove only sample bloat.

## Keep
- Enhanced Input mappings that can be remapped for robots
- Gameplay Ability System foundations
- Equipment/weapon patterns that can be reused for hitscan/projectile families
- Multiplayer-safe state ownership patterns
- Experience loading only if it remains decoupled from sample identity

## Remove or isolate
- Sample maps and sample cosmetic content
- Unused demo UI flows
- Sample character identity assets
- Dead game feature plugins not needed by AFL

## Procedure
1. Inventory all Lyra plugins, maps, sample assets, and game feature dependencies.
2. Mark each item as keep, isolate, or remove.
3. Verify that removal does not break combat family extensibility.
4. Replace sample-facing names with AFL-neutral abstractions.
5. Capture a prune report listing every removal and every preserved system.

## Deliverables
- prune report
- keep/remove matrix
- list of replaced references

## Validation
- project still opens
- preserved modules compile
- input mappings remain usable
- no sample map is referenced by production code
