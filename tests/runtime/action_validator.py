from __future__ import annotations

from typing import Any


ALLOWED_ACTIONS = {
    "join",
    "ready",
    "objective_enter",
    "capture_start",
    "capture_complete",
    "heartbeat",
}


def validate_action(payload: dict[str, Any]) -> list[str]:
    problems: list[str] = []

    action_type = payload.get("type")
    if action_type not in ALLOWED_ACTIONS:
        problems.append(f"invalid_action_type:{action_type}")

    if "player_id" not in payload or not isinstance(payload.get("player_id"), str):
        problems.append("missing_or_invalid_player_id")

    return problems
