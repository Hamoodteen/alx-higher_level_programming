#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in my_list:
            print("{:d}".format(i if isinstance(i, int) else ""), end="")
        print()
    except IndexError:
        pass
