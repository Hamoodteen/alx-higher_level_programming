#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """commentttttttttttttttttttttttttttt"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
