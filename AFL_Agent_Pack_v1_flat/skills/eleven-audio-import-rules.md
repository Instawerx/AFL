# Eleven Audio Import Rules

## Purpose
Bring generated VO and announcer assets into AFL without chaos.

## Categories
- announcer
- objective
- overtime
- victory
- robot-status
- tutorial

## Procedure
1. Normalize filenames with event-first naming.
2. Import to `Content/Audio/Events/<Category>/`.
3. Create cue or MetaSound wrapper if required.
4. Map the event id in a routing table.
5. Reject clips with missing category or event id.

## Validation
- filename includes category and event key
- event routing table contains every imported clip
- no clip is left orphaned in raw import folders
