def binary_search(list, item):
	low = 0                       
	high = len(list) - 1
	#low和high用于追踪要在其中查找的列表部分	
	while low <= high:   #只要范围没有缩小到只包含一个元素就检查中间的元素
		mid = (low  + high) // 2
		guess = list[mid]
		if guess == item:   #找到了元素
			return mid
		if guess > item:   #猜大了
			high = mid - 1
		else:
			low = mid + 1  #猜大了
	return None


my_list = [1,2,3,4,5]

print(binary_search(my_list, 3))