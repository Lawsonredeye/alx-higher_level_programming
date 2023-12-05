#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in range(len(matrix)):
        row_as_str = []
        for j in range(len(matrix[i])):
            row_as_str.append(str(matrix[i][j]))
        print(" ".join(row_as_str))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
