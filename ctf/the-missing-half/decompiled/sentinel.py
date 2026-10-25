from protocol import serve
from ports import SENTINEL


def handle(req):
    return {"health": "green", "reason": "pid-exists", "ready": False,
            "generation": req.get("generation", 6)}


if __name__ == "__main__":
    serve(SENTINEL, handle)
