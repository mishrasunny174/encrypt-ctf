#!/usr/bin/env python


#hamming code challenge

import random


intro = '''

Welcome To Encrypt CTF 2019

you will be provided a 7 bit hamming code with 4 bits as Data bit 
and remaining 3 bits are parity bits and are used to detect error.
hamming code can detect 1 bit of error and correct it.
for Ex: 1001001 
its a 7 bit code

left most bit is most significant bit
and 1st,2nd,3rd and 5th bit from left are DATA bits and 1st, 2nd 
and 4th bit from right are parity bit. you will be provided by 
several hamming codes and your job is to send DATA bits from the
hamming code

REMEMBER Sometimes some bits may be flipped. you need to recognise
correct the error and then send the Data Bits.

AND WE FOLLOW EVEN PARITY AND WE WILL ASK IT 100 TIMES'''
print intro

print "\n"


def generate_code():
	num = bin(random.randint(64,127))[2:]
	#print len(num)
	#print num,type(num)

	
	return num

def data_print(code):
	code = list(code)
	data = []
	#1001001
	#DDDPDPP
	#7654321
	p1 = int(code[0])+int(code[2])+int(code[4])+int(code[6]) #1 3 5 7
	p2 = int(code[5])+int(code[4])+int(code[1])+int(code[0]) #2 3 6 7
	p4 = int(code[3])+int(code[2])+int(code[1])+int(code[0]) #4 5 6 7

	#print "p1: ",p1
	#print "p2: ",p2
	#print "p4: ",p4
	error = False
	p1_error = False
	p2_error = False
	p4_error = False 


	#for even parity
	if(p1%2!=0):
		error = True
		p1_error = True
	if(p2%2!=0):
		error = True
		p2_error = True
	if(p4%2!=0):
		error = True
		p4_error = True
	else:
		data += code[0]
		data += code[1]
		data += code[2]
		data += code[4]

	#print "error: ",error
	#print "p1_error: ",p1_error
	#print "p2_error: ",p2_error
	#print "p4_error: ",p4_error

	if(error):
		if(p1_error and (p2_error and (p4_error))):
			code[0] = str(int( not int(code[0])))
		elif(p1_error and (p2_error and ( not p4_error ))):
			code[5] = str(int( not int(code[5])))
		elif(p1_error and (not p2_error and (p4_error))):
			code[2] = str(int( not int(code[2])))
		elif(p1_error and (not p2_error and ( not p4_error))):
			code[6] = str(int( not int(code[6])))
		elif(not p1_error and (p2_error and (p4_error))):
			code[1] = str(int( not int(code[1])))
		elif(not p1_error and ( p2_error and ( not p4_error))):
			code[5] = str(int( not int(code[5])))
		elif(not p1_error and (not p2_error and (p4_error))):
			code[4] = str(int( not int(code[4])))
		else:
			data += code[0]
			data += code[1]
			data += code[2]
			data += code[4]
		data += code[0]
		data += code[1]
		data += code[2]
		data += code[4]
	
	return list(data)


i=0
for j in range(100):
	n = generate_code()
	print "hamming code:",n
	print "enter data bits: "
	ask = raw_input()
	real = data_print(n)
	realdata = "".join(real)
	if ask == realdata:
		print "correct"
		i+=1
		
	#print "i: " ,i
	#print "list of data: ",real
	#print "data as string: ",realdata
	#print "user input",ask
	if i==100:
		break
	real = []
	realdata = ""
	ask = ""
print "encryptCTF{hummmmm_hummmmmm}"
















