#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = len(matrix)
    for i in range(l):
        for j in range(l):
            print("{:d}".format(matrix[i][j]), end=" " if j != l - 1 else "")
        print()
