#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat2 = [row[:] for row in matrix]
    for i in range(len(mat2)):
        for j in range(len(mat2[i])):
            mat2[i][j] *= mat2[i][j]
    return mat2
