#!/usr/bin/python3
import base64
from Crypto.Cipher import AES
import glob

key = "besthacker@@@@@@"

def decrypt_ranso(arq, key):
    f = open(arq, "rb").read()
    aes = AES.new(key , AES.MODE_ECB)
    try:
       decrypt = aes.decrypt(f)
       nd = decrypt.decode().rstrip("@")
       origi = base64.b64decode(nd)
    
       f = open(arq, "wb")
       f.write(origi)
       f.close()
       print("%s descriptografado.." % (arq))
    except:
       print("Arquivo comum..")
lista = glob.glob("*.txt")
for i in range(0,len(lista)):
    arq = lista[i]
    decrypt_ranso(arq, key)
