def get_biggest_profit(array):
	return max(array) - min(array)

def find_sum_numbers(array,total):
	result = []
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] + array[j] == total and [array[j],array[i]] not in result:
				result.append([array[i],array[j]])
	return result

def frequency_sort(array):
	


if __name__ == '__main__':
	print get_biggest_profit([3,45,76,23,54])
	print find_sum_numbers([1,2,3,4,5,6,7,8,9],10)
	print frequency_sort([3,2,3,4,5,3,6,4,4,4])