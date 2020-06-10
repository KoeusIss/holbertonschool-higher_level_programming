#!/usr/bin/python3
"""Base Module"""
import json
import csv


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
        if list_objs is not None:
            for d in list_objs:
                l.append(cls.to_dictionary(d))
        with open(str(cls.__name__ + ".json"), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON representation"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a class to csv"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            ll = [[x.id, x.width, x.height, x.x, x.y] for x in list_objs]
        else:
            ll = [[x.id, x.size, x.x, x.y] for x in list_objs]
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(ll)
