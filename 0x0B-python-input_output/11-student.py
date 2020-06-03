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

    def to_json(self):
        """Returns the json representation of instance"""
        return self.__dict__
