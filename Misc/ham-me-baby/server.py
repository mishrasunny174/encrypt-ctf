#!/usr/bin/python
import numpy as np
import random

G=np.array([1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1]).reshape(7,4)

intro = r'''
                        Welcome To 

     ____                       __    _______________  
    / __/__  __________ _____  / /_  / ___/_  __/ __/  
   / _// _ \/ __/ __/ // / _ \/ __/ / /__  / / / _/    
  /___/_//_/\__/_/  \_, / .__/\__/  \___/ /_/ /_/      
                ___/___/_/_____                        
               |_  |/ _ <  / _ \                       
              / __// // / /\_, /                       
             /____/\___/_//___/                        
                                                         

you will be receiving hamming(7,4) codes. your job is to send data bits
from a 7 bit hamming code. 
 ___________________________________________________________________
|                                                                   |
|   DO YOUR RESEARCH : https://en.wikipedia.org/wiki/Hamming(7,4)   |
|  FLAG WILL BE PRINTED AFTER YOU SEND CORRECT DATA BITS 100 TIMES  |
|___________________________________________________________________|

               the order of the bits followed is

                    P1 P2 D3 P4 D5 D6 D7


and come back here. remember somebits could be flipped. you need to send
correct data bits.
'''

def generate_code():
  num = np.array([int(a) for a in bin(random.randint(0,15))[2:].zfill(4)])
  return num

print intro
ok=1
for i in range(100):
  n = generate_code()
  hamming_code_n = np.matmul(G,n)%2
  if(random.random()>0.5):
    bit = random.randint(0,6)
    hamming_code_n[bit]^=1

  print "[*] CODE:",''.join(str(a) for a in list(hamming_code_n))

  ask = str(raw_input("[*] DATA: ")).strip()
  check=0
  if(len(ask)==4):
    if(len(set(ask))==2 and ('0' in set(ask) and '1' in set(ask))):
      check=1
    elif(len(set(ask))==1 and ('0' in set(ask) or '1' in set(ask))):
      check=1

  if not check:
    print 'Invalid Input! Aborting!'
    ok=0
    break
  
  if ask == ''.join(str(a) for a in list(n)):
    print "CODE VALIDATED"
  else:
    print "Wrong Answer! Aborting!"
    ok=0
    break

if ok:
  print "here's your flag: encryptCTF{1t_w4s_h4rd_th4n_1_th0ught}"

