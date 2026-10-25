from protocol import serve
from ports import CHAOS


def handle(req):
    run = req.get("run", "replay-01")
    request_id = req.get("request", "r-0")
    value = sum((i + 1) * b for i, b in enumerate((run + request_id).encode()))
    modes = ["ok", "timeout-once", "stale-cache", "reordered-ledger", "truncated-frame"]
    mode = modes[value % len(modes)]
    return {"run": run, "request": request_id, "schedule_index": value % 97, "fault": mode}


if __name__ == "__main__":
    serve(CHAOS, handle)
