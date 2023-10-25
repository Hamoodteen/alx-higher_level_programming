#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
