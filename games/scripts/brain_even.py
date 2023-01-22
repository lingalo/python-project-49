#!/usr/bin/env python3
from games.logic import main


start = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num1, num2 = None):
    print(f'Question: {num1}')
    if num1 % 2:
        return 'no'
    else:
        return 'yes'


if __name__ == '__main__':
    main(start, is_even)
