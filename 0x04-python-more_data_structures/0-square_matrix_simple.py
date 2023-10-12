#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat2 = matrix.copy()
    for i in mat2:
        for j in mat2[i]:
            mat2[i][j] *= matrix[i][j]
    return mat2
