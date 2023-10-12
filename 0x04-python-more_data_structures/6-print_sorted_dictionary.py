#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = a_dictionary.copy()
    sorted(sort)
    for i, j in sort.items():
        print("{}: {}".format(i, j))
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)