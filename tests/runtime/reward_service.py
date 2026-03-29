from __future__ import annotations

from typing import Any


def calculate_rewards(session_type: str, result_payload: dict[str, Any]) -> dict[str, int]:
    if session_type in ("PrivateLobby", "InternalTest", "SpectatorOnly"):
        return {"coins_awarded": 0, "xp_awarded": 0}

    base_coins = int(result_payload.get("coins_awarded", 0))
    base_xp = int(result_payload.get("xp_awarded", 0))

    if not result_payload.get("session_valid", False):
        return {"coins_awarded": 0, "xp_awarded": 0}

    return {"coins_awarded": base_coins, "xp_awarded": base_xp}
