"""Module to do Caesar cipher rotations."""

from string import ascii_uppercase


def rotate(text: str, key: int) -> str:
    """Return the Caesar cipher
    :param text: str - the text to be rotated.
    :param key: int - the rotation key.
    :return: str - the cipher string.
    """
    key = key % 26
    transposed_alphabet = ascii_uppercase[key:] + ascii_uppercase[:key]
    rotation = str.maketrans(
        ascii_uppercase + ascii_uppercase.lower(),
        transposed_alphabet + transposed_alphabet.lower(),
    )
    return text.translate(rotation)
