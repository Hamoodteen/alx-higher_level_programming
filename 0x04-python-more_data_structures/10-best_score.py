#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    i = 0
    for j in a_dictionary.values():
        if i < j:
            i = j
    return i
