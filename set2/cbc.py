from Crypto.Cipher import AES
import padding
import sys
sys.path.insert(0, '../set1')
import xor

def decrypt(ciptext, key, iv):
	obj2 = AES.new(key, AES.MODE_ECB)
	prev_cipblock=iv
	ptext=bytearray()
	for x in range(0, len(ciptext), 16):
		cipblock=ciptext[x:(x+16)]
		#if len(cipblock)<16:
		#	cipblock=padding.padding(cipblock, 16)
		#a = cipblock.decode('Utf-8')
		a = obj2.decrypt(bytes(cipblock))
		#print (a)
		a = xor.xor(a, prev_cipblock)
		#a=a.decode('UTF-8')
		ptext+=a
		#print(a)
		x+=16
		prev_cipblock=cipblock
		#f=input()

	
	return ptext


def encrypt(ptext, key, iv):
	obj2 = AES.new(key, AES.MODE_ECB)
	prev_cipblock=iv
	ciptext=bytearray()
	#print (len(ptext))
	for x in range(0, len(ptext), 16):
		#print (x)
		pblock=ptext[x:(x+16)]
		if len(pblock)<16:
			pblock=padding.padding(pblock, 16)

		a = xor.xor(pblock, prev_cipblock)
		#a = a.decode('UTF-8')
		b = obj2.encrypt(bytes(a))
		#print (b)
		#a = xor.xor(a, prev_cipblock)
		#a=a.decode('UTF-8')
		ciptext+=b
		#print(b)

		prev_cipblock=b
		#f=input()
		
	
	return ciptext
