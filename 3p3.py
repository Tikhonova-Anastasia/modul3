def large(arr):
	max_ = arr[0]
	for ele in arr:
		if ele > max_:
			max_ = ele
	return max_
list1 = [56, 9, 11, 2]
result = large(list1)
print(result)