
def binary_search(array,element):
	low = 0
	high = len(array) - 1 

	while low <= high:
		mid = (low+high)/2
		if array[mid] < element:
			low = mid + 1
		elif array[mid] > element:
			high = mid - 1
		else:
			return mid
	return False

if __name__ == '__main__':
	array = [1,2,3,4,5]
	print binary_search(array,6)
