"""Module to calculate the difference of squares of a number."""


def square_of_sum(number):
    """Return the square of the sum of the first n natural numbers."""
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number):
    """Return the sum of the squares of the first n natural numbers."""
    return sum(i**2 for i in range(1, number + 1))


def difference_of_squares(number):
    """Return the difference of the squares of the first n natural numbers."""
    return square_of_sum(number) - sum_of_squares(number)
