#!/usr/bin/python3
def remove_char_at(str, n):
    cp = str
    return cp[:n] + cp[n+1:] if n >= 0 else cp
