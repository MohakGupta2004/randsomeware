import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file=="encrypt.py" or file=='decrypt.py' or file=='TheKey.key':
        continue
    if os.path.isfile(file):
        files.append(file)

with open('TheKey.key','rb') as key:
    secret_key=key.read()

for file in files:
    with open(file,'rb') as theFile:
        contents=theFile.read()
    contents_decryption = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as decrypted_file:
        decrypted_file.write(contents_decryption)
