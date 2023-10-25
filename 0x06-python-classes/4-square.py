#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        __size = value
        return __size

    def area(self):
        return self.__size ** 2
