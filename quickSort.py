#version1
quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
	[item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
	[item for item in array[1:] if item > array[0]])


#version2
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


#version3
def quick_sort(array, l, r):
	if l < r:
		q = partition(array, l, r)
		quick_sort(array, l, q - 1)
		quick_sort(array, q + 1, r)


def partition(array, l, r):
	x = array[r]
	i = l - 1
	'''
	i从左边开始，依次指向应该移向右侧的元素，然后从该元素的往后寻找，
	找到第一个应该在左侧的元素即为j指向的元素，然后将两者互换
	只需要一趟遍历，即可完成一次二分
	i最终停在比target小的最后一个元素的位置上
	'''
	for j in range(l, r):
		if array[j] <= x:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i + 1], array[r] = array[r], array[i + 1]
	return i + 1


#version4 非递归实现
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])



