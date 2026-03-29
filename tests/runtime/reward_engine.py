from __future__ import annotations

import argparse
import json
from pathlib import Path

from anti_abuse_rules import evaluate_abuse


def calculate_rewards(result_payload: dict) -> dict:
    abuse_flags = evaluate_abuse(result_payload)
    eligible = len(abuse_flags) == 0 and result_payload.get("session_valid", False)

    if not eligible:
        return {
            "eligible": False,
            "coins_awarded": 0,
            "xp_awarded": 0,
            "abuse_flags": abuse_flags,
        }

    return {
        "eligible": True,
        "coins_awarded": int(result_payload.get("coins_awarded", 0)),
        "xp_awarded": int(result_payload.get("xp_awarded", 0)),
        "abuse_flags": abuse_flags,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-file", required=True)
    args = parser.parse_args()

    result_file = Path(args.result_file)
    payload = json.loads(result_file.read_text(encoding="utf-8"))
    rewards = calculate_rewards(payload)

    out_dir = Path("artifacts/runtime")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "reward_result.json"
    out_file.write_text(json.dumps(rewards, indent=2), encoding="utf-8")

    print(f"Reward validation completed: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
