#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


def write_file(filename="", text=""):
    """commentttttttttttttttttttttttttttt"""
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            f.write(text)
    except PermissionError:
        print("Permission denied")
