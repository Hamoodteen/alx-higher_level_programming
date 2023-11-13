#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""
from models.base import Base


class Rectangle(Base):
    """a class Rectangle that inherits from Base.
    Public instance methods:
       - area()
       - display()
       - to_dictionary()
       - update()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialized Rectangle instance.

        Args:
           - __width: width of the Rectangle
           - __height: height of the Rectangle.
           - __x: position
           - __y: position
           - id: id
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the Rectangle to a value.

        Args:
           - value: value of the width must be an int.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the Rectangle to a value

        Args:
           - value: value of the height must be an int.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of position x to a value.

        Args:
           - value: value of x must be an integer.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the position y of the Rectangle to a value

        Args:
           - value: value of y must be an int
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
