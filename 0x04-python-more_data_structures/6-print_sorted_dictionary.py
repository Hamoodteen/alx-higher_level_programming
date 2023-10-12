#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = a_dictionary.copy()
    sorted(sort)
    for i in sort:
        for j in sort.values():
            print("{}:{}".format(i, j))
