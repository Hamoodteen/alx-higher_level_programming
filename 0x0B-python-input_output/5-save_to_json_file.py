#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


import json


def save_to_json_file(my_obj, filename):
    """commentttttttttttttttttttttttttttt"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
