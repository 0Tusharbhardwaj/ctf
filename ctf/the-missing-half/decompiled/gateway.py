import os
import subprocess
from protocol import ask, serve
from ports import (FRONTDOOR, BROKER, CACHE, SENTINEL, DECOY, LEDGER,
                   WORKER_A, WORKER_B)

ROOT = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.join(ROOT, "verifier-core")


def verify(candidate):
    try:
        p = subprocess.run([CORE, candidate], text=True, capture_output=True, timeout=1)
        return {"accepted": p.returncode == 0, "verifier": p.stdout.strip() or "core unavailable"}
    except (OSError, subprocess.TimeoutExpired):
        return {"accepted": False, "verifier": "core unavailable"}


def handle(req):
    command = req.get("command", "help")
    run = req.get("run", "replay-01")
    rid = req.get("request", "r-17")
    if command == "topology":
        return {"modules": ["resolver", "broker", "chaos", "cache", "worker-a", "worker-b",
                            "sentinel", "decoy", "ledger", "verifier-core", "gateway"],
                "network": "loopback-only", "simulated_ips": ["192.0.2.17", "198.51.100.9", "203.0.113.44"]}
    if command == "inspect":
        return {
            "route": ask(BROKER, {"run": run, "request": rid}),
            "cache": ask(CACHE, {"request": rid}),
            "health": ask(SENTINEL, {"generation": 7}),
            "decoy": ask(DECOY, {"request": rid}),
            "worker_a": ask(WORKER_A, {"candidate": req.get("candidate", "")} ),
            "worker_b": ask(WORKER_B, {"candidate": req.get("candidate", "")} ),
            "ledger": ask(LEDGER, {"request": rid}),
        }
    if command == "submit":
        candidate = req.get("candidate", "")
        result = verify(candidate)
        decision = "d-" + str(sum(candidate.encode()) % 10000)
        result["decision_id"] = decision
        result["request"] = rid
        result["notes"] = "decoy and sentinel values are advisory"
        return result
    if command == "prove":
        a, b = req.get("candidate", ""), req.get("second", "")
        va, vb = verify(a), verify(b)
        valid = a != b and va["accepted"] and vb["accepted"]
        return {"proved": valid, "distinct": a != b, "first": va, "second": vb,
                "result": "NON-UNIQUENESS DEMONSTRATED" if valid else "proof rejected"}
    if command == "help":
        return {"commands": ["topology", "inspect", "submit", "prove"],
                "example": {"command": "submit", "candidate": "CTF{0000}"}}
    return {"error": "unknown command", "commands": ["topology", "inspect", "submit", "prove"]}


if __name__ == "__main__":
    serve(FRONTDOOR, handle)
