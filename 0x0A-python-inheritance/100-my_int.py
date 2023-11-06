#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


class MyInt(int):
    """commentttttttttttttttttttttttttttt"""
    def __eq__(self, other):
        return True if int.__ne__(self, other) else False

    def __ne__(self, other):
        return True if int.__eq__(self, other) else False
