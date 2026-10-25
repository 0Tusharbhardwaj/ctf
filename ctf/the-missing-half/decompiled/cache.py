from protocol import serve
from ports import CACHE


def handle(req):
    rid = req.get("request", "r-0")
    age = (sum(rid.encode()) * 7) % 41
    return {"status": "HIT" if age > 20 else "MISS", "age": age,
            "generation": 5 if age > 20 else 7, "request": rid}


if __name__ == "__main__":
    serve(CACHE, handle)
