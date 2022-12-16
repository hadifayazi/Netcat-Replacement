import socket

TARGET_PORT=9998
TARGET_IP = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((TARGET_IP, TARGET_PORT))

client.send("Hello from client".encode('utf-8'))

response = client.recv(4096).decode('utf-8')
print(response)
client.close()
