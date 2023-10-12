#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = {a: a_dictionary[a] for a in sorted(a_dictionary)}
    for i, j in sort.items():
        print("{}: {}".format(i, j))
