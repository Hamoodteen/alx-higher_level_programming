#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """commenttttttttttttttttttttttttttttttt"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.__size = value

    def update(self, *args, **kwargs):
        """commenttttttttttttttttttttttttttttttt"""
        if args and len(args) != 0 and len(args) <= 5:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
