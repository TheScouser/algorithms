def rotate_matrix(matrix):
	size = len(matrix)
	for i in range(size / 2):
		for j in range(i,size-i-1):
			top = matrix[i][j]
			matrix[i][j] = matrix[j][size-i-1]
			matrix[j][size-i-1] = matrix[size-i-1][size-j-1]
			matrix[size-i-1][size-j-1] = matrix[size-j-1][i]
			matrix[size-j-1][i] = top

	return matrix

matrix  = [[i for i in range(10)] for j in range(10)]

print rotate_matrix(matrix)