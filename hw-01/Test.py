import unittest
import math
from main import classify_triangle  # Import the function from main.py

class TestClassifyTriangle(unittest.TestCase):

    # Test for Equilateral Triangle
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle")

    # Test for Isosceles Triangle
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles triangle")

    # Test for Scalene Triangle
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene triangle")

    # Test for Right Scalene Triangle
    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle and Right triangle")

    # Test for Right Isosceles Triangle
    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles triangle and Right triangle")

    # Test for Invalid Triangle (does not satisfy the triangle inequality)
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(1, 10, 12), "Not a triangle")

    # Test for Zero Length Sides (Invalid Triangle)
    def test_zero_length_sides(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not a triangle")

    # Test for Negative Length Sides (Invalid Triangle)
    def test_negative_length_sides(self):
        self.assertEqual(classify_triangle(-1, -1, -1), "Not a triangle")

if __name__ == "__main__":
    unittest.main()



