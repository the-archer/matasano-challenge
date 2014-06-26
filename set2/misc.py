from Crypto.Cipher import AES
import random
import cbc
import padding

def get_random_AES_key():
	return get_random_bytes(16)


def get_random_bytes(n):
	random.seed(None)
	b = bytearray()
	for x in range(0, n):
		r = random.randint(0, 255)
		b.append(r)

	return b



def encryption_oracle(ptext):
	key=get_random_AES_key()
	random.seed(None)
	before = random.randint(5, 10)
	after = random.randint(5, 10)
	btext = get_random_bytes(before)
	btext += ptext.encode('UTF-8')
	btext += get_random_bytes(after)
	
	if(random.randint(0, 1)==0):
		if ((len(btext)%16)!=0):
			btext = padding.padding(btext, len(btext)+ 16 -(len(btext)%16))
		obj = AES.new(bytes(key), AES.MODE_ECB)
		cip = obj.encrypt(bytes(btext))
		print ("ECB")
	else:
		iv=get_random_bytes(16)
		cip = cbc.encrypt(btext, bytes(key), iv)
		print ("CBC")




	return cip


#demo changes