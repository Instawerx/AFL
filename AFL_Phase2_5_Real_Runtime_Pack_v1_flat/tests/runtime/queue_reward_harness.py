from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)

from orchestrator import run_pipeline
from runtime_config import RuntimeConfig

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

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL queue -> reward runtime harness")
    parser.add_argument("--scenario", required=True, help="Path to scenario YAML")
    parser.add_argument("--env-file", required=False, help="Optional runtime env file")
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

    config = RuntimeConfig.from_env(args.env_file)
    result = run_pipeline(config, data)
    print("Harness runtime passed.")
    print(f"Runtime mode: {result['runtime_mode']}")
    print(f"Result file: {result['result_file']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
