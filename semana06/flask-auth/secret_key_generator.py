from cryptography.fernet import Fernet
import secrets
import base64

key = Fernet.generate_key()
print(key.decode())

secret_key = base64.urlsafe_b64encode(secrets.token_bytes(32))
print(secret_key.decode())