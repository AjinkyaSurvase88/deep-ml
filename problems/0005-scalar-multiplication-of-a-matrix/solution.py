def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result=[]

	for i in matrix:
		list1=[]
		for j in i:
			list1.append(j*scalar)
		result.append(list1)

	return result