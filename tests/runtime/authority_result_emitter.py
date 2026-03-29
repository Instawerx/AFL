from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def emit_authority_artifacts(output_dir: Path, state_payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    match_result = {
        "match_id": state_payload["match_id"],
        "session_id": state_payload["session_id"],
        "winner": state_payload["winner"],
        "session_valid": True,
        "coins_awarded": 100 if state_payload["winner"] else 0,
        "xp_awarded": 250 if state_payload["winner"] else 0,
        "objective_events": [
            {"event_type": "authoritative_match_end", "winner": state_payload["winner"], "tick": state_payload["tick"]}
        ],
    }

    reward_result = {
        "eligible": bool(state_payload["winner"]),
        "coins_awarded": match_result["coins_awarded"],
        "xp_awarded": match_result["xp_awarded"],
    }

    (output_dir / "authoritative_state_snapshot.json").write_text(json.dumps(state_payload, indent=2), encoding="utf-8")
    (output_dir / "authoritative_match_result.json").write_text(json.dumps(match_result, indent=2), encoding="utf-8")
    (output_dir / "authoritative_reward_result.json").write_text(json.dumps(reward_result, indent=2), encoding="utf-8")
