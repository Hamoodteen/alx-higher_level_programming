#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = a_dictionary.copy()
    if value not in a_dictionary or len(a_dictionary) == 0:
        return a_dictionary
    for i, j in deletion.items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary
