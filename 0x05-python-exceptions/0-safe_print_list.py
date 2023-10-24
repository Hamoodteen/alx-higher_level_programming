#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except:
        s = 0
        for i in my_list:
            print(i, end="")
            s += 1
        print()
        return s
