#!/usr/bin/python3
""" Test function find_peak """


""" it will be O(n) or O(log(n))"""


def find_peak(list_of_integers):
    """ Test function find_peak """

    if len(list_of_integers) == 0:
        return None
    return max(sorted(list_of_integers))
