#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = my_list.copy()
    for i in range(len(my_list)):
        if cp[i] == search:
            cp[i] = replace
    return cp
