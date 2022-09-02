def is_armstrong_number(number: int) -> bool:
    """Checks if a number is an Armstrong number."""
    digits = str(number)
    return number == sum(int(num) ** len(digits) for num in digits)
