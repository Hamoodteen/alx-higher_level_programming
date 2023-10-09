#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = reversed(my_list)
    for i in my_list2:
        print("{:d}".format(int(i)))
