import binascii
import padding

s = input("Enter string:")
l = int(input("Enter no of bytes to pad up to:"))

barray = s.encode(encoding='UTF-8')
b= bytearray(barray)
print (type(b))
print (b)
b=padding.padding(b, l)
print (b)