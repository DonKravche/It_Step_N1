
import socket

HOST = '127.0.0.2'
PORT = 3600


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1_socket:
    server1_socket.bind((HOST, PORT))
    server1_socket.listen()

    client_socket, address = server1_socket.accept()
    print(f'Accepted connection from {address}')

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            with open("data.txt", "w") as file:
                file.write(data)
        else:
            print('Client disconnected')