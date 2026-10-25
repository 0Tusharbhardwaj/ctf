from protocol import serve
from ports import LEDGER


def handle(req):
    rid = req.get("request", "r-0")
    return {"request": rid, "parent": "r-" + str(max(0, sum(rid.encode()) % 11 - 1)),
            "decision_id": req.get("decision", "d-unknown"), "flush_order": "buffered"}


if __name__ == "__main__":
    serve(LEDGER, handle)
