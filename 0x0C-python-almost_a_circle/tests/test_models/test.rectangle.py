#!/usr/bin/python3
"""Unittest rectangle
Test cases for the class Rectangle.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class TestRectangle that inherits from unittest.TestCase."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """class TestRectangle: checking for id."""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 8, 3, 7, -9)
        self.assertEqual(r2.id, -9)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_2_1(self):
        """class TestRectangle: checks for attribute values."""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(6, 3, 2, 1, 12)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)

    def test_2_2(self):
        """class TestRectangle: checks for missing arguments."""

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r2 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_2_3(self):
        """class TestRectangle: checks for inheritance."""

        r1 = Rectangle(2, 1)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_2_3(self):
        """Test Rectangle class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(x.exception))
