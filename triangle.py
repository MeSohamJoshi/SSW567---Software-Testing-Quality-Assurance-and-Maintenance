"""
This module contains a function to classify types of triangles based on side lengths.
"""

def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer
    values corresponding to the lengths of the three sides of the triangle.

    return:
        - 'Equilateral' if all three sides are equal
        - 'Isosceles' if exactly one pair of sides are equal
        - 'Scalene' if no pair of sides are equal
        - 'NotATriangle' if the side lengths cannot form a valid triangle
        - 'Right' if the triangle is a right triangle
    """

    # Input validation
    if any(side > 200 or side <= 0 for side in (a, b, c)) or \
       not all(isinstance(side, int) for side in (a, b, c)):
        return 'InvalidInput'
    
    # Check for valid triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Triangle type classification
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a == b or b == c or a == c:
        triangle_type = 'Isosceles'
    else:
        triangle_type = 'Scalene'
    
    # Check for right triangle
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    return triangle_type

