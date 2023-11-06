#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def add_attribute(op, n, v):
    """commentttttttttttttttttttttttttttt"""
    setattr(op, n, v)
    if op.n != v:
        raise TypeError("can't add new attribute")
