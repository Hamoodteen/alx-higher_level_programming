#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = []
    if value not in a_dictionary:
        return a_dictionary
    for i, j in a_dictionary.items():
        if j == value:
            deletion.append(i)
    for k in deletion:
        a_dictionary.pop(k)
    return a_dictionary
