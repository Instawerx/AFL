from __future__ import annotations

import argparse
from pathlib import Path
import os
import subprocess
import sys
import time


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


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL local Unreal server adapter")
    parser.add_argument("--env-file", required=False)
    args = parser.parse_args()

    overrides = load_env_file(Path(args.env_file)) if args.env_file else {}
    def get(name: str, default: str = "") -> str:
        return os.getenv(name, overrides.get(name, default))

    server_exe = get("AFL_SERVER_EXE", "")
    server_args = get("AFL_SERVER_ARGS", "")

    if not server_exe:
        print("No AFL_SERVER_EXE configured. Unreal adapter running in no-op mode.")
        return 0

    exe_path = Path(server_exe)
    if not exe_path.exists():
        print(f"Configured AFL_SERVER_EXE not found: {exe_path}")
        return 2

    cmd = [str(exe_path)]
    if server_args.strip():
        cmd.extend(server_args.split())

    proc = subprocess.Popen(cmd)
    print(f"Started Unreal server process: pid={proc.pid}")
    time.sleep(3)
    proc.terminate()
    print("Stopped Unreal server process.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
