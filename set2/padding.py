def padding(b, l):
	b= bytearray(b)
	num = l - len(b)
	for x in range(0, num):
		b.append(num)
	return b
