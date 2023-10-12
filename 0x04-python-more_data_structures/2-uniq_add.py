#!/usr/bin/python3
def uniq_add(my_list=[]):
    myset = set()
    myset.append(my_list[i] for i in range(len(my_list)))
    j = 0
    for i in myset:
        j += myset[i]
    return j
