"""Module to determine the type of triangle"""


def is_triangle(func):
    """Decorator function to determine if the triangle is valid"""

    def wrapper(sides):
        if 0 in sides:
            return False
        if not sides[0] + sides[1] >= sides[2]:
            return False
        if not sides[1] + sides[2] >= sides[0]:
            return False
        if not sides[2] + sides[0] >= sides[1]:
            return False
        return func(sides)

    return wrapper


@is_triangle
def equilateral(sides):
    """Determine if the triangle is equilateral"""
    return sides[0] == sides[1] == sides[2]


@is_triangle
def isosceles(sides):
    """Determine if the triangle is isosceles"""
    return len(set(sides)) < 3


@is_triangle
def scalene(sides):
    """Determine if the triangle is scalene"""
    return len(set(sides)) == 3
