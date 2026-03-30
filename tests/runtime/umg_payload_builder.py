from __future__ import annotations

import argparse, json
from pathlib import Path
from umg_contracts import build_umg_announcer, build_umg_lower_thirds, build_umg_phase, build_umg_scoreboard

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL UMG payload builder")
    parser.add_argument("--hud-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    hud = Path(args.hud_dir)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    scoreboard = load_json(hud / "scoreboard_widget_contract.json")
    lower = load_json(hud / "lower_third_widget_contract.json")
    announcer = load_json(hud / "announcer_widget_contract.json")
    phase = load_json(hud / "match_phase_widget_contract.json")

    bundles = {
        "scoreboard_umg_payload.json": build_umg_scoreboard(scoreboard),
        "lower_thirds_umg_payload.json": build_umg_lower_thirds(lower),
        "announcer_umg_payload.json": build_umg_announcer(announcer),
        "phase_umg_payload.json": build_umg_phase(phase),
    }

    for name, payload in bundles.items():
        (out / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"UMG payloads written to: {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
