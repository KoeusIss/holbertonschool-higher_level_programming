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
        return list(map(json.dumps, list_dictionaries))
