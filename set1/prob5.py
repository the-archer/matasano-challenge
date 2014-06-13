import sys
import xor
import convert
import binascii


f1 = open("input5.txt", "r")

s = f1.read()

k = input("Enter key:")

s=s.encode("utf-8")

k = k.encode("utf-8")
p = xor.xor(s, k)
p = binascii.hexlify(p)
print (p)
f2 = open("output5.txt", "w")
f2.write(str(p))
f2.close()
f1.close()