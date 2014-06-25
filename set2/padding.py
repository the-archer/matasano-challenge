def padding(b, l):
	num = l - len(b)
	for x in range(0, num):
		b.append(num)
	return b
