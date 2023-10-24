#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value if isinstance(value, int) else ""))
        return True
    except ValueError:
        return False
