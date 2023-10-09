#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = my_list.copy()
    my_list3 = reversed(my_list2)
    for i in my_list3:
        print("{:d}".format(i))
