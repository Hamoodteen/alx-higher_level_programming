#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    my_list2 = my_list.copy()
    for c in range(l):
        my_list2[c] = my_list[l-1-c]
    for i in my_list2:
        print("{:d}".format(i))
