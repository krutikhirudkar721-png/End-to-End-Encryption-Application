import socket
from crypto_utils import decrypt_message

HOST = "127.0.0.1"
PORT = 5000

# Load shared secret key
with open("shared_key.bin", "rb") as file:
    key = file.read()

# Connect to server
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.connect((HOST, PORT))

# Identify as receiver
receiver.sendall(b"RECEIVER")

print("Receiver connected. Waiting for message...")

# Receive encrypted message
encrypted_message = receiver.recv(4096).decode()

print("\nEncrypted message received:")
print(encrypted_message)

# Decrypt
decrypted = decrypt_message(encrypted_message, key)

print("\nDecrypted message:")
print(decrypted)

receiver.close()