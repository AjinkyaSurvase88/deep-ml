def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result=[]
	if mode=='column':
		
		for i in range(len(matrix[0])):
			res1=0
			sum1=0
			for j in range(len(matrix)):
				sum1+=matrix[res1][i]
				res1+=1
			result.append(sum1/len(matrix))
	else:
		for i in matrix:
			result.append(sum(i)/len(i))
	return result

