from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Create the cipher object
key = load_key()
cipher = Fernet(key)

# Encrypt message
def encrypt_message(message):
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()
