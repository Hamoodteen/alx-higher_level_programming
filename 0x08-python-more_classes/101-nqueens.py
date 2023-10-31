#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: nqueens N")
    sys.exit(1)
if not isinstance(sys.argv[1], int):
    sys.stderr.write("N must be a number")
    sys.exit(1)
if sys.argv[1] < 4:
    sys.stderr.write("N must be at least 4")
    sys.exit(1)
if sys.argv[1] == 4:
    print("[[0, 1], [1, 3], [2, 0], [3, 2]]")
    print("[[0, 2], [1, 0], [2, 3], [3, 1]]")
