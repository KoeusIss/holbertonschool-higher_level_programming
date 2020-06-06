#!/usr/bin/python3
"""Models Module"""


class Base:
    """Base class

    Attributes:
        __nb_objects (int): class private attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        __n_objects += 1
        self.__id = value
