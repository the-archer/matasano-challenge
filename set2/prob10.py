from Crypto.Cipher import AES
import base64
import cbc
f1 = open("gistfile10.txt", "r")


bigstring=bytes()
for  line in f1:
	line = base64.b64decode(line.rstrip('\n'))
	#line = line.decode('UTF-8')
	bigstring += line

f1.close()

key = ("YELLOW SUBMARINE").encode('UTF-8')

iv = bytes(16)
#print (bigstring)
print (len(iv))


cbc.decrypt(bigstring, key, iv)




