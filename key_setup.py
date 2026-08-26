from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)

with open("shared_key.bin", "wb") as file:
    file.write(key)

print("Secret key generated successfully.")