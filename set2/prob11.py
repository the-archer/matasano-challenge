import misc

inp = "A"*1000


cip = misc.encryption_oracle(inp)

count=0
for x in range(0, len(cip)):
	for j in range(x+16, len(cip), 16):
		if cip[x:x+16]==cip[j:j+16]:
			count+=1

print(count)
if count>0:
	print ("ECB")
else:
	print("CBC")