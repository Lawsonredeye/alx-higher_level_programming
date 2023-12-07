#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_sublist = []
        for j in i:
            new_sublist.append(j**2)
        new_matrix.append(new_sublist)
    return new_matrix
