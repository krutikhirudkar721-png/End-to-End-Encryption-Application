from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

def generate_key():
    return AESGCM.generate_key(bit_length=256)

def encrypt_message(message, key):
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)

    ciphertext = aesgcm.encrypt(
        nonce,
        message.encode(),
        None
    )

    return base64.b64encode(nonce + ciphertext).decode()


def decrypt_message(encrypted_message, key):
    data = base64.b64decode(encrypted_message)

    nonce = data[:12]
    ciphertext = data[12:]

    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()
