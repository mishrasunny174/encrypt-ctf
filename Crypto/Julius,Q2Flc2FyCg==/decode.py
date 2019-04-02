#!/usr/bin/env python

flag = ""
ciphertext = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==".decode('base64')
for char in ciphertext:
    flag += chr(ord(char) - 24)

print flag
