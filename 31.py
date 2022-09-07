x = int(input())
p = int(input())
y = int(input())

s = x * (p/100)
years = 100

while x < y:
	x = round(x+s, 2)
	years += 1
print(years)