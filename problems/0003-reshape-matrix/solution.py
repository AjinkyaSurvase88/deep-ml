def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    result = []
    mid = []

    # Flatten the matrix
    for row in a:
        for value in row:
            mid.append(value)

    # Check if reshaping is possible
    if len(mid) != new_shape[0] * new_shape[1]:
        return []

    no = 0

    # Create the new matrix
    for i in range(new_shape[0]):
        dummy = []

        for j in range(new_shape[1]):
            dummy.append(mid[no])
            no += 1

        result.append(dummy)

    return result

