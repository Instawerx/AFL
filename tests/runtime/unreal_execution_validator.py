from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED_IMPL = [
    "bp_runtime_bridge_spec.json",
    "bp_spectator_controller_spec.json",
    "widget_scoreboard_impl.json",
    "widget_lower_thirds_impl.json",
    "widget_announcer_impl.json",
    "widget_phase_impl.json",
    "demo_bootflow_manifest.json",
    "sequencer_binding_plan.json",
]

REQUIRED_RUNTIME = [
    "widget_binding_map.json",
    "camera_binding_manifest.json",
    "json_polling_bridge.json",
    "demo_scene_runtime_manifest.json",
    "lyra_demo_map_manifest.json",
]

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL Unreal execution validator")
    parser.add_argument("--impl-dir", required=True)
    parser.add_argument("--runtime-dir", required=True)
    args = parser.parse_args()

    impl_dir = Path(args.impl_dir)
    runtime_dir = Path(args.runtime_dir)

    missing = []
    for name in REQUIRED_IMPL:
        if not (impl_dir / name).exists():
            missing.append(f"impl:{name}")
    for name in REQUIRED_RUNTIME:
        if not (runtime_dir / name).exists():
            missing.append(f"runtime:{name}")

    if missing:
        raise SystemExit("\n".join(missing))

    print(json.dumps({
        "status": "passed",
        "impl_dir": str(impl_dir),
        "runtime_dir": str(runtime_dir),
        "checked_impl": REQUIRED_IMPL,
        "checked_runtime": REQUIRED_RUNTIME,
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
