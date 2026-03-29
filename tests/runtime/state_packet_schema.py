from __future__ import annotations

from typing import Any

REQUIRED_PACKET_KEYS = {
    "packet_type",
    "match_id",
    "session_id",
    "tick",
    "state",
    "players",
}

def validate_state_packet(packet: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    missing = REQUIRED_PACKET_KEYS - set(packet.keys())
    if missing:
        problems.append(f"Missing packet fields: {', '.join(sorted(missing))}")
    if packet.get("packet_type") != "state_snapshot":
        problems.append(f"Invalid packet_type: {packet.get('packet_type')}")
    if "tick" in packet and not isinstance(packet["tick"], int):
        problems.append("tick must be int")
    if "players" in packet and not isinstance(packet["players"], dict):
        problems.append("players must be an object/map")
    return problems
