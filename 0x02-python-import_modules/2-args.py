#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1) if len(sys.argv) > 2 else "1 argument:")
        for i in range(1, len(sys.argv)):
            j = sys.argv[i]
            print("{:d}: {:s}".format(i, j))