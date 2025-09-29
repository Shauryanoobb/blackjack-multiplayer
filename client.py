import socket
import json

def run_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9999))

    # Join game
    s.send(json.dumps({"type": "JOIN_GAME", "player": "Alice"}).encode())
    data = s.recv(1024)
    print("Server:", json.loads(data.decode()))

    # Example action
    s.send(json.dumps({"type": "ACTION", "action": "HIT"}).encode())
    data = s.recv(1024)
    print("Server:", json.loads(data.decode()))

    s.close()

if __name__ == "__main__":
    run_client()
