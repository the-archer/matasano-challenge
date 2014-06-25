import binascii


def decimaltobinary(s, fl): # fl is padding 
	r=bin(s)[2:].zfill(fl)
	return r

def plaintexttobinary(s):
	r=""
	for i in range(0, len(s)):
		r = r + decimaltobinary(ord(s[i]), 8)
	return r


def binarytoplaintext(s):
	r=""
	for i in range(0, len(s), 8):
		r = r + chr(int(s[i:i+8], 2))

	return r

def hextobinary(barray):
	
	return binascii.unhexlify(barray)

def binarytohex(s):
	r=""
	for i in range(0, len(s), 4):
		temp = int(s[i:i+4], 2)
		if(temp<10):
			r = r + str(temp)
		else:
			r = r + chr(temp+87)

	return r

def base64tobinary(s):
	r=""
	for c in s:
		if ord(c)>=65 and ord(c)<=90:
			r = r + bin(ord(c)-65)[2:].zfill(6)
		elif ord(c)>=97 and ord(c)<=122:
			r = r + bin(ord(c)-71)[2:].zfill(6)
		elif ord(c)>=48 and ord(c)<=57:	
			r = r + bin(ord(c)+4)[2:].zfill(6)
		elif c=='+':
			r = r + bin(62)[2:].zfill(6)
		else:
			r = r + bin(63)[2:].zfill(6)

	return r

def binarytobase64(barray):
	
	
	return r

def hextobase64(barray):
	r = hextobinary(barray)
	print (r)
	t = binarytobase64(r)
	return t


def base64tohex(s):
	r = base64tobinary(s)
	t = binarytohex(r)
	return t


def hexstringtobytearray(s):
	barray=bytearray()
	for x in range(0, len(s), 2):
		barray.append(int(s[x:(x+2)], 16))

	return barray


