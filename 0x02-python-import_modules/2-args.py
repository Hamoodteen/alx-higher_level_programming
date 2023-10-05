#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
