#!/usr/bin/python3
""" Test function find_peak """


""" it will be O(n) or O(log(n))"""


def find_peak(list_of_integers):
    """ Test function find_peak """

    if len(list_of_integers) == 0:
        return None
    if not sorted(list_of_integers):
        list_of_integers.sort()
        return max(list_of_integers)
    m = 0
    for i in list_of_integers:
        if i > m:
            m = i
    return m
