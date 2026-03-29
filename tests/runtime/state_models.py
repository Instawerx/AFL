from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict


@dataclass
class PlayerState:
    player_id: str
    team: str
    ready: bool = False
    connected: bool = True
    objective_control: int = 0


@dataclass
class AuthoritativeMatchState:
    match_id: str
    session_id: str
    arena: str
    mode: str
    tick: int = 0
    state: str = "lobby"
    players: Dict[str, PlayerState] = field(default_factory=dict)
    winner: str | None = None

    def as_jsonable(self) -> dict:
        return {
            "match_id": self.match_id,
            "session_id": self.session_id,
            "arena": self.arena,
            "mode": self.mode,
            "tick": self.tick,
            "state": self.state,
            "winner": self.winner,
            "players": {k: asdict(v) for k, v in self.players.items()},
        }
