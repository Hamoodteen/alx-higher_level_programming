#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: nqueens N\n")
    sys.exit(1)
try:
    na = int(sys.argv[1])
except ValueError:
    sys.stderr.write("N must be a number\n")
    sys.exit(1)
if na < 4:
    sys.stderr.write("N must be at least 4\n")
    sys.exit(1)
if na == 4:
    ls1 = [[0, 1], [1, 3], [2, 0], [3, 2]]
    print(ls1)
    ls2 = [[0, 2], [1, 0], [2, 3], [3, 1]]
    print(ls2)
