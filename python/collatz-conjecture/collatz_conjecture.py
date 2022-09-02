"""Collatz Conjecture"""


def steps(number: int) -> int:
    """Given a number return the number of steps it takes for mutate it to 1"""
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    _steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        _steps += 1
    return _steps

def most_steps(n):
    '''Return the number under n that has the longest chain of steps.'''
    longest = 0
    number = None
    for i in range(n, 0, -1):
        temp = steps(i)
        if temp > longest:
            longest = temp
            number = i
    return number