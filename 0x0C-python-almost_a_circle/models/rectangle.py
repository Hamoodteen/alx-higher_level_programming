#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""

from base import Base


class Rectangle(Base):
    """commenttttttttttttttttttttttttttttttt"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, v):
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        self.__height = v

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v
