import socket

PORT=9998
IP = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)