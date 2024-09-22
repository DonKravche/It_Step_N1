import socket
import threading

HOST = '127.0.0.1'
PORT = 7800

user_name = input('Hello Customer! Please enter your name: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((HOST, PORT))


def write():
    while True:
        message = f"{user_name}: {input()}"
        client_socket.send(message.encode())


def receive():
    while True:
        try:
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))
        except Exception as e:
            print(f"An error occurred: {e}")
            break


client_socket.send(user_name.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
