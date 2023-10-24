#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(int(value))
        return True
    except ValueError:
        print("{} is not an integer".format("{value:d}"))
        return False
