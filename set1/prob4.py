import sys
import convert
import xor
import binascii


freqtab={}
frlist=[]
f3=open("freq.txt", "r")

for line in f3:
	words=line.split()
	
	freqtab[words[0]]=float(words[1])
	frlist.append(words[0])
mindev=100.000
ans=""

f2 = open("gistfile4.txt", "r")
store=0
lineno=0
linecur=0
for line in f2:
	linecur+=1
	line = line.rstrip('\n')
	#print line
	#k = raw_input()
	s = binascii.unhexlify(line)
	#print (s)
	for i in range(0,  256):
		a = bytes([i]*(int)(len(s)))
		count=0
		flag=0
		dev=0
		freqline={}
		freqline = freqline.fromkeys(frlist, 0)
		p = xor.xor(s, a)
		try:
			p = p.decode("utf-8")
			
		except Exception:
			#print ("Here")
			continue
		#print p
		#print (p)
		for j in range(0, len(p)):
			c = p[j]
			if ord(c)>31 and ord(c)<127 or ord(c)==10:
				if c.isalpha():
					count=count+1
					freqline[c.upper()]=freqline[c.upper()]+1


					
			else:
				flag=1
				break		



		if flag==0:
			
			for key in freqline:
				if count>0:
					freqline[key]=float(freqline[key])/float(count)
				dev =  dev + abs(freqline[key]-freqtab[key])
			
			
			dev = dev/float(count)
		
			if dev < mindev:

				ans = p
				mindev=dev	
				store=i
				lineno=linecur




print (ans)
print ("Line : "+str(lineno))
print ("Key = "+ chr(store))
print (mindev)

f2.close()
f3.close()