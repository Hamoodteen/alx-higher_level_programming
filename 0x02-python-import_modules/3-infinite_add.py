#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    s = 0
    for i in argv:
        if i == argv[0]:
            continue
        s += int(i)
    print(s)
