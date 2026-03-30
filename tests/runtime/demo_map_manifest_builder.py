from __future__ import annotations

import argparse
import json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL demo map manifest builder")
    parser.add_argument("--runtime-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    runtime_dir = Path(args.runtime_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    runtime_manifest = load_json(runtime_dir / "demo_scene_runtime_manifest.json")
    widget_map = load_json(runtime_dir / "widget_binding_map.json")
    camera_manifest = load_json(runtime_dir / "camera_binding_manifest.json")
    polling_bridge = load_json(runtime_dir / "json_polling_bridge.json")

    payload = {
        "map_name": runtime_manifest["demo_map"],
        "arena": "CrashSiteOmega",
        "mode": "AssaultCore",
        "startup_sequence": [
            "Spawn BP_AFL_RuntimeBridge",
            "Spawn BP_AFL_SpectatorController",
            "Load widget binding map",
            "Load camera binding manifest",
            "Start JSON polling bridge",
            "Apply scene playback manifest",
        ],
        "widget_classes": [v["widget_class"] for v in widget_map.values()],
        "camera_track": camera_manifest["sequencer_track_name"],
        "bridge_mode": polling_bridge["bridge_mode"],
    }

    (output_dir / "lyra_demo_map_manifest.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Lyra demo map manifest written: {output_dir / 'lyra_demo_map_manifest.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
