from Crypto.Cipher import AES
import padding
import sys
sys.path.insert(0, '../set1')
import xor

def decrypt(ciptext, key, iv):
	obj2 = AES.new(key, AES.MODE_ECB)
	prev_cipblock=iv
	ptext=""
	for x in range(0, len(ciptext)):
		cipblock=ciptext[x:(x+16)]
		if len(cipblock)<16:
			cipblock=padding.padding(cipblock, 16)

		a = obj2.decrypt(cipblock)
		a = xor.xor(a, prev_cipblock)
		ptext+=a
		print(a)
		x+=16
		prev_cipblock=cipblock

	
	return ptext