def getHammingDistance(s1, s2):
	x=s1.encode("utf-8")
	y=s2.encode("utf-8")
	dis=0

	ff=255
	for i in range(0, max(len(x), len(y))):
		a=0
		b=0
		if i < len(x):
			a=x[i]
		if i < len(y):
			b=y[i]
		val =a^b
		while(val):
			dis+=1
			val &=val-1

	return dis
	