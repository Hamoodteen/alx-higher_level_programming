#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = []
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j == value:
                deletion.append(i)
        for k in deletion:
            del a_dictionary[k]
    return a_dictionary
