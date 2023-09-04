def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""

    if not matrix:
        print()
        return

    for row in matrix:
        for num in row:
            print(f"{num:d}", end=" ")
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)
