import socket
from crypto_utils import encrypt_message

HOST = "127.0.0.1"
PORT = 5000

# Load shared secret key
with open("shared_key.bin", "rb") as file:
    key = file.read()


# Get message
message = input("Enter your message: ")

# Encrypt message
encrypted = encrypt_message(message, key)

print("\nEncrypted message:")
print(encrypted)

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Identify as sender
client.sendall(b"SENDER")

# Send encrypted message
client.sendall(encrypted.encode())

print("\nEncrypted message sent to server.")

client.close()
