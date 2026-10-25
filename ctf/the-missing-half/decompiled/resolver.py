from protocol import serve
from ports import RESOLVER

IPS = ["192.0.2.17", "198.51.100.9", "203.0.113.44"]


def handle(req):
    run = req.get("run", "replay-01")
    idx = sum(run.encode()) % len(IPS)
    return {"name": req.get("name", "orchid.table"), "ip": IPS[idx],
            "ttl": 1 + idx, "alias": "orchid.archive" if idx == 1 else "orchid.table"}


if __name__ == "__main__":
    serve(RESOLVER, handle)
