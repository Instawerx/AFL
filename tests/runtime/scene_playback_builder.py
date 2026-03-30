from __future__ import annotations

import argparse, json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL scene playback builder")
    parser.add_argument("--visual-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    visual = Path(args.visual_dir)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    scoreboard = load_json(visual / "scoreboard_umg_payload.json")
    lower = load_json(visual / "lower_thirds_umg_payload.json")
    announcer = load_json(visual / "announcer_umg_payload.json")
    phase = load_json(visual / "phase_umg_payload.json")
    camera_timeline = load_json(visual / "camera_cue_timeline.json")

    manifest = {
        "demo_name": "AFL_Investor_Demo_Visual",
        "sequence": [
            {"step": "load_scoreboard", "widget": scoreboard["widget_name"]},
            {"step": "load_lower_thirds", "widget": lower["widget_name"]},
            {"step": "load_announcer", "widget": announcer["widget_name"]},
            {"step": "load_phase_widget", "widget": phase["widget_name"]},
            {"step": "play_camera_timeline", "cue_count": len(camera_timeline)},
        ],
        "winner": phase["data"].get("winner"),
    }

    (out / "scene_playback_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Scene playback manifest written: {out / 'scene_playback_manifest.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
