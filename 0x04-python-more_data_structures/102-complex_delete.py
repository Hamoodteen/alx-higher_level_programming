#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary:
        return a_dictionary
    for i, j in a_dictionary.items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary
