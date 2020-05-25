#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class

    Attributes:
        width (int): private attribute
        height (int): private attribute
    """

    def __init__(self, width=0, height=0):
        """
        Initializer of rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter

        Returns:
            (int): the width of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value (int): a positive integer

        Raises:
            TypeError: if value not an integer
            ValueError: if value is negative

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter

        Returns:
            (int): the height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
