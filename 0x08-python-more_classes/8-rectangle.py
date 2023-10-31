#!/usr/bin/python3
"""
commentttttttttttttttttttttttttttttt
"""


class Rectangle():
    """ commenttttttttttttttttttttttttttttt """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        mystr = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                mystr += str(self.print_symbol)
            mystr += "\n" if i != self.__height - 1 else ""
        return mystr

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.width * rect_1.height) >= (rect_2.width * rect_2.height):
            return rect_1
        else:
            return rect_2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
