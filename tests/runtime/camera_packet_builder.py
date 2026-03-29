from __future__ import annotations

from typing import Any


def build_camera_packets(state: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "camera_id": "hero_wide",
            "mode": "wide",
            "target": state.get("winner") or "center_objective",
            "priority": 1,
        },
        {
            "camera_id": "objective_focus",
            "mode": "objective",
            "target": "center_objective",
            "priority": 2,
        },
        {
            "camera_id": "winner_follow",
            "mode": "follow",
            "target": state.get("winner"),
            "priority": 3,
        },
    ]
