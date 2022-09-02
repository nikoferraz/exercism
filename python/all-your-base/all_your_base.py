"""Module for converting numbers to different base systems."""


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:

    """Return the numbers in the output base.
    :param input_base: int - the base of the digits.
    :param digits: list[int] - a list of digits forming a number in the input base.
    :param output_base: int - the desired output base.
    :return: list[int] - a list of digits forming a number in the output base."""

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    base_ten = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        base_ten *= input_base
        base_ten += digit

    rebased = []
    while base_ten > 0:
        base_ten, rem = divmod(base_ten, output_base)
        rebased.insert(0, rem)

    return rebased or [0]
