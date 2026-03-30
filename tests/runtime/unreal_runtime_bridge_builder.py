from __future__ import annotations

import argparse
import json
from pathlib import Path

from widget_binding_contracts import build_widget_binding_map
from camera_binding_manifest import build_camera_binding_manifest
from json_polling_bridge import build_json_polling_bridge

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL Unreal runtime bridge builder")
    parser.add_argument("--visual-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    visual_dir = Path(args.visual_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    required = [
        "scoreboard_umg_payload.json",
        "lower_thirds_umg_payload.json",
        "announcer_umg_payload.json",
        "phase_umg_payload.json",
        "camera_cue_timeline.json",
        "scene_playback_manifest.json",
    ]
    for name in required:
        path = visual_dir / name
        if not path.exists():
            raise SystemExit(f"Missing visual demo artifact: {path}")

    camera_timeline = load_json(visual_dir / "camera_cue_timeline.json")
    scene_manifest = load_json(visual_dir / "scene_playback_manifest.json")

    widget_map = build_widget_binding_map()
    camera_manifest = build_camera_binding_manifest(camera_timeline)
    polling_bridge = build_json_polling_bridge()

    demo_runtime_manifest = {
        "demo_map": "CrashSiteOmega_Demo",
        "lyra_compatible": True,
        "runtime_bridge_actor": "BP_AFL_RuntimeBridge",
        "spectator_controller": "BP_AFL_SpectatorController",
        "widget_binding_map_file": "widget_binding_map.json",
        "camera_binding_manifest_file": "camera_binding_manifest.json",
        "scene_playback_manifest_file": "scene_playback_manifest.json",
        "source_visual_manifest": scene_manifest,
    }

    (output_dir / "widget_binding_map.json").write_text(json.dumps(widget_map, indent=2), encoding="utf-8")
    (output_dir / "camera_binding_manifest.json").write_text(json.dumps(camera_manifest, indent=2), encoding="utf-8")
    (output_dir / "json_polling_bridge.json").write_text(json.dumps(polling_bridge, indent=2), encoding="utf-8")
    (output_dir / "demo_scene_runtime_manifest.json").write_text(json.dumps(demo_runtime_manifest, indent=2), encoding="utf-8")

    print(f"Unreal runtime bridge artifacts written to: {output_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
