from collections import deque

def calculate(number, operation, number_2):
    match operation:
        case "plus":
            return number + number_2
        case "minus":
            return number - number_2
        case "divided":
            return number / number_2
        case "multiplied":
            return number * number_2
        case _:
            raise ValueError("unknown operation")

def answer(question):
    question_list = question.strip("?").split()
    numbers, operations = deque(), deque()
    for word in question_list:
        if word[0] == '-' or word.isnumeric():
            numbers.append(int(word))
        elif word in "minus equal plus divided multiplied":
            operations.append(word)


    if len(numbers) == 0 and len(operations) == 0:
        raise ValueError("unknown operation")

    if len(operations) == 0:
        return numbers.pop()

    result = calculate(numbers.popleft(), operations.popleft(), numbers.popleft())

    while len(operations) > 0:
        result = calculate(result, operations.popleft(), numbers.popleft())

    return result