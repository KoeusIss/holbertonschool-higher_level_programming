#!/usr/bin/python3
"""Square module"""
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
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns humain readable Square form"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """update square attributes"""
        for idx, item in enumerate(args):
            if idx == 0:
                self.id = item
            if idx == 1:
                self.size = item
            if idx == 2:
                self.x = item
            if idx == 3:
                self.y = item
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "size":
                self.size = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """Dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
