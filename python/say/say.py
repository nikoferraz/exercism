"""Module to spell out numbers."""

ONES = "zero one two three four five six seven eight nine ten".split()
TEENS = "zero eleven twelve thirtee fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "zero ten twenty thirty forty fifty sixty seventy eighty ninety".split()
LARGE_NUMS = "thousand million billion".split()


def spell(number, large):
    """Return a number spelled out."""

    if number == 0:
        return ""

    spelled_out = ""
    if number > 99:
        spelled_out += f"{ONES[number // 100]} hundred"
        number %= 100
        if number == 0:
            return spelled_out
        spelled_out += " "

    if 0 < number < 11:
        spelled_out += ONES[number]
    elif number < 20:
        spelled_out += TEENS[number % 10]
    else:
        tens = TENS[number // 10]
        if (number := number % 10) > 0:
            tens += f"-{ONES[number]}"
        spelled_out += tens

    if large >= 0:
        spelled_out += f" {LARGE_NUMS[large]}"

    return spelled_out


def say(number):
    """Returns a string with number spelled out.

    The maximum number is 999,999,999,999 or
    Nine hundred and ninety-nine billion nine hundred and
    ninety-nine million ninehundred and ninety-nine thousand
    nine hundred and ninety-nine.
    """

    if 0 > number or number >= 1e12:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    spelled_out = []
    num = number
    large = -1
    while num > 0:
        num, remainder = divmod(num, 1000)
        spelled_number = spell(remainder, large)
        spelled_out.append(spelled_number)
        large += 1

    return " ".join(reversed(spelled_out)).strip()
