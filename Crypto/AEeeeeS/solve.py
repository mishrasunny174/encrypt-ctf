#!/usr/bin/env python

from Crypto.Util.number import *
from Crypto.Cipher import AES

key = '110100001010100111001101110001011101000010100000110001001101100010100101100010011110010111010001100101011010110110010101111001'

ciphertext = 'c68145ccbc1bd6228da45a574ad9e29a77ca32376bc1f2a1e4cd66c640450d77'

ciphertext = ciphertext.decode('hex')

flag = ''

original_key = long_to_bytes(int(key,2))

cipher = AES.new(original_key,AES.MODE_ECB)

flag = cipher.decrypt(ciphertext)

print flag
