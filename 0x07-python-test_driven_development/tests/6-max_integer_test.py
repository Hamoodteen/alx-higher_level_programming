"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ classssssssssssssssssssssssssssssssssssssssssss """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertNotEqual(max_integer([1, 2, 3, 4, 5]), 2)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertNotEqual(max_integer(["x", "u", "a", "e"]), "e")
        self.assertEqual(max_integer(["a", "A"]), "a")
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 7, 7]), 7)
        with self.assertRaises(TypeError):
            max_integer(["a", "b", 4, 2])
        with self.assertRaises(TypeError):
            max_integer(4, 2)
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer([4, [2, 4, 6], 1, 7])
        try:
            max_integer((4, 2, 1, 7))
        except TypeError:
            self.fail()


if __name__ == '__main__':
    unittest.main()
