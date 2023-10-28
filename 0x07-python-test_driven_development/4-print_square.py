#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


def print_square(size):
    """ commenttttttttttttttttttttttttttttt """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(((('#' * size) + '\n') * size), end="")
