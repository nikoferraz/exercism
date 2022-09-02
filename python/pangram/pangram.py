def is_pangram(sentence: str) -> bool:
    """Determines if a sentence is a pangram."""
    return len({ch for ch in sentence.lower() if ch.isalpha()}) == 26
