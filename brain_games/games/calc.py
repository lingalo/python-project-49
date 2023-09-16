from random import randint, choice


def calc():
    num1 = randint(1, 5)
    num2 = randint(1, 5)
    elem = choice('+-*')
    if elem == '+':
        correct_answer = num1 + num2
        expression = f'{num1} + {num2}'
    elif elem == '-':
        correct_answer = num1 - num2
        expression = f'{num1} - {num2}'
    else:
        correct_answer = num1 * num2
        expression = f'{num1} * {num2}'
    return correct_answer, expression
