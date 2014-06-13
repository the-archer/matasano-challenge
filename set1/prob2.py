import sys
import convert
import xor
import binascii

a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
a = binascii.unhexlify(a)
b = binascii.unhexlify(b)
c = xor.xor(a, b)
#c = convert.binarytohex(c)
print (binascii.hexlify(c))