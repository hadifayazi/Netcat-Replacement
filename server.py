import socket
import threading


PORT=9998
IP = socket.gethostbyname(socket.gethostname())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT} ")

    while True:
        client_socket, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]} ")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()