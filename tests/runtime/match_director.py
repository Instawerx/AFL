from __future__ import annotations

import argparse
import json
from pathlib import Path

from camera_packet_builder import build_camera_packets


def build_director_state(state: dict) -> dict:
    phase = "pregame"
    if state.get("state") == "match_live":
        phase = "live"
    elif state.get("state") == "completed":
        phase = "postgame"

    return {
        "director_mode": "broadcast_demo",
        "phase": phase,
        "active_camera": "hero_wide" if phase != "postgame" else "winner_follow",
        "winner": state.get("winner"),
        "camera_packets": build_camera_packets(state),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL match director simulator")
    parser.add_argument("--state-file", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    state = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    payload = build_director_state(state)
    out_file = output_dir / "match_director_state.json"
    out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Match director state written: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
