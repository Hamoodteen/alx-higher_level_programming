#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = a_dictionary.copy()
    if value not in a_dictionary:
        return a_dictionary
    for i, j in deletion.items():
        if j == value:
            deletion.append(i)
    for k in deletion:
        del a_dictionary[k]
    return a_dictionary
