#!/usr/bin/python3
def no_c(my_string):
    ns = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        ns += c
    return ns
