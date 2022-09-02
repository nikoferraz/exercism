"""Anagrams functions."""

from collections import Counter


def is_anagram(word: str, candidate: str) -> bool:
    """Return true if candidate is an anagram of word and false otherwise
    :param word: str - a string that needs to be checked against.
    :param candidate: str - a string that is tested to be an anagram of word.
    :return: bool - True if canidadte is an anagram of word, false otherwise.
    """
    return Counter(word.lower()) == Counter(candidate.lower())


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Return a set of candidate anagrams for a given word

    :param word: str - a word from which the candidate words is an anagram.
    :param candidates: list[str] - a list of candidate words that could be an anagram of word.
    :return: list[str] - a list with all candidate words that are an anagram of word.
    """
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word.lower() and is_anagram(word, candidate)
    ]
