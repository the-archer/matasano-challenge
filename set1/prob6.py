import sys
import xor
import convert
import binascii
import hamming
import prob3
import base64


f1 = open("gistfile6.txt", "r")

bigstring=""
for  line in f1:
	line = base64.b64decode(line.rstrip('\n'))
	line = line.decode('UTF-8')
	bigstring += line
	
f1.close()

#print (bigstring)
#sim = input()
minned=[]
ksize=[]
for keysize in range(2, 41):
	ed1 = hamming.getHammingDistance(bigstring[0:keysize], bigstring[keysize:(2*keysize)])
	ed2 = hamming.getHammingDistance(bigstring[(2*keysize):(3*keysize)], bigstring[(3*keysize):(4*keysize)])
	ed3 = hamming.getHammingDistance(bigstring[(4*keysize):(5*keysize)], bigstring[(5*keysize):(6*keysize)])
	ed4 = hamming.getHammingDistance(bigstring[(6*keysize):(7*keysize)], bigstring[(7*keysize):(8*keysize)])
	ned = float((ed1+ed2))/(4*keysize)
	print (ned) 		
	minned.append(ned)
	ksize.append(keysize)

ksize = [x for (y, x) in sorted(zip(minned, ksize))]	
print(ksize)

no_of_values=int(input("Enter no. of least values to check:"))



for x in range(0, no_of_values):
	keysize = ksize[x]
	blocks=[]
	keys=[]
	dev=0
	flag=0
	for i in range(0, keysize):
		blocks.append("")
		for j in range(i, len(bigstring), keysize):
			blocks[i]+=bigstring[j]
		s=(blocks[i]).encode('UTF-8')
		#s=binascii.unhexlify(blocks[i])
		tup=prob3.getSingleXORKey(s)
		#print (len(tup))
		if(tup[1]==-1):
			flag=1
			print ("Failed : "+ str(keysize))
			break
		keys.append(tup[1])
		dev+=tup[2]
		
	


	if flag==1:
		continue
	
	
	ans=xor.xor((bigstring.encode('UTF-8')), keys)

	dev = float(dev)/keysize

	ans=ans.decode('UTF-8')
	#print (ans)
	print (keysize)
	print(keys)
	print (dev/keysize)
	




