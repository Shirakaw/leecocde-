def selectionSort(arr):        #对数组排序
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)   # 找到数组最小的元素，并将其加入到新数组中
		newArr.append(arr.pop(smallest))
	return newArr