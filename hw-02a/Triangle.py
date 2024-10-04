def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer
    values corresponding to the lengths of the three sides of the Triangle.

    return:
        - If all three sides are equal, return 'Equilateral'
        - If exactly one pair of sides are equal, return 'Isosceles'
        - If no pair of sides are equal, return 'Scalene'
        - If not a valid triangle, return 'NotATriangle'
        - If the sum of any two sides equals the square of the third side, return 'Right'
    """

    
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

   
    if a == b == c:
        return 'Equilateral'

   
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    
    if a == b or b == c or a == c:
        return 'Isosceles'

    
    return 'Scalene'

