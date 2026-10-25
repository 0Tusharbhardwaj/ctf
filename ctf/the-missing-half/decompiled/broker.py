from protocol import ask, serve
from ports import BROKER, RESOLVER, CHAOS


def handle(req):
    run, rid = req.get("run", "replay-01"), req.get("request", "r-0")
    dns = ask(RESOLVER, {"name": "orchid.table", "run": run})
    fault = ask(CHAOS, {"run": run, "request": rid})
    peer = "table-a" if fault["schedule_index"] % 2 else "table-b"
    return {"peer": peer, "ip": dns["ip"], "generation": 6 + fault["schedule_index"] % 2,
            "fault": fault["fault"], "request": rid}


if __name__ == "__main__":
    serve(BROKER, handle)
