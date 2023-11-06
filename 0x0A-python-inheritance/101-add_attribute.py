#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def add_attribute(op, n, v):
    """commentttttttttttttttttttttttttttt"""
    if not hasattr(op, n):
        if not setattr(op, n, v):
            raise TypeError("can't add new attribute")
