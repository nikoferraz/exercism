"""Binary search module."""

from typing import TypeVar

T = TypeVar("T")


def find(search_list: list[T], value: T) -> int:
    """Return the index of the value in the list.
    :param search_list: list - list to be searched.
    :param value:  T - a value that is searched.
    :return: int - the index of the value
    """

    left, right = 0, len(search_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if search_list[middle] == value:
            return middle
        if search_list[middle] < value:
            left = middle + 1
        elif search_list[middle] > value:
            right = middle - 1

    raise ValueError("value not in array")
