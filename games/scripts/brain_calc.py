#!/usr/bin/env python3
from games.logic import main
from random import choices


start = 'What is the result of the expression?'


def calc(num1, num2):
    operator = choices('+-*')
    expression = f'{num1} {operator[0]} {num2}'
    print(f'Question: {expression}')
    return eval(f'{expression}')


if __name__ == '__main__':
    main(start, calc)
