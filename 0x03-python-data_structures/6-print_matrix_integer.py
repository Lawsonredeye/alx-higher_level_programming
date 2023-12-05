#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in range(len(matrix)):
        print(" ".join("{:d}".format(matrix[i][j]) for j in range(len(matrix[i]))))
