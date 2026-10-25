"""Tiny JSON-lines protocol shared by the local challenge modules."""
import json
import socket


def ask(port, payload, timeout=1.0):
    raw = (json.dumps(payload, separators=(",", ":")) + "\n").encode()
    with socket.create_connection(("127.0.0.1", port), timeout=timeout) as sock:
        sock.settimeout(timeout)
        sock.sendall(raw)
        data = b""
        while not data.endswith(b"\n"):
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
    return json.loads(data.decode())


def serve(port, callback):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(32)
    print(f"listening 127.0.0.1:{port}", flush=True)
    while True:
        conn, _ = server.accept()
        with conn:
            conn.settimeout(2.0)
            try:
                data = b""
                while not data.endswith(b"\n") and len(data) < 65536:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    data += chunk
                req = json.loads(data.decode() or "{}")
                result = callback(req)
                conn.sendall((json.dumps(result) + "\n").encode())
            except Exception as exc:
                conn.sendall((json.dumps({"error": type(exc).__name__}) + "\n").encode())
