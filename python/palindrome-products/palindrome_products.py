def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.
 
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    largest_num = 0
    for factor in range(max_factor, min_factor - 1, -1):
        for factor_2 in range(factor, min_factor - 1, -1):
            temp = factor * factor_2
            stemp = str(temp)
            if temp > largest_num and stemp == stemp[::-1]:
                largest_num = temp

    factors = get_factors(largest_num, min_factor, max_factor)
    if not factors or largest_num == 0:
        return None, []
    return largest_num, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.
 
    :param min_factor: int
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    smallest_num = max_factor**2
    for factor in range(min_factor, max_factor + 1, 1):
        for factor_2 in range(min_factor, max_factor + 1, 1):
            temp = factor * factor_2
            stemp = str(temp)
            if temp < smallest_num and stemp == stemp[::-1]:
                smallest_num = temp

    if str(smallest_num) != str(smallest_num)[::-1]:
        return None, []

    factors = get_factors(smallest_num, min_factor, max_factor)

    return smallest_num, factors


def get_factors(num, min_factor, max_factor):
    factors = []
    for factor in range(min_factor, max_factor + 1):
        if num % factor == 0:
            factors.append([factor, num // factor])
    return factors