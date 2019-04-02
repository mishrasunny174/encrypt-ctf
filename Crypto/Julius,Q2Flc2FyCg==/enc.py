#!/usr/bin/env python

flag = "encryptCTF{3T_7U_BRU73?!}"
#flagb64 = flag.encode('base64') <-- not used 
ciphertext = ""
for char in flag:
    ciphertext += chr(ord(char) + 24)

print ciphertext.encode('base64')
