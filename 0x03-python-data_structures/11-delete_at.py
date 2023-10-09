#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in my_list:
        if i != my_list[idx]:
            new_list.append(i)
    my_list[idx] = None
    return new_list
