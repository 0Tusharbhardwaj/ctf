from protocol import serve
from ports import WORKER_A


def handle(req):
    return {"worker": "table-a", "generation": 6, "label": (len(req.get("candidate", "")) * 3) % 17}


if __name__ == "__main__":
    serve(WORKER_A, handle)
