l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
duplicats = []
for i in set(l):
	if l.count(i) > 1:
		duplicats.append(i)
print(duplicats)

