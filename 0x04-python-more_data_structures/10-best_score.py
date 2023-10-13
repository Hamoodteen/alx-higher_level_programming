#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    v = ""
    for j, k in a_dictionary.items():
        if i < k:
            i = k
            v = j
    return v
