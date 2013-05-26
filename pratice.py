
test = [[1,1,0,0,1],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,1],[1,0,0,1,1]]
test_transfer = []

def matrix_trasfer(origin, transfer):	
	for i in range(len(origin)):
		transfer.append([])
		for j in range(len(test)):
			transfer[i].append(origin[j][i])

	print test_transfer


def matrix_multi(origin, transfer):
	result_matrix = []
	total = 0
	for k in range(len(origin)): # k = origin_row
		result_matrix.append([])
		for i in range(len(origin)): # i = transfer_row
			for j in range(len(origin[0])): # j = origin&transfer_col
				total = total + origin[k][j]*transfer[i][j] 

			result_matrix[k].append(total)
			total = 0
	print result_matrix


matrix_trasfer(test, test_transfer)
matrix_multi(test, test_transfer)
