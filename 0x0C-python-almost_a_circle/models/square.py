#!/usr/bin/python3
"""Module square.py
class Square that inherits from Rectangle.
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square instances

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return s
