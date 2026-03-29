from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict, List


@dataclass
class ConnectedClient:
    player_id: str
    ready: bool = False
    team: str | None = None


@dataclass
class SessionState:
    session_id: str
    queue_name: str
    session_type: str
    arena: str
    mode: str
    state: str = "lobby"
    clients: Dict[str, ConnectedClient] = field(default_factory=dict)

    def as_jsonable(self) -> dict:
        return {
            "session_id": self.session_id,
            "queue_name": self.queue_name,
            "session_type": self.session_type,
            "arena": self.arena,
            "mode": self.mode,
            "state": self.state,
            "clients": {k: asdict(v) for k, v in self.clients.items()},
        }
