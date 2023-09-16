#!/usr/bin/env python3
from random import randint
from brain_games.logic import logic


RULES = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    num3 = randint(2, 10)
    num1 = randint(2, 10) * num3
    num2 = randint(2, 10) * num3
    correct_answer = num3
    for x in range(num3, min(num1, num2) + 1):
        if not num1 % x and not num2 % x:
            if x > num3:
                correct_answer = x
        x += 1

    print(f'читерство ужас:{num1}, {num2}')
    numbers = f'{num1} {num2}'
    return (correct_answer, numbers)


def main():
    logic(RULES, brain_gcd)


if __name__ == '__main__':
    main()
