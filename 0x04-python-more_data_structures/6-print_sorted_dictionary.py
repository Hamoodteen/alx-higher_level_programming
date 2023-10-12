#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = a_dictionary.copy()
    sorted(sort)
    for i, j in sort.items():
        print("{}: {}".format(i, j))
