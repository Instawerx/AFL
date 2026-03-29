from __future__ import annotations

import argparse
import json
import socket
import threading
import time


def serve_health(port: int, stop_flag: dict) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", port))
    sock.listen(5)
    sock.settimeout(0.5)
    while not stop_flag["stop"]:
        try:
            conn, _ = sock.accept()
            conn.sendall(b"AFL_STUB_OK")
            conn.close()
        except socket.timeout:
            continue
    sock.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health-port", type=int, required=True)
    parser.add_argument("--lifetime", type=int, default=12)
    args = parser.parse_args()

    stop_flag = {"stop": False}
    t = threading.Thread(target=serve_health, args=(args.health_port, stop_flag), daemon=True)
    t.start()

    print(json.dumps({"status": "started", "health_port": args.health_port}))
    time.sleep(args.lifetime)
    stop_flag["stop"] = True
    t.join(timeout=2)
    print(json.dumps({"status": "stopped"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
