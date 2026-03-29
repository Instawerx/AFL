from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

from file_event_adapter import read_events
from match_result_builder import build_result
from reward_engine import calculate_rewards


def process_event_file(event_file: Path, output_dir: Path) -> dict:
    events = read_events(event_file)
    result = build_result(events)
    rewards = calculate_rewards(result)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "live_match_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (output_dir / "live_reward_result.json").write_text(json.dumps(rewards, indent=2), encoding="utf-8")
    timeline = [
        {"index": i, "event_type": e["event_type"], "player_id": e["player_id"], "timestamp": e["timestamp"]}
        for i, e in enumerate(events)
    ]
    (output_dir / "live_event_timeline.json").write_text(json.dumps(timeline, indent=2), encoding="utf-8")
    return {"result": result, "rewards": rewards, "timeline_count": len(timeline)}


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL live Unreal file hook")
    parser.add_argument("--watch-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--poll-seconds", type=float, default=1.0)
    parser.add_argument("--once", action="store_true", default=True)
    args = parser.parse_args()

    watch_dir = Path(args.watch_dir)
    output_dir = Path(args.output_dir)
    watch_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    processed: set[str] = set()

    while True:
        found = False
        for event_file in sorted(watch_dir.glob("*.json")):
            if str(event_file) in processed:
                continue
            found = True
            summary = process_event_file(event_file, output_dir)
            print(f"Processed live event file: {event_file}")
            print(json.dumps(summary, indent=2))
            processed.add(str(event_file))
        if args.once and found:
            return 0
        time.sleep(args.poll_seconds)
