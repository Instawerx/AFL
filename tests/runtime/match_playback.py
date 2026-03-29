from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

from file_event_adapter import read_events
from match_result_builder import build_result
from reward_engine import calculate_rewards


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL recorded match playback")
    parser.add_argument("--event-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--speed", type=float, default=1.0)
    args = parser.parse_args()

    event_file = Path(args.event_file)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    events = read_events(event_file)
    playback = []
    for idx, event in enumerate(events):
        playback.append({
            "index": idx,
            "event_type": event["event_type"],
            "player_id": event["player_id"],
            "team": event["team"],
            "timestamp": event["timestamp"],
        })
        time.sleep(0.01 / max(args.speed, 0.1))

    result = build_result(events)
    rewards = calculate_rewards(result)

    (output_dir / "playback_timeline.json").write_text(json.dumps(playback, indent=2), encoding="utf-8")
    (output_dir / "playback_match_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (output_dir / "playback_reward_result.json").write_text(json.dumps(rewards, indent=2), encoding="utf-8")

    print(f"Playback completed: {event_file}")
    print(f"Timeline entries: {len(playback)}")
    return 0
