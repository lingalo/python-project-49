#!/usr/bin/env python3
from games.logic import main


start = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num1, num2 = None):
    print(f'Question: {num1}')
    if num1 == 1:
        return 'no'
    for x in range(2, num1):
        if num1 % x == 0:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    main(start, is_prime)
