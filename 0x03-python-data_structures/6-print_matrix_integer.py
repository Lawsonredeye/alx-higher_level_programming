#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat = matrix
    if not mat:
        return None
    for i in range(len(mat)):
        print(" ".join("{:d}".format(mat[i][j]) for j in range(len(mat[i]))))
