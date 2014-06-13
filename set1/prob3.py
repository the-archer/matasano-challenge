import sys
import convert
import xor
import binascii


def getSingleXORKey(s):
	freqtab={}

	frlist=[]
	f3=open("freq.txt", "r")
	for line in f3:
		words=line.split()
		
		freqtab[words[0]]=float(words[1])
		frlist.append(words[0])
	mindev=100.000
	ans=""
	store=-1
	for i in range(0,  256):
		a = bytes([i]*(int)(len(s)))
		count=0
		flag=0
		dev=0
		warn=0
		freqline={}
		freqline = freqline.fromkeys(frlist, 0)
		p = xor.xor(s, a)
		#print (p)
		try:
			p = p.decode('UTF-8')
		except Exception:

			continue
		#print (p)		
		for j in range(0, len(p)):
			c = p[j]
			if ord(c)>31:
				if c.isalpha():
					count=count+1
					freqline[c.upper()]=freqline[c.upper()]+1


						
			else:
				if(ord(c)!=10):
					warn+=1
				continue
				#break
				



		if flag==0:
			if(count<=0):
				continue
			for key in freqline:
				

				freqline[key]=float(freqline[key])/float(count)
				dev =  dev + abs(freqline[key]-freqtab[key])
		

			dev = dev/float(count)
			dev += warn
			#print (dev)
			#print (i)
			if dev < mindev:
				ans = p
				mindev=dev	
				store=i
	f3.close()
	#print (mindev)
	return (ans, store, mindev)


if __name__ == "__main__":

	f2 = open("input3.txt", "r")
	s = f2.readline()
	s = binascii.unhexlify(s)
	tup=getSingleXORKey(s)
	f2.close()




	print (tup[0])
	print ("Key = "+ chr(tup[1]))
	print(tup[2])


