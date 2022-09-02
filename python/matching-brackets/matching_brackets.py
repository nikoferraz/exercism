"""Functions to find if there are matching brackets."""

from collections import deque


OPENED = {"(": ")", "{": "}", "[": "]"}
CLOSED = {value: key for key, value in OPENED.items()}
BRACKETS = list(OPENED.keys()) + list(CLOSED.keys())


def is_paired(input_string: str) -> bool:
    """Return True if bracket pairs are matched, False otherwise.
    :param input_string: str - a setence with matched/unmatched brackets.
    :return: bool - True if all pairs of brackets are correctly matched.
    """
    all_brackets = deque(
        bracket for bracket in list(input_string) if bracket in BRACKETS
    )

    current = ""

    open_brackets = deque()

    while all_brackets:
        current = all_brackets.popleft()
        if current in OPENED:
            open_brackets.append(current)
        else:
            try:
                if current == OPENED[open_brackets[-1]]:
                    open_brackets.pop()
                else:
                    return False
            except IndexError:
                return False
    if open_brackets:
        return False
    return True
