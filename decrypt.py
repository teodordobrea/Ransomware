import os
from cryptography.fernet import Fernet

starting_path = "./files_to_encrypt"
files = []

for file in os.listdir(starting_path):
    if os.path.isfile(os.path.join(starting_path,file)):
        files.append(file)



with open("the_key.key", "rb") as key:
    secret_key = key.read()

for file in files:
    with open(os.path.join(starting_path,file), "rb") as the_file:
        contents = the_file.read()

    contents_decrypted = Fernet(secret_key).decrypt(contents)
    
    with open(os.path.join(starting_path,file), "wb") as the_file:
        the_file.write(contents_decrypted)

print(f"All the files in the path {starting_path} have been decrypted.")
