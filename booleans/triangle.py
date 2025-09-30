"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths."""

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    is_triangle_ok = is_triangle(sides)
    if not is_triangle_ok:
        return False

    if a == b == c:
        return True
    return False
        


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    is_triangle_ok = is_triangle(sides)
    if not is_triangle_ok:
        return False

    if a == b or b == c or a == c:
        return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    is_triangle_ok = is_triangle(sides)
    if not is_triangle_ok:
        return False

    if a != b and c != a and c != b:
        return True
    return False

def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == 0 or b == 0 or c == 0:
        return False

    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False
