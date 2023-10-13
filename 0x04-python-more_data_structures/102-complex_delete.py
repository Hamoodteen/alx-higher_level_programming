#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = []
    if value not in a_dictionary or len(a_dictionary) == 0:
        return a_dictionary
    for i, j in a_dictionary.items():
        if j == value:
            deletion.append(i)
    for k in deletion:
        del a_dictionary[k]
    return a_dictionary
