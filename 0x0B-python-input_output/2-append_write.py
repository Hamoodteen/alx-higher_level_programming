#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def append_write(filename="", text=""):
    """commentttttttttttttttttttttttttttt"""
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(text)
        return len(text)
