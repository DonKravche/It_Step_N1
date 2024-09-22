import socket

HOST = '127.0.0.2'
PORT = 3600

with socket.socket() as client1_socket:
    client1_socket.connect((HOST, PORT))
    client1_socket.send(b'Hello, Server! From Client!')

    while True:
        data = client1_socket.recv(1024).decode('utf-8')

        print(data)