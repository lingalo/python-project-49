#!/usr/bin/env python3
from games.logic import logic


start = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num1, num2=None):
    print(f'Question: {num1}')
    if num1 % 2:
        return 'no'
    else:
        return 'yes'


def main():
    logic(start, is_even)


if __name__ == '__main__':
    main()
