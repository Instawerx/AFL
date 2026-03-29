from __future__ import annotations

import argparse
import json
from pathlib import Path

from announcer_feed_builder import build_announcer_feed
from camera_packet_builder import build_camera_packets
from lower_third_builder import build_lower_thirds
from scoreboard_packet_builder import build_scoreboard_packet


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL broadcast overlay builder")
    parser.add_argument("--state-file", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    state = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    scoreboard = build_scoreboard_packet(state)
    lower_thirds = build_lower_thirds(state)
    announcer_feed = build_announcer_feed(state)
    camera_packets = build_camera_packets(state)

    (output_dir / "scoreboard_packet.json").write_text(json.dumps(scoreboard, indent=2), encoding="utf-8")
    (output_dir / "lower_thirds.json").write_text(json.dumps(lower_thirds, indent=2), encoding="utf-8")
    (output_dir / "announcer_feed.json").write_text(json.dumps(announcer_feed, indent=2), encoding="utf-8")
    (output_dir / "camera_packets.json").write_text(json.dumps(camera_packets, indent=2), encoding="utf-8")

    print(f"Broadcast overlay artifacts written to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
