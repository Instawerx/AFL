from __future__ import annotations

import argparse
import json
import socket
from pathlib import Path

from state_packet_schema import validate_state_packet


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL spectator UDP simulator")
    parser.add_argument("--port", type=int, default=9120)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-packets", type=int, default=5)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", args.port))
    sock.settimeout(5)

    packets = []
    try:
        while len(packets) < args.max_packets:
            data, _ = sock.recvfrom(65535)
            packet = json.loads(data.decode("utf-8"))
            problems = validate_state_packet(packet)
            if problems:
                raise SystemExit("\n".join(problems))
            packets.append(packet)
    finally:
        sock.close()

    (output_dir / "spectator_packets.json").write_text(json.dumps(packets, indent=2), encoding="utf-8")
    print(f"Spectator received {len(packets)} packets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
