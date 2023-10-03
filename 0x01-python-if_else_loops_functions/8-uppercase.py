#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            print(chr(i - 32), end="")
        else:
            print(chr(i), end="")
