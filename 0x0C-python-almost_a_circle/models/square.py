#!/usr/bin/python3
from models.base import *
from models.rectangle import *


class Square(Rectangle):
    """Square class inherited from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.__size = value

    def __str__(self):
        """Returns humain readable Square form"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )
