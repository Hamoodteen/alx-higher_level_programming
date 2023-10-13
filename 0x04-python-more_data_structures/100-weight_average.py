#!/usr/bin/python3
def weight_average(my_list=[]):
    res, div = 0, 0
    if len(my_list) == 0 or not my_list:
        return 0
    for i in my_list:
        res += i[0] * i[1]
        div += i[1]
    return res / div
