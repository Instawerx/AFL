from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)

from file_event_adapter import write_events
from socket_event_adapter import get_socket_stub_description


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_events_from_scenario(data: dict) -> list[dict]:
    players = data["players"]
    arena = data["arena"]
    mode = data["mode"]
    session_type = data["session_type"]
    match_id = data.get("match_id", "match_demo_001")

    events = [
        {
            "event_type": "objective_entered",
            "timestamp": now_iso(),
            "match_id": match_id,
            "player_id": players[0],
            "team": "A",
            "arena": arena,
            "mode": mode,
            "session_type": session_type,
        },
        {
            "event_type": "capture_started",
            "timestamp": now_iso(),
            "match_id": match_id,
            "player_id": players[0],
            "team": "A",
            "arena": arena,
            "mode": mode,
            "session_type": session_type,
        },
    ]

    if data.get("simulation", {}).get("overtime", False):
        events.append(
            {
                "event_type": "overtime_started",
                "timestamp": now_iso(),
                "match_id": match_id,
                "player_id": players[0],
                "team": "A",
                "arena": arena,
                "mode": mode,
                "session_type": session_type,
            }
        )

    if data.get("simulation", {}).get("disconnect_player"):
        events.append(
            {
                "event_type": "disconnect",
                "timestamp": now_iso(),
                "match_id": match_id,
                "player_id": data["simulation"]["disconnect_player"],
                "team": "B",
                "arena": arena,
                "mode": mode,
                "session_type": session_type,
            }
        )

    if data.get("expected", {}).get("winner"):
        winner = data["expected"]["winner"]
        team = "A" if winner == players[0] else "B"
        events.append(
            {
                "event_type": "capture_completed",
                "timestamp": now_iso(),
                "match_id": match_id,
                "player_id": winner,
                "team": team,
                "arena": arena,
                "mode": mode,
                "session_type": session_type,
            }
        )

    events.append(
        {
            "event_type": "match_end",
            "timestamp": now_iso(),
            "match_id": match_id,
            "player_id": data["expected"]["winner"],
            "team": "A",
            "arena": arena,
            "mode": mode,
            "session_type": session_type,
        }
    )

    return events


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["file", "socket"], default="file")
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    scenario_path = Path(args.scenario)
    data = yaml.safe_load(scenario_path.read_text(encoding="utf-8"))

    if args.mode == "socket":
        print(get_socket_stub_description())
        return 0

    events = build_events_from_scenario(data)
    out_file = Path("artifacts/runtime/match_events.json")
    write_events(out_file, events)
    print(f"Telemetry events written: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
