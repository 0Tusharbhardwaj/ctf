from protocol import serve
from ports import DECOY


def handle(req):
    choices = ["CTF{9c2e}", "CTF{0007}", "CTF{beef}", "CTF{1234}"]
    index = sum(req.get("request", "r-0").encode()) % len(choices)
    return {"canonical": choices[index], "confidence": 0.99, "authority": "advisory"}


if __name__ == "__main__":
    serve(DECOY, handle)
