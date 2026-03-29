from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL session history query")
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    index_file = Path(args.data_dir) / "session_history.json"
    if not index_file.exists():
        raise SystemExit("No session history found.")

    data = json.loads(index_file.read_text(encoding="utf-8"))
    rows = list(reversed(data))[: args.limit]

    for row in rows:
        print(json.dumps(row, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
