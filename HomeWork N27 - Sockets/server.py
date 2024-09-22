import socket

HOST = '127.0.0.1'
PORT = 4300

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'Port {PORT} is listening')

    client_socket, address = server_socket.accept()
    print(f'Accepted connection from {address}')

    with client_socket:
        while True:
            try:
                data = client_socket.recv(1024)

                # If data is empty, the client has closed the connection
                if not data:
                    print("Client disconnected")
                    break

                print(f"Received: {data.decode('utf-8')}")

                message = "Connection established! \nThank you for connecting!"
                client_socket.sendall(message.encode('utf-8'))

            except ConnectionResetError:
                print("Connection reset by peer")
                break

            except ConnectionAbortedError:
                print("Connection aborted by peer")
                break

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
