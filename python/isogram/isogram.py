def is_isogram(string):
    """Checks if the string is an isogram."""
    isogram = string.replace("-", "").replace(" ", "")
    return len(isogram) == len(set(isogram.upper()))
