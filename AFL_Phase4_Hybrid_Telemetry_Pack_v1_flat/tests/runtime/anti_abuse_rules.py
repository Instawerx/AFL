from __future__ import annotations

from typing import Any


def evaluate_abuse(result_payload: dict[str, Any]) -> list[str]:
    problems: list[str] = []

    if result_payload.get("session_type") in ("PrivateLobby", "InternalTest"):
        problems.append("non_competitive_session")

    if result_payload.get("disconnect_count", 0) > 0 and not result_payload.get("allow_disconnect_rewards", False):
        problems.append("disconnect_invalidates_rewards")

    if result_payload.get("players_count", 0) < 2:
        problems.append("not_enough_players")

    return problems
