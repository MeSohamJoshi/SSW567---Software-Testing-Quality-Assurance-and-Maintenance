# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from triangle import classify_triangle



class TestTriangles(unittest.TestCase):

   
    def testInvalidInputs(self):
        self.assertEqual(classify_triangle(-2, 3, 4), 'InvalidInput', '-2,3,4 is invalid input')
        self.assertEqual(classify_triangle(0, 10, 12), 'InvalidInput', '0,10,12 is invalid input')
        self.assertEqual(classify_triangle(201, 50, 100), 'InvalidInput', '201,50,100 exceeds max side length')

    
    def testNotATriangle(self):
        self.assertEqual(classify_triangle(2, 10, 20), 'NotATriangle', '2,10,20 does not form a triangle')
        self.assertEqual(classify_triangle(3, 4, 8), 'NotATriangle', '3,4,8 does not form a triangle')

    
    def testRightTriangles(self):
        self.assertEqual(classify_triangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')
        self.assertEqual(classify_triangle(12, 5, 13), 'Right', '12,5,13 is a Right triangle')
        self.assertEqual(classify_triangle(10, 6, 8), 'Right', '10,6,8 is a Right triangle')

    
    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(7, 7, 7), 'Equilateral', '7,7,7 should be equilateral')
        self.assertEqual(classify_triangle(50, 50, 50), 'Equilateral', '50,50,50 should be equilateral')

    
    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(10, 10, 15), 'Isosceles', '10,10,15 should be isosceles')
        self.assertEqual(classify_triangle(25, 25, 30), 'Isosceles', '25,25,30 should be isosceles')
        self.assertEqual(classify_triangle(8, 10, 8), 'Isosceles', '8,10,8 should be isosceles')

    
    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(9, 11, 13), 'Scalene', '9,11,13 should be scalene')
        self.assertEqual(classify_triangle(15, 20, 25), 'Right', '15,20,25 should be a right triangle, not just scalene')

    
    def testEdgeCases(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle', '1,2,3 does not form a valid triangle')
        self.assertEqual(classify_triangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

