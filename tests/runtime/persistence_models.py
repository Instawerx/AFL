from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class PersistedSessionRecord:
    session_id: str
    match_id: str
    winner: str | None
    session_valid: bool
    source_file: str
    archived_at: str

    def as_jsonable(self) -> dict[str, Any]:
        return asdict(self)
