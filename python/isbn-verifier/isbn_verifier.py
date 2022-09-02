"""Module for validating ISBN strings."""


def is_valid(isbn: str) -> bool:
    """Checks if the given string is a valid ISBN."""
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for val, char in enumerate(isbn[::-1], start=1):
        if char.isdigit():
            total += int(char) * val
        elif char == "X" and val == 1:
            total += 10
        else:
            return False
    return (total % 11) == 0
