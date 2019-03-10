#!/usr/bin/env python2
from pwn import *

HOST = "localhost"
PORT = 7777
local = False

if local:
    p = process("./crackme02");
else:
    p = remote(HOST,PORT)

print p.recvuntil("Enter input #0: ")
p.sendline("CRACKME02")
print p.recvuntil("Enter input #1: ")
p.sendline(p32(0xdeadbeef))
print p.recvuntil("Enter input #2: ")
p.sendline("ZXytUb9fl78evgJy3KJN")
print p.recvuntil("Enter input #3: ")
p.sendline("1")
print p.recvuntil("Enter input #4: ")
p.sendline("pewdiepie")
print p.recvall()
