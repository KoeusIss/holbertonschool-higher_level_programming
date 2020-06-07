#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
        width (int): rectangle's width
        height (int): rectangle's height
        x (int): rectangle's abscissa
        y (int): rectangle's orders
        id (int): the rectangle id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): given setting value

        Raises:
            TypeError: if width not an integer
            ValueError: if width a null or negative integer

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): given setting value

        Raises:
            TypeError: if height not an integer
            ValueError: if height a null or negative integer

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter

        Args:
            value (int): given stting value

        Raises:
            TypeError: if x not an integer
            ValueError: if x non positive integer

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter

        Args:
            value (int): given setting value

        Raises:
            TypeError: if y not integer
            ValueError: if y non positive integer

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """displays a rectangle with #"""
        print("{}".format("\n"*self.y), end="")
        for i in range(self.height):
            print("{}{}".format(" "*self.x, "#"*self.width))

    def __str__(self):
        """Returns humain readable rectangle form"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """updates rectangle attributes

        Args:
            args (tuple): tuple of a designated attributes

        """
        for idx, item in enumerate(args):
            if idx == 0: self.id = item
            if idx == 1: self.width = item
            if idx == 2: self.height = item
            if idx == 3: self.x = item
            if idx == 4: self.y = item
        for k, v in kwargs.items():
            if k == "id": self.id = v
            if k == "width": self.width = v
            if k == "height": self.height = v
            if k == "x": self.x = v
            if k == "y": self.y = v
