#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary:
        return a_dictionary
    else:
        a_dictionary = {k: v for k, v in a_dictionary.items() if v!= value}
        return a_dictionary
