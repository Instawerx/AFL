from __future__ import annotations

import argparse, json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL camera timeline builder")
    parser.add_argument("--broadcast-dir", required=True)
    parser.add_argument("--hud-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    b = Path(args.broadcast_dir)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    director = load_json(b / "match_director_state.json")
    camera_packets = load_json(b / "camera_packets.json")
    ui_state = load_json(Path(args.hud_dir) / "spectator_ui_state.json")

    phase = director.get("phase", "pregame")
    cues = []
    tick = 0
    for packet in camera_packets:
        cues.append({
            "time_index": tick,
            "camera_id": packet.get("camera_id"),
            "mode": packet.get("mode"),
            "target": packet.get("target"),
            "phase": phase,
            "overlay_state": ui_state.get("overlay_visibility", {}),
        })
        tick += 1

    (out / "camera_cue_timeline.json").write_text(json.dumps(cues, indent=2), encoding="utf-8")
    print(f"Camera cue timeline written: {out / 'camera_cue_timeline.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
