from __future__ import annotations
import argparse, json
from pathlib import Path

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def main() -> int:
    parser = argparse.ArgumentParser(description='AFL Widget implementation builder')
    parser.add_argument('--runtime-dir', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()

    r = Path(args.runtime_dir)
    o = Path(args.output_dir)
    o.mkdir(parents=True, exist_ok=True)

    widget_map = load_json(r / 'widget_binding_map.json')

    scoreboard = {
        "widget_class": "WBP_AFL_Scoreboard",
        "hierarchy": ["RootCanvas", "TitleText", "WinnerText", "TeamAList", "TeamBList", "TeamAScore", "TeamBScore"],
        "binding_map": widget_map["scoreboard_widget"]["bindings"],
    }
    lower = {
        "widget_class": "WBP_AFL_LowerThirdStack",
        "hierarchy": ["RootCanvas", "CardRepeater"],
        "binding_map": widget_map["lower_third_widget"]["bindings"],
    }
    announcer = {
        "widget_class": "WBP_AFL_AnnouncerBanner",
        "hierarchy": ["RootCanvas", "MessageText"],
        "binding_map": widget_map["announcer_widget"]["bindings"],
    }
    phase = {
        "widget_class": "WBP_AFL_MatchPhase",
        "hierarchy": ["RootCanvas", "PhaseText", "CameraText", "WinnerText"],
        "binding_map": widget_map["phase_widget"]["bindings"],
    }

    out = {
        "widget_scoreboard_impl.json": scoreboard,
        "widget_lower_thirds_impl.json": lower,
        "widget_announcer_impl.json": announcer,
        "widget_phase_impl.json": phase,
    }

    for name, payload in out.items():
        (o / name).write_text(json.dumps(payload, indent=2), encoding='utf-8')

    print(f"Widget implementation specs written to: {o}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
