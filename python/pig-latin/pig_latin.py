"""Function to translate English to Pig Latin."""


def pig_latin(word: str) -> str:
    """Return a word converted to pig latin.
    :param word - str: a word to be translated to pig lating.
    :return: str - the translated word
    """
    vowels = list("aeiou")
    vowels_sound = ["xr", "yt"]

    if word[0] in vowels or word[:2] in vowels_sound:
        return word + "ay"

    word_has_vowel = any(char in vowels for char in word)
    if word_has_vowel or "y" in word:
        while word[0] not in vowels and word[:2] not in vowels_sound:
            if word[:2] == "qu":
                word = word[2:] + word[:2]
            else:
                word = word[1:] + word[0]
            if word[0] == "y":
                break

    return word + "ay"


def translate(text: str) -> str:
    """Return a translated word or sentence from English to Pig Latin.
    :param word - str: a word to be translated to pig lating.
    :return: str - the translated word
    """
    return " ".join(pig_latin(word) for word in text.split(" "))
