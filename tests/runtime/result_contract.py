from __future__ import annotations

from typing import Any


REQUIRED_RESULT_KEYS = {
    "winner",
    "coins_awarded",
    "xp_awarded",
    "session_valid",
    "objective_events",
}


def validate_result_contract(payload: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    missing = REQUIRED_RESULT_KEYS - set(payload.keys())
    if missing:
        problems.append(f"Missing result fields: {', '.join(sorted(missing))}")

    if "objective_events" in payload and not isinstance(payload["objective_events"], list):
        problems.append("objective_events must be a list")

    if "session_valid" in payload and not isinstance(payload["session_valid"], bool):
        problems.append("session_valid must be a boolean")

    for key in ("coins_awarded", "xp_awarded"):
        if key in payload and not isinstance(payload[key], int):
            problems.append(f"{key} must be an int")

    return problems
