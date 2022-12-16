import socket
import threading


PORT=9998
IP = socket.gethostbyname(socket.gethostname())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT} ")