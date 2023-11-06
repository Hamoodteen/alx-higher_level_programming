#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def add_attribute(op, n, v):
    """commentttttttttttttttttttttttttttt"""
    setattr(op, n, v)
    if not hasattr(op, n):
        raise TypeError("can't add new attribute")
