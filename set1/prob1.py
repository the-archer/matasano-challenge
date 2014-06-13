import sys
import convert
import binascii
import base64

#barray = bytearray()
#barray = input("Enter string:").encode(encoding='UTF-8')
#print (barray)
#print (type(barray))

#bbyytes = bytes()
#s=input("Enter hex string:")
s="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b=binascii.unhexlify(s)
print (b)
r = base64.b64encode(b)
print (r)
t = base64.b64decode(r)
print (t)
l = binascii.hexlify(t)
print (l)
# r = convert.binarytobase64(barray)
# print (r)
# t = convert.base64tohex(r)
# print (t)
