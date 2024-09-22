import socket
import threading

HOST = '127.0.0.1'
PORT = 7800

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print('Server is running and listening')

clients = []
nicknames = {}


def broadcast(message, sender_address):
    for client in clients:
        if client != sender_address:
            server_socket.sendto(message, client)


def receive():
    while True:
        try:
            message, address = server_socket.recvfrom(1024)
            if address not in clients:
                clients.append(address)
                nickname = message.decode('utf-8')
                nicknames[address] = nickname
                print(f"New client connected: {nickname} ({address})")
                broadcast(f"{nickname} has joined the chat".encode(), address)
            else:
                broadcast(message, address)
        except Exception as e:
            print(f"An error occurred: {e}")


receive_thread = threading.Thread(target=receive)
receive_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Server is shutting down...")
    server_socket.close()
