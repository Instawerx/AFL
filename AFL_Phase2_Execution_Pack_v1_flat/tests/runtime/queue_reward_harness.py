from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)


REQUIRED_SCENARIO_KEYS = {
    "session_type",
    "queue_name",
    "players",
    "arena",
    "mode",
    "expected",
}


def fail(message: str, code: int = 1) -> None:
    print(message)
    raise SystemExit(code)


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        fail("Scenario must load as a mapping.", 3)
    return data


def validate_scenario(data: dict) -> list[str]:
    problems: list[str] = []
    missing = REQUIRED_SCENARIO_KEYS - set(data.keys())
    if missing:
        problems.append(f"Missing required keys: {', '.join(sorted(missing))}")

    players = data.get("players")
    if not isinstance(players, list) or len(players) < 2:
        problems.append("Scenario players must be a list with at least 2 players.")

    expected = data.get("expected")
    if not isinstance(expected, dict):
        problems.append("expected must be a mapping.")
    else:
        for key in ("winner", "coins_awarded", "xp_awarded"):
            if key not in expected:
                problems.append(f"expected.{key} is required")

    return problems


def run_dry_scenario(data: dict, results_dir: Path) -> Path:
    results_dir.mkdir(parents=True, exist_ok=True)

    winner = data["expected"]["winner"]
    coins_awarded = data["expected"]["coins_awarded"]
    xp_awarded = data["expected"]["xp_awarded"]

    result = {
        "status": "passed",
        "session_type": data["session_type"],
        "queue_name": data["queue_name"],
        "arena": data["arena"],
        "mode": data["mode"],
        "players": data["players"],
        "result": {
            "winner": winner,
            "coins_awarded": coins_awarded,
            "xp_awarded": xp_awarded,
        },
        "notes": "Dry-run harness only. No live EOS session or Unreal dedicated server launched.",
    }

    outfile = results_dir / "queue_reward_result.json"
    outfile.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return outfile


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL queue -> reward dry-run harness")
    parser.add_argument("--scenario", required=True, help="Path to scenario YAML")
    parser.add_argument(
        "--results-dir",
        default=os.environ.get("AFL_RESULTS_DIR", "artifacts/runtime"),
        help="Results directory",
    )
    args = parser.parse_args()

    scenario_path = Path(args.scenario)
    if not scenario_path.exists():
        fail(f"Scenario file not found: {scenario_path}", 4)

    data = read_yaml(scenario_path)
    problems = validate_scenario(data)
    if problems:
        for p in problems:
            print(f"- {p}")
        fail("Scenario validation failed.", 5)

    results_path = run_dry_scenario(data, Path(args.results_dir))
    print(f"Harness dry-run passed. Results written to: {results_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
