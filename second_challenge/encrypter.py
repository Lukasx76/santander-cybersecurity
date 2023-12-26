# Fernet is an encryptation algorithm
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("filekey.txt", "wb") as filekey:
    filekey.write(key)

# opening the key
with open("filekey.txt", "rb") as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open("test.txt", "rb") as file:
    original_file = file.read()


# encrypting the file
file_encrypted = fernet.encrypt(original_file)

# opening the file in write mode and
# writing the encrypted data
with open("test.txt", "wb") as encrypted_file:
    encrypted_file.write(file_encrypted)
