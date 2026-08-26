import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Server started...")
print(f"Listening on {HOST}:{PORT}")

receiver_conn = None

while True:
    conn, address = server.accept()

    role = conn.recv(1024).decode()

    if role == "RECEIVER":
        receiver_conn = conn
        print("Receiver connected:", address)

    elif role == "SENDER":
        print("Sender connected:", address)

        encrypted_message = conn.recv(4096)

        print("\nEncrypted message received by server:")
        print(encrypted_message.decode())

        if receiver_conn:
            receiver_conn.sendall(encrypted_message)
            print("\nEncrypted message forwarded to receiver.")

        conn.close()

        if receiver_conn:
            receiver_conn.close()

        break

server.close()
print("\nServer closed.")