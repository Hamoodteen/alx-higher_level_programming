#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv)
    if l == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(l - 1) if l > 2 else "1 argument:")
        for i in range(1, l):
            j = argv[i]
            print("{:d}: {}".format(i, j))
