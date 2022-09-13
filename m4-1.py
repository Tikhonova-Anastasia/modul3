
def binary_search(lst, serch):
	left = 0
	right = len(lst) - 1
	
	while left <= right:
		mid = (left + right) // 2
		if lst[mid] == serch:
			return mid
		elif lst[mid] > serch:
			right = mid - 1
		else:
			left = mid + 1
	
	return None

lst = [3, 8, 9, 11, 15, 42, 13, 18, 55, 36, 2, 19]
serch = int(input('Введите число: ')) 
print(binary_search(lst, serch))	