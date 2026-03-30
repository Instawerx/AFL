from __future__ import annotations
import argparse, json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def main() -> int:
    parser = argparse.ArgumentParser(description='AFL Blueprint implementation builder')
    parser.add_argument('--runtime-dir', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()

    r = Path(args.runtime_dir)
    o = Path(args.output_dir)
    o.mkdir(parents=True, exist_ok=True)

    runtime_manifest = load_json(r / 'demo_scene_runtime_manifest.json')
    widget_map = load_json(r / 'widget_binding_map.json')
    camera_manifest = load_json(r / 'camera_binding_manifest.json')
    polling_bridge = load_json(r / 'json_polling_bridge.json')

    bp_runtime_bridge = {
        "blueprint_class": "BP_AFL_RuntimeBridge",
        "parent_class": "Actor",
        "responsibilities": [
            "Poll runtime JSON folder",
            "Load widget binding map",
            "Load camera binding manifest",
            "Dispatch widget updates",
            "Dispatch camera cue updates",
        ],
        "functions": [
            "BeginPlay -> StartPolling",
            "StartPolling -> SetTimerByEvent",
            "LoadJsonArtifacts",
            "DispatchWidgetAndCameraState",
            "OnRuntimeManifestChanged",
        ],
        "polling_contract": polling_bridge,
    }

    bp_spectator_controller = {
        "blueprint_class": "BP_AFL_SpectatorController",
        "parent_class": "PlayerController",
        "responsibilities": [
            "Spawn spectator HUD widgets",
            "Consume runtime bridge updates",
            "Apply match phase state",
            "Apply camera cue state",
        ],
        "functions": [
            "InitSpectatorHUD",
            "ApplyWidgetState",
            "ApplyCameraCue",
            "ApplyPhaseState",
        ],
        "camera_contract": camera_manifest,
        "runtime_manifest": runtime_manifest,
    }

    out = {
        "bp_runtime_bridge_spec.json": bp_runtime_bridge,
        "bp_spectator_controller_spec.json": bp_spectator_controller,
        "bp_widget_binding_reference.json": widget_map,
    }

    for name, payload in out.items():
        (o / name).write_text(json.dumps(payload, indent=2), encoding='utf-8')

    print(f"Blueprint implementation specs written to: {o}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
