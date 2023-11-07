#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def read_file(filename=""):
    """commentttttttttttttttttttttttttttt"""
    with open(filename, "r", encoding="UTF-8") as f:
        for i in f:
            print(i, end="")
