#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 0 if len(tuple_a) < 1 else tuple_a[0]
    a1 = 0 if len(tuple_a) < 2 else tuple_a[1]
    b0 = 0 if len(tuple_b) < 1 else tuple_b[0]
    b1 = 0 if len(tuple_b) < 2 else tuple_b[1]
    tuple_sum = (a0+b0, a1+b1)
    return tuple_sum
