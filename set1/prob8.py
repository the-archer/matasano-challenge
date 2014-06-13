

f1 = open("gistfile8.txt", "r")
i=0
st=0
for line in f1:
	i+=1
	line = line.rstrip('\n')
	for x in range(0, len(line), 32):
		for j in range(x+32, len(line), 32):
			if line[x:x+32]==line[j:j+32]:
				print (line[x:x+32])
				print (i)
				st=i

	if st!=0:
		print (line)
		st=0			
f1.close()
