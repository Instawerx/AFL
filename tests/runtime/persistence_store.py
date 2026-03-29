from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from persistence_models import PersistedSessionRecord


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_runtime_artifacts(runtime_dir: Path) -> list[Path]:
    candidates = [
        runtime_dir / "authoritative_match_result.json",
        runtime_dir / "playback_match_result.json",
        runtime_dir / "live_match_result.json",
        runtime_dir / "multiplayer_match_result.json",
        runtime_dir / "match_result.json",
    ]
    return [p for p in candidates if p.exists()]


def archive_artifact(source: Path, archive_dir: Path) -> Path:
    archive_dir.mkdir(parents=True, exist_ok=True)
    target = archive_dir / source.name
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return target


def append_index(index_file: Path, record: dict[str, Any]) -> None:
    if index_file.exists():
        data = json.loads(index_file.read_text(encoding="utf-8"))
    else:
        data = []
    data.append(record)
    index_file.parent.mkdir(parents=True, exist_ok=True)
    index_file.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL local persistence store")
    parser.add_argument("--runtime-dir", required=True)
    parser.add_argument("--data-dir", required=True)
    args = parser.parse_args()

    runtime_dir = Path(args.runtime_dir)
    data_dir = Path(args.data_dir)
    sessions_dir = data_dir / "sessions"
    archive_dir = data_dir / "archive"
    index_file = data_dir / "session_history.json"

    found = read_runtime_artifacts(runtime_dir)
    if not found:
        raise SystemExit("No runtime match result artifacts found to archive.")

    for source in found:
        payload = load_json(source)
        archived = archive_artifact(source, archive_dir)
        record = PersistedSessionRecord(
            session_id=str(payload.get("session_id", payload.get("match_id", "unknown_session"))),
            match_id=str(payload.get("match_id", payload.get("session_id", "unknown_match"))),
            winner=payload.get("winner"),
            session_valid=bool(payload.get("session_valid", True)),
            source_file=str(archived),
            archived_at=now_iso(),
        )
        append_index(index_file, record.as_jsonable())

        session_file = sessions_dir / f"{record.session_id}.json"
        session_file.parent.mkdir(parents=True, exist_ok=True)
        session_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"Archived {len(found)} runtime artifact(s) into {data_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
