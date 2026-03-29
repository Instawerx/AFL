from __future__ import annotations

import argparse
import json
from pathlib import Path
import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)

from result_contract import validate_result_contract
from reward_service import calculate_rewards


def load_env_file(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def get_env(name: str, overrides: dict[str, str], default: str = "") -> str:
    return os.getenv(name, overrides.get(name, default))


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Scenario must load as a mapping.")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL EOS smoke adapter")
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--env-file", required=False)
    args = parser.parse_args()

    overrides = load_env_file(Path(args.env_file)) if args.env_file else {}
    scenario = read_yaml(Path(args.scenario))

    eos_fields = [
        "EOS_PRODUCT_ID",
        "EOS_SANDBOX_ID",
        "EOS_DEPLOYMENT_ID",
        "EOS_CLIENT_ID",
        "EOS_CLIENT_SECRET",
    ]
    missing = [name for name in eos_fields if not get_env(name, overrides, "")]
    eos_ready = len(missing) == 0

    result_payload = {
        "winner": scenario["expected"]["winner"],
        "coins_awarded": int(scenario["expected"]["coins_awarded"]),
        "xp_awarded": int(scenario["expected"]["xp_awarded"]),
        "session_valid": True,
        "objective_events": [
            {"event": "objective_entered", "player": scenario["players"][0]},
            {"event": "capture_completed", "player": scenario["expected"]["winner"]},
        ],
    }

    problems = validate_result_contract(result_payload)
    if problems:
        for p in problems:
            print(f"- {p}")
        return 3

    rewards = calculate_rewards(scenario["session_type"], result_payload)

    output = {
        "status": "passed",
        "eos_ready": eos_ready,
        "missing_eos_fields": missing,
        "session_type": scenario["session_type"],
        "queue_name": scenario["queue_name"],
        "arena": scenario["arena"],
        "mode": scenario["mode"],
        "result": result_payload,
        "reward_result": rewards,
        "notes": "Phase 3 EOS smoke adapter validates config, contract, and reward boundary.",
    }

    out_dir = Path("artifacts/runtime")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "eos_session_smoke_result.json"
    out_file.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(f"EOS smoke passed. Result file: {out_file}")
    if not eos_ready:
        print("EOS config is incomplete; smoke run completed in config-validation mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
