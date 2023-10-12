#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = a_dictionary.copy()
    print(sort.items() for i in sorted(sort))
