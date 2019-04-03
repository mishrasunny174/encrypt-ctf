from pwn import *
context.log_level = "debug"
import numpy as np
def readjunk(x):
  for i in range(x):
    print s.recvline().strip()

H=np.array([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]])
R=np.array([[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
print H
print R

s=remote("104.154.106.182", 6969)
readjunk(29)

for i in range(100):
  a=s.recvline().strip()
  print a
  c=a.split()[-1]
  c=np.array([int(a) for a in c])
  r=np.matmul(H,c)%2
  x= int(''.join(str(a) for a in reversed(r)),2)
  if(x):
    c[x-1]^=1
  p=np.matmul(R,c)%2
  o= ''.join(str(a) for a in p)
  print o
  s.sendline(o)
  print s.recvline().strip()
print s.recv()
