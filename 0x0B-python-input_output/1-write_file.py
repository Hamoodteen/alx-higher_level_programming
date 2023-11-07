#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def write_file(filename="", text=""):
    """commentttttttttttttttttttttttttttt"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(text)
        return len(text)
