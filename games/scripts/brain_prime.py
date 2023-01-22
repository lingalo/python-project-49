#!/usr/bin/env python3
from games.logic import logic


start = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num1, num2=None):
    print(f'Question: {num1}')
    if num1 == 1:
        return 'no'
    for x in range(2, num1):
        if num1 % x == 0:
            return 'no'
    return 'yes'


def main():
    logic(start, is_prime)


if __name__ == '__main__':
    main()
