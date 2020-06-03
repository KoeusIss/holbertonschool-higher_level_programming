#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class
    Attributes:
        first_name (str): the student first name
        last_name (str): the student last name
        age (int): the student age

    """

    def __init__(self, first_name, last_name, age):
        """Initailazer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the json representation of instance

        Args:
            attrs (list): a given attributes

        Returns:
            (dict) a dictionary

        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
