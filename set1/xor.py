


def xor(a, b):
	d=bytearray()
	for x in range(0, len(a)):
		d.append(a[x]^b[x%len(b)])

	return d