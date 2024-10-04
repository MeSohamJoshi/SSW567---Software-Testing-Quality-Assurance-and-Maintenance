def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.
    :param a: Length of the first side.
    :param b: Length of the second side.
    :param c: Length of the third side.
    :return: A string describing the type of triangle.
    """

    # Triangle inequality check (ensures the sides form a valid triangle)
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    # Sorting the sides for easier right-triangle checking
    sides = sorted([a, b, c])

    # Check for a right triangle (Pythagoras: a^2 + b^2 = c^2)
    is_right_triangle = round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5)

    # Check for equilateral triangle (all sides equal)
    if a == b == c:
        return "Equilateral triangle" + (" and Right triangle" if is_right_triangle else "")

    # Check for isosceles triangle (two sides equal)
    if a == b or b == c or a == c:
        return "Isosceles triangle" + (" and Right triangle" if is_right_triangle else "")

    # Otherwise, it’s a scalene triangle (no sides are equal)
    return "Scalene triangle" + (" and Right triangle" if is_right_triangle else "")

def main():
    print("Welcome to the Triangle Classifier!")

    while True:
        try:
            # Input for the sides of the triangle
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            c = float(input("Enter the length of side c: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Call the classify_triangle function and display the result
        result = classify_triangle(a, b, c)
        print(f"The triangle is classified as: {result}")

        # Asking if the user wants to classify another triangle
        again = input("Do you want to classify another triangle? (yes to continue, any other key to exit): ").strip().lower()
        if again != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()



