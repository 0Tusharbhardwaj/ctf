from protocol import serve
from ports import WORKER_B


def handle(req):
    return {"worker": "table-b", "generation": 7, "label": (sum(req.get("candidate", "").encode()) * 5) % 17}


if __name__ == "__main__":
    serve(WORKER_B, handle)
