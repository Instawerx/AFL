from __future__ import annotations

from typing import Any

def build_overlay_payload(state_payload: dict[str, Any]) -> dict[str, Any]:
    players = state_payload.get("players", {})
    leader = None
    if players:
        leader = sorted(players.keys())[0]

    return {
        "overlay_type": "spectator_summary",
        "match_id": state_payload.get("match_id"),
        "session_id": state_payload.get("session_id"),
        "state": state_payload.get("state"),
        "tick": state_payload.get("tick"),
        "winner": state_payload.get("winner"),
        "player_count": len(players),
        "featured_player": leader,
    }
