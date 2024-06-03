import os
from cryptography.fernet import Fernet

starting_path = "./files_to_encrypt"
files = []

for file in os.listdir(starting_path):
    if os.path.isfile(os.path.join(starting_path,file)):
        files.append(file)


key = Fernet.generate_key()

with open("the_key.key", "wb") as the_key:
    the_key.write(key)

for file in files:
    with open(os.path.join(starting_path,file), "rb") as the_file:
        contents = the_file.read()

    contents_encrypted = Fernet(key).encrypt(contents)
    
    with open(os.path.join(starting_path,file), "wb") as the_file:
        the_file.write(contents_encrypted)

print(f"All the files in the path {starting_path} have been encrypted.")