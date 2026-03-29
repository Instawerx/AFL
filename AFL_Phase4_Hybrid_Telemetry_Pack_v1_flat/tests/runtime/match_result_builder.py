from __future__ import annotations

import argparse
import json
from pathlib import Path
from collections import Counter

from file_event_adapter import read_events
from event_schema import validate_event


def build_result(events: list[dict]) -> dict:
    problems = []
    for idx, event in enumerate(events):
        errs = validate_event(event)
        for err in errs:
            problems.append(f"event[{idx}]: {err}")

    if problems:
        raise SystemExit("\n".join(problems))

    first = events[0]
    captures = [e for e in events if e["event_type"] == "capture_completed"]
    denials = [e for e in events if e["event_type"] == "capture_denied"]
    disconnects = [e for e in events if e["event_type"] == "disconnect"]
    overtimes = [e for e in events if e["event_type"] == "overtime_started"]

    winner = captures[-1]["player_id"] if captures else first["player_id"]

    team_counts = Counter(e["team"] for e in events if e["event_type"] == "capture_completed")

    return {
        "match_id": first["match_id"],
        "arena": first["arena"],
        "mode": first["mode"],
        "session_type": first.get("session_type", "PublicCompetitive"),
        "winner": winner,
        "session_valid": True,
        "players_count": len({e["player_id"] for e in events}),
        "disconnect_count": len(disconnects),
        "objective_events": events,
        "captures_completed": len(captures),
        "denials": len(denials),
        "overtime": len(overtimes) > 0,
        "coins_awarded": 100 if captures else 25,
        "xp_awarded": 250 if captures else 75,
        "team_capture_counts": dict(team_counts),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-file", required=True)
    args = parser.parse_args()

    event_file = Path(args.event_file)
    events = read_events(event_file)
    result = build_result(events)

    out_dir = Path("artifacts/runtime")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "match_result.json"
    out_file.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Match result built: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
