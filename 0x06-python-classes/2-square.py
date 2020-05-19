#!/usr/bin/python3
class Square:
    """
    Square define a geometric shape square

    Attributes:
        __size (int): the size of the square

    """
    def __init__(self, size=0):
        """
        Init method is a constructor fo Square class

        Args:
            size (int): the size of the square

        """
        self.size = size

    @property
    def size(self):
        """
        Getter of instance attribute

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of instance attributes

        Args:
            value (int): an integer assigned to to the square size

        """
        if type(value) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
