
from Crypto.Cipher import AES
import base64
f1 = open("gistfile7.txt", "r")

bigstring=bytes()
for  line in f1:
	line = base64.b64decode(line.rstrip('\n'))
	#line = line.decode('UTF-8')
	bigstring += line

f1.close()
print (len(bigstring)%16)
obj2 = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
a = obj2.decrypt(bigstring)
print (a.decode('UTF-8'))
