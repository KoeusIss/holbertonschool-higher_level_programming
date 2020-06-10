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
        """Create from dictionnary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        filename = cls.__name__ + ".json"
        ll = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                a_dictionary = cls.from_json_string(f.read())
                for row in a_dictionary:
                    ll.append(cls.create(**row))
                return ll
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a class to csv"""
        filename = cls.__name__ + ".csv"
        attributes = ["id", "x", "y"]
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id","width", "height", "x", "y"]
                else:
                    attributes = ["id","size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=attributes)
                for item in list_objs:
                    writer.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "w") as f:
                reader = csv.DictReader(f)
                ll = []
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    ll.append(row)
                return [cls.create(**item) for item in ll]
        except FileNotFoundError:
            return []