from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
import os

flag = open("flag.txt",'r')

p = getPrime(128)
q = getPrime(128)
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)

message = bytes_to_long(flag.read())

ciphertext = pow(message,e,n)
ciphertext = long_to_bytes(ciphertext).encode('hex')
encrypt = open("flag.enc",'w')

encrypt.write("ciphertext: \n" + ciphertext)
encrypt.close()
flag.close()
pubkeyfile = open("pubkey.pem",'w')
pubkey = RSA.construct([long(n), long(e)])
pubkeyfile.write(pubkey.exportKey('PEM'))
pubkeyfile.close()
