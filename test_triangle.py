import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_area(self):
        self.assertEqual(area(10, 5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)