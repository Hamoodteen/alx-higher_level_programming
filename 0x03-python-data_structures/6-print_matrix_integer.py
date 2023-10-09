#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        li = len(matrix[i])
        for j in range(li):
            print("{:d}".format(matrix[i][j]), end=" " if j != li - 1 else "")
        print()
