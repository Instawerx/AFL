from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)

from session_registry import SessionRegistry
from lobby_simulator import build_lobby
from match_coordinator import run_match


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Scenario must load as a mapping.")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL multiplayer orchestrator")
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    scenario = read_yaml(Path(args.scenario))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    players = scenario.get("players", [])
    if len(players) < 2:
        raise SystemExit("Scenario players must include at least 2 players.")

    registry = SessionRegistry()
    session = registry.create_session(
        queue_name=scenario["queue_name"],
        session_type=scenario["session_type"],
        arena=scenario["arena"],
        mode=scenario["mode"],
    )

    for player in players:
        registry.add_player(session.session_id, player)

    lobby = build_lobby(players, min_players=int(scenario.get("session", {}).get("min_players", 2)))
    if not lobby.ready:
        raise SystemExit("Lobby failed readiness check.")

    registry.set_state(session.session_id, "ready")
    match = run_match(players, lobby.teams, scenario)
    registry.set_state(session.session_id, "completed")

    session_payload = registry.export()[0]
    match_payload = {
        "session_id": session.session_id,
        "winner": match.winner,
        "duration_seconds": match.duration_seconds,
        "session_valid": match.session_valid,
        "objective_events": match.objective_events,
        "coins_awarded": int(scenario["expected"]["coins_awarded"]),
        "xp_awarded": int(scenario["expected"]["xp_awarded"]),
    }
    reward_payload = {
        "session_id": session.session_id,
        "eligible": bool(match.session_valid),
        "coins_awarded": int(scenario["expected"]["coins_awarded"]) if match.session_valid else 0,
        "xp_awarded": int(scenario["expected"]["xp_awarded"]) if match.session_valid else 0,
    }

    (output_dir / "multiplayer_session.json").write_text(json.dumps(session_payload, indent=2), encoding="utf-8")
    (output_dir / "multiplayer_match_result.json").write_text(json.dumps(match_payload, indent=2), encoding="utf-8")
    (output_dir / "multiplayer_reward_result.json").write_text(json.dumps(reward_payload, indent=2), encoding="utf-8")

    print(f"Multiplayer session completed: {session.session_id}")
    print(f"Winner: {match.winner}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
