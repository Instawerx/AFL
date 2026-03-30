from __future__ import annotations
import argparse, json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def main() -> int:
    parser = argparse.ArgumentParser(description='AFL Demo bootflow builder')
    parser.add_argument('--runtime-dir', required=True)
    parser.add_argument('--impl-dir', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()

    r = Path(args.runtime_dir)
    i = Path(args.impl_dir)
    o = Path(args.output_dir)
    o.mkdir(parents=True, exist_ok=True)

    lyra_manifest = load_json(r / 'lyra_demo_map_manifest.json')
    bp_runtime = load_json(i / 'bp_runtime_bridge_spec.json')
    bp_controller = load_json(i / 'bp_spectator_controller_spec.json')

    bootflow = {
        "bootflow_name": "AFL_Lyra_Demo_Boot",
        "map_name": lyra_manifest["map_name"],
        "startup_order": [
            "Spawn BP_AFL_RuntimeBridge",
            "Spawn BP_AFL_SpectatorController",
            "Create WBP_AFL_Scoreboard",
            "Create WBP_AFL_LowerThirdStack",
            "Create WBP_AFL_AnnouncerBanner",
            "Create WBP_AFL_MatchPhase",
            "Bind JSON polling updates",
            "Apply first camera cue",
            "Enter spectator demo mode",
        ],
        "runtime_bridge_class": bp_runtime["blueprint_class"],
        "spectator_controller_class": bp_controller["blueprint_class"],
        "lyra_compatible": True,
    }

    sequencing = {
        "sequencer_mode": "json_driven_demo",
        "camera_track_source": "camera_binding_manifest.json",
        "widget_update_source": "widget_binding_map.json",
        "runtime_manifest_source": "demo_scene_runtime_manifest.json",
    }

    (o / 'demo_bootflow_manifest.json').write_text(json.dumps(bootflow, indent=2), encoding='utf-8')
    (o / 'sequencer_binding_plan.json').write_text(json.dumps(sequencing, indent=2), encoding='utf-8')
    print(f"Demo bootflow artifacts written to: {o}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
