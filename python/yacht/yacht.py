from collections import Counter
from typing import Callable


def times_num(num: int, dice: list[int]) -> int:
    """Return the number of points.
    :param num - int: a number indicating the corresponding play in Yacht.
    :param dice - list[int]: a list with the integer corresponding to the die face.
    :return: int - the number of points received for the play.
    """
    return Counter(dice)[num] * num


def four_of_a_kind(dice: list[int]) -> int:
    """Return the number of points.
    :param dice - list[int]: a list with the integer corresponding to the die face.
    :return: int - the number of points received for the play.
    """
    face, count = Counter(dice).most_common(1)[0]
    if count >= 4:
        return face * 4
    return 0


# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: times_num(1, dice)
TWOS = lambda dice: times_num(2, dice)
THREES = lambda dice: times_num(3, dice)
FOURS = lambda dice: times_num(4, dice)
FIVES = lambda dice: times_num(5, dice)
SIXES = lambda dice: times_num(6, dice)
FULL_HOUSE = lambda dice: sum(dice) if set(Counter(dice).values()) == {2, 3} else 0
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = lambda dice: 30 if set(dice) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == {2, 3, 4, 5, 6} else 0
CHOICE = sum


def score(dice: list[int], category: Callable[[list[int]], int]) -> int:
    """Return the number of points.
    :param dice - list[int]: a list with the integer corresponding to the die face.
    :param category - Callable: a function for a corresponding play in Yacht.
    :return: int - the number of points received for the play.
    """
    return category(dice)
