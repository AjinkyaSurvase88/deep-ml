def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    result=[]
    # for i in a:
    #     arr=[]
    #     k=0
    #     for j in range(len(i)):
    #         arr.append(i[k])
    #     k+=1
    #     result.append(arr)

    # return result
    k=0
    for i in range(len(a[0])):
        arr=[]
        
        for i in range(len(a)):
            arr.append(a[i][k])
        k+=1
        result.append(arr)
    return result



    pass