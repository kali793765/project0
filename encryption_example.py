from cryptography.fernet import Fernet
# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
original_message = b"Secret Data"
encrypted_message = cipher.encrypt(original_message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print(f"Original: {original_message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")