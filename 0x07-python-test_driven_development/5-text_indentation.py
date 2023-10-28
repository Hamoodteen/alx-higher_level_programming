#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


def text_indentation(text):
    """ commenttttttttttttttttttttttttttttt """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newstr = ""
    for c in text:
        newstr += c
        if c in ".?:":
            newstr += "\n\n"
    print(newstr, end="")
