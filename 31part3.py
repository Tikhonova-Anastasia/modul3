def area(a, b, c):
	p = (a + b +c) / 2
	return(p * (p-a)*(p-b)*(p-c)) ** 0.5
s = area(3, 2, 4)
print(s)
