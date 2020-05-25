#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initializer of rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        """
        self.__width = width
        self.__height = height

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

    def area(self):
        """
        Returns the area of the rectangle

        Returns:
            (int): the rectangle area

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle

        Returns:
            (0): if one of width or height is none
            (int): the rectangle perimiter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2
