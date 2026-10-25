#!/usr/bin/env python3
"""Start and supervise the local ORCHID service modules."""
import os
import signal
import socket
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
MODULES = ["resolver.py", "chaos.py", "broker.py", "cache.py", "worker_a.py",
           "worker_b.py", "sentinel.py", "decoy.py", "ledger.py", "gateway.py"]
PORTS = [17101, 17103, 17102, 17104, 17105, 17106, 17107, 17108, 17109, 17111]
children = []


def stop(*_):
    for proc in reversed(children):
        if proc.poll() is None:
            proc.terminate()
    for proc in children:
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
    raise SystemExit(0)


def main():
    if not os.path.exists(os.path.join(ROOT, "verifier-core")):
        raise SystemExit("verifier-core is missing; see build instructions in ../organizer/SOLUTION.md")
    try:
        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        probe.close()
    except OSError as exc:
        raise SystemExit(f"local TCP sockets are unavailable: {exc}")
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    for module in MODULES:
        children.append(subprocess.Popen([sys.executable, os.path.join(ROOT, module)], cwd=ROOT))
    deadline = time.monotonic() + 5
    pending = set(PORTS)
    while pending and time.monotonic() < deadline:
        for port in tuple(pending):
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.1):
                    pending.remove(port)
            except OSError:
                pass
        if pending:
            time.sleep(0.05)
    dead = [p for p in children if p.poll() is not None]
    if dead or pending:
        stop()
    print("ORCHID local suite ready at 127.0.0.1:17111; Ctrl-C to stop", flush=True)
    try:
        while True:
            time.sleep(1)
            if any(p.poll() is not None for p in children):
                print("module exited; stopping suite", file=sys.stderr)
                stop()
    except KeyboardInterrupt:
        stop()


if __name__ == "__main__":
    main()
