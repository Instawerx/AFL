from __future__ import annotations

from typing import Any


def build_scoreboard_packet(state: dict[str, Any]) -> dict[str, Any]:
    players = state.get("players", {})
    team_a = [p for p in players.values() if p.get("team") == "A"]
    team_b = [p for p in players.values() if p.get("team") == "B"]

    return {
        "overlay_type": "scoreboard",
        "match_id": state.get("match_id"),
        "session_id": state.get("session_id"),
        "state": state.get("state"),
        "tick": state.get("tick", 0),
        "winner": state.get("winner"),
        "team_a_players": [p.get("player_id") for p in team_a],
        "team_b_players": [p.get("player_id") for p in team_b],
        "team_a_objective_control": sum(int(p.get("objective_control", 0)) for p in team_a),
        "team_b_objective_control": sum(int(p.get("objective_control", 0)) for p in team_b),
    }
