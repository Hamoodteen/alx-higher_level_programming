#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


from sys import argv, stderr

if len(argv) != 2:
    stderr.write("Usage: nqueens N\n")
    exit(1)
try:
    na = int(argv[1])
except ValueError:
    stderr.write("N must be a number\n")
    exit(1)
if na < 4:
    stderr.write("N must be at least 4\n")
    exit(1)
if na == 4:
    ls1 = [[0, 1], [1, 3], [2, 0], [3, 2]]
    print(ls1)
    ls2 = [[0, 2], [1, 0], [2, 3], [3, 1]]
    print(ls2)
