#!/usr/bin/env python3
from random import randint, choice
from brain_games.logic import logic


RULES = 'What is the result of the expression?'


def brain_calc():
    num1 = randint(1, 5)
    num2 = randint(1, 5)
    elem = choice('+-*')
    if elem == '+':
        correct_answer = num1 + num2
        expression = f'{num1} + {num2}'
        print(correct_answer)
    elif elem == '-':
        correct_answer = num1 - num2
        expression = f'{num1} - {num2}'
        print(correct_answer)
    else:
        correct_answer = num1 * num2
        expression = f'{num1} * {num2}'
        print(correct_answer)
    return correct_answer, expression


def main():
    logic(RULES, brain_calc)


if __name__ == '__main__':
    main()
