"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
from math import sqrt, pi


class TestAddArea(unittest.TestCase):
    """tests of the Circle class method, add_area"""
    def test_typical_values(self):
        """test for add_area using typical values."""
        c1 = Circle(2)
        c2 = Circle(3)
        c3 = c1.add_area(c2)
        self.assertEqual(c1.get_area() + c2.get_area(), c3.get_area())
        self.assertEqual(sqrt(c3.get_area()/pi), c3.get_radius())

        c4 = Circle(2905.39)
        c5 = Circle(37.22)
        c6 = c4.add_area(c5)
        self.assertAlmostEqual(c4.get_area() + c5.get_area(), c6.get_area())
        self.assertAlmostEqual(sqrt(c6.get_area() / pi), c6.get_radius())

    def test_one_circle_has_radius_0(self):
        """test for add_area for an "edge case" where one circle has radius 0."""
        c0 = Circle(0)
        c1 = Circle(5)
        c2 = c1.add_area(c0)
        c3 = c0.add_area(c1)
        self.assertEqual(c1.get_area(), c2.get_area())
        self.assertEqual(c1.get_area(), c3.get_area())
        self.assertEqual(5, c2.get_radius())
        self.assertEqual(5, c3.get_radius())

    def test_radius_cannot_be_negative(self):
        """test that circle constructor raises exception of radius is negative."""
        with self.assertRaises(ValueError):
            c_negative1 = Circle(-9999999)
        with self.assertRaises(ValueError):
            c_negative2 = Circle(-0.0000000001)
