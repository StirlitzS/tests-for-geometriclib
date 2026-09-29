import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0), 0)

    def test_area(self):
        self.assertEqual(area(4), 16)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)