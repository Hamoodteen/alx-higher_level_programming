#!/usr/bin/python3
def uniq_add(my_list=[]):
    myset = set()
    for i in range(len(my_list)):
        myset.add(my_list[i])
    j = 0
    for i in myset:
        j += i
    return j
