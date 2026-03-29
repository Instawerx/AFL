from __future__ import annotations

from typing import Any

REQUIRED_EVENT_KEYS = {
    "event_type",
    "timestamp",
    "match_id",
    "player_id",
    "team",
    "arena",
    "mode",
}

ALLOWED_EVENT_TYPES = {
    "objective_entered",
    "capture_started",
    "capture_completed",
    "capture_denied",
    "damage_event",
    "disconnect",
    "match_end",
    "overtime_started",
}


def validate_event(event: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    missing = REQUIRED_EVENT_KEYS - set(event.keys())
    if missing:
        problems.append(f"Missing event fields: {', '.join(sorted(missing))}")

    event_type = event.get("event_type")
    if event_type not in ALLOWED_EVENT_TYPES:
        problems.append(f"Invalid event_type: {event_type}")

    for key in ("event_type", "timestamp", "match_id", "player_id", "team", "arena", "mode"):
        if key in event and not isinstance(event[key], str):
            problems.append(f"{key} must be a string")

    return problems
