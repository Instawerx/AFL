# AFL Phase 4 Event Contract

## Active transport

Phase 4 uses file-based event output as the active integration path.

## Future transport

The same schema is intended to move to socket transport later.

## Required event fields

- event_type
- timestamp
- match_id
- player_id
- team
- arena
- mode

## Allowed event types

- objective_entered
- capture_started
- capture_completed
- capture_denied
- damage_event
- disconnect
- match_end
- overtime_started
