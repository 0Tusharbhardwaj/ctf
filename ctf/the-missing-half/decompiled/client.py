#!/usr/bin/env python3
import json
from protocol import ask
from ports import FRONTDOOR


def main():
    print("ORCHID front door. Commands: topology | inspect [request-id] | submit <candidate> | prove <a> <b> | help | quit")
    while True:
        try:
            parts = input("orchid> ").strip().split()
        except EOFError:
            break
        if not parts:
            continue
        cmd = parts[0]
        if cmd in ("quit", "exit"):
            break
        req = {"command": cmd}
        if cmd == "inspect" and len(parts) > 1:
            req["request"] = parts[1]
        elif cmd == "submit" and len(parts) > 1:
            req["candidate"] = parts[1]
        elif cmd == "prove" and len(parts) > 2:
            req["candidate"], req["second"] = parts[1:3]
        try:
            print(json.dumps(ask(FRONTDOOR, req), indent=2))
        except OSError as exc:
            print(f"front door unavailable: {exc}")


if __name__ == "__main__":
    main()
