import sys
import convert
a = raw_input()
a = convert.hextobinary(a)
print convert.binarytoplaintext(a)