"""Functions for encoding/decoding atbash cipher."""

from string import ascii_lowercase

ATBASH_ALPHABET = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
PLAINTEXT = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)


def encode(plain_text: str) -> str:

    """
    :param plain_test: str - a plain text string to be encoded.
    :return: str - an encoded string.
    """

    clean_text = "".join([char for char in plain_text.lower() if char.isalnum()])
    atbash = clean_text.translate(ATBASH_ALPHABET)
    return " ".join(atbash[i : i + 5] for i in range(0, len(atbash), 5))


def decode(ciphered_text: str) -> str:

    """
    :param ciphered_text: str - a string of cipher text to be decoded.
    :return: str - a decoded string.
    """

    return ciphered_text.replace(" ", "").translate(PLAINTEXT)
