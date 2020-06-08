#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base class

    Attributes:
        __nb_objects (int): class private attribute
        id (int): public instance attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer

        Args:
            id (int): objects id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON format representaion"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation

        Args:
            list_objs (list): list of instance

        """
        l = []
        for d in list_objs:
            l.append(cls.to_dictionary(d))
        with open(str(cls.__name__ + ".json"), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON representation"""
        if json_string is None or json_string == '':
            return []
        return json.dumps(json_string)
