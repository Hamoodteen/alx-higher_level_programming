#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplist = my_list.copy()
    if idx < 0 or idx > len(cplist) - 1:
        return cplist
    cplist[idx] = element
    return cplist
