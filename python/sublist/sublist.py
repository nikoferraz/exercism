from typing import Any

SUBLIST = 1
SUPERLIST = 2
EQUAL = 0
UNEQUAL = -1


def sublist(list_one: list[Any], list_two: list[Any]) -> int:
    """Return an integer indicating the relationship between to lists.
    :param list_one: list[Any] - a list of any type.
    :param list_two: list[Any] - a list of any type.
    :return: int - an integer indicating if list one is a sublist,
    superlist, equal to or unequal to list_two.
    """

    list_one = str(list_one).strip("[]") + ","
    list_two = str(list_two).strip("[]") + ","

    if list_one == list_two:
        return EQUAL

    if list_one in list_two:
        return SUBLIST

    if list_two in list_one:
        return SUPERLIST

    return UNEQUAL
