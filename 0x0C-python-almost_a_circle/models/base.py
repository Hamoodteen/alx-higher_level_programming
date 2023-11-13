#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""
import json


class Base:
    """commenttttttttttttttttttttttttttttttt"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """commenttttttttttttttttttttttttttttttt"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
