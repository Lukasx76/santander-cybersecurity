from cryptography.fernet import Fernet

with open("filekey.txt", "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("test.txt", "rb") as encrypted_file:
    file_to_decrypt = encrypted_file.read()

with open("test.txt", "wb") as decrypted_file:
    decrypted_file.write(fernet.decrypt(file_to_decrypt))
