import cbc

inp = "Yellow Submarine is cool"
key= ("YELLOW SUBMARINE").encode('UTF-8')
iv = bytes(16)
ip = inp.encode('UTF-8')
a = cbc.encrypt(ip, key, iv)

print (a)

b = cbc.decrypt(a, key, iv)

print (b)
