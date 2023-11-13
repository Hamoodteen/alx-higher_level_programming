#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """commenttttttttttttttttttttttttttttttt"""
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if not list_objs:
                json.dump([], f)
            else:
                json.dump(cls.to_json_string(list_objs), f)

    @staticmethod
    def from_json_string(json_string):
        """commenttttttttttttttttttttttttttttttt"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """commenttttttttttttttttttttttttttttttt"""
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """commenttttttttttttttttttttttttttttttt"""
        with open(
                "{}.csv".format(cls.__name__),
                "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if not list_objs:
                w.writerow([])
            else:
                f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file_csv(cls):
        """commenttttttttttttttttttttttttttttttt"""
        with open(
                "{}.csv".format(cls.__name__),
                "r", newline="", encoding="utf-8") as f:
            print(f.read())
