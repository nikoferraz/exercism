"""Module to classify the Nicomachean "perfection" of a number."""

from math import sqrt

PERFECT = "perfect"
DEFICIENT = "deficient"
ABUNDANT = "abundant"


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive factors.
    :param number: int - a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquote_sum = get_aliquote_sum(number)
    if aliquote_sum == number:
        return PERFECT
    if aliquote_sum < number:
        return DEFICIENT
    return ABUNDANT


def get_aliquote_sum(number: int) -> list[int]:
    """Return a list of the factors of a number, excluding the number itself.
    :param number: int - a positive integer.
    :return: list[int] - A list of integers representing the factors of a number.
    """
    if number == 1:
        return 0
    aliquote_sum = {1}
    for factor in range(2, int(sqrt(number)) + 1):
        if number % factor == 0:
            aliquote_sum.add(factor)
            aliquote_sum.add(number // factor)

    return sum(aliquote_sum)
