from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_events(out_file: Path, events: list[dict[str, Any]]) -> Path:
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(events, indent=2), encoding="utf-8")
    return out_file


def read_events(in_file: Path) -> list[dict[str, Any]]:
    data = json.loads(in_file.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Event file must contain a list of events.")
    return data
