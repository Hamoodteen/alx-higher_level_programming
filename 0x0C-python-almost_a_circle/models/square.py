#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """commenttttttttttttttttttttttttttttttt"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width or self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value
