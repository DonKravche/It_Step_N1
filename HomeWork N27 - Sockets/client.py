import socket

HOST = '127.0.0.1'
PORT = 4300

with socket.socket() as client_socket:
    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        client_socket.send(b'Hello, server!')

        while True:
            data = client_socket.recv(1024)

            if not data:
                print("Server closed the connection")
                break

            print(f"Received from server: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Connection refused by the server")

    except Exception as e:
        print(f"An error occurred: {e}")
