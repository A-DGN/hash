import socket
import hashlib

def hash_data(data):
    result = hashlib.sha256(data.encode()).hexdigest()
    return result

def send_hash_to_server(data):
    hashed_data = hash_data(data)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("server_address", server_port))
        s.sendall(hashed_data.encode())
        response = s.recv(1024)
        print(f"Received from server: {response.decode()}")
