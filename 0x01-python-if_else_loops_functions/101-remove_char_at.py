#!/usr/bin/python3
def remove_char_at(str, n):
    cp = str
    print(cp[:n], end="")
    print(cp[n+1:-1])
