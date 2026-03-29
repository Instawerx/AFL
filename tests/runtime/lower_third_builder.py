from __future__ import annotations

from typing import Any


def build_lower_thirds(state: dict[str, Any]) -> list[dict[str, Any]]:
    players = state.get("players", {})
    cards = []
    for player_id, payload in players.items():
        cards.append(
            {
                "overlay_type": "player_lower_third",
                "player_id": player_id,
                "team": payload.get("team"),
                "ready": payload.get("ready"),
                "connected": payload.get("connected"),
                "objective_control": payload.get("objective_control", 0),
            }
        )
    return cards
