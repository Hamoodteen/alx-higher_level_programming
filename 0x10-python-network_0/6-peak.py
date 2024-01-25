#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    m = 0
    for i in list_of_integers:
        if i > m:
            m = i
    return m
