from pwn import *
#context.log_level="debug"

p = remote("127.0.0.1",5004)



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
	
	return list(data[:4])

output = ""
i=0
#print p.recv(100)
while i<100:
	
	codel = p.recvuntil("CODE: ")
	#print "code recieved"
	code = p.recv(7)
	bits = p.recvuntil("DATA: ")
	out = "".join(data_print(code))
	#print "==========\nout: {}\n=========".format(out)

	p.sendline(out)
	#correct = p.recvuntil("correct")
	#print correct
	output+=codel
	#output+=correct
	output+=bits
	i+=1
	log.info("sent "+out+" for code: "+code)


print p.recvall()
