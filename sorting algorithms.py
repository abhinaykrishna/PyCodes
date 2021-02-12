# # Bubble Sort

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

length = len(numbers)

def bubbleSort(num):
	count = 0
	for i in range(length-1):
		for j in range(i+1,length):
			if num[i] > num[j]:
				num[i],num[j] = num[j],num[i]
				count+=1

	print('Total comparisons is {}'.format(count))

bubbleSort(numbers)

#---------------------------------------------------------

numbers1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Selection Sort

def selectionSort(num):
	count = 0
	for i in range(len(num)-1):
		smallest = num[i]
		smallest_index = i
		for j in range(i+1,len(num)):
			count+=1
			if smallest > num[j]:
				smallest = num[j]
				smallest_index = j

		if smallest_index != i:
			num[smallest_index],num[i] = num[i],num[smallest_index]

	print(num,'comparisons made here - {}'.format(count))
	
selectionSort(numbers1)

#---------------------------------------------------------

numbers2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Insertion Sort

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]
        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
    return list_a

insertion_sort(numbers2)


#---------------------------------------------------------

numbers3 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def mergeSort(num):
	if len(num) == 1:
		return num
	else:
		midpoint = int(len(num)/2)
		left_list,right_list = mergeSort(num[:midpoint]),mergeSort(num[midpoint:])

	return merge(left_list,right_list)

def merge(left,right):

	result = []
	left_index = right_index = 0
	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index+=1
		else:
			result.append(right[right_index])
			right_index+=1

	result.extend(left[left_index:])
	result.extend(right[right_index:])
	return result

mergeSort(numbers3)

#---------------------------------------------------------

numbers4 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def quickSort(num):

	if len(num) <= 1:
		return num
	else:
		pivot = num.pop()

	lower_than_pivot = []
	greater_than_pivot = []

	for item in num:
		if item > pivot :
			greater_than_pivot.append(item)
		else:
			lower_than_pivot.append(item)

	return quickSort(lower_than_pivot) + [pivot] + quickSort(greater_than_pivot)

sortedArray = quickSort(numbers4)
print(sortedArray)


#--------------------------------------------------------