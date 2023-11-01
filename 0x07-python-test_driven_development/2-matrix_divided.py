#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


def matrix_divided(matrix, div):
    """ commenttttttttttttttttttttttttttttt """
    newmat = []
    newlist = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for ln in range(1, len(matrix)):
        if len(matrix[ln]) != len(matrix[ln - 1]):
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                a = "matrix must be a matrix"
                b = " (list of lists) "
                c = "of integers/floats"
                raise TypeError(a + b + c)
            newlist.append(round((j / div), 2))
        newmat.append(newlist)
        newlist = []
    return newmat
