#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


import json


def load_from_json_file(filename):
    """commentttttttttttttttttttttttttttt"""
    with open(filename, "r", encoding="UTF-8") as f:
        json.load(f)
