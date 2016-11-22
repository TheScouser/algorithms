def zero_matrix(matrix):
	zeroed = []
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if [i,j] not in zeroed:
				if matrix[i][j] == 0:
					zeroed.append([i,j])
	for x in zeroed:
		for i in x[0]


matrix  = [[i for i in range(0,10)] for j in range(0,10)]

zero_matrix(matrix)