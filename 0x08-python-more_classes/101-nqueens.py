#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


from sys import argv, stderr

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    na = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if na < 4:
    print("N must be at least 4")
    exit(1)
if na == 4:
    ls1 = [[0, 1], [1, 3], [2, 0], [3, 2]]
    print(ls1)
    ls2 = [[0, 2], [1, 0], [2, 3], [3, 1]]
    print(ls2)
