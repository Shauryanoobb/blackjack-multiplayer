import socket
import json

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break  # client disconnected

        msg = json.loads(data.decode())
        print("Received:", msg)

        if msg["type"] == "JOIN_GAME":
            response = {"type": "GAME_START", "hand": ["K♣", "5♦"]}
            conn.send(json.dumps(response).encode())

        elif msg["type"] == "ACTION":
            response = {"type": "ACK", "action": msg["action"]}
            conn.send(json.dumps(response).encode())

    conn.close()
    print("Client disconnected")

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 9999))
    s.listen()
    print("Server listening on port 9999...")

    conn, addr = s.accept()
    handle_client(conn, addr)

if __name__ == "__main__":
    run_server()
