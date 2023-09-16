#!/usr/bin/env python3
from random import randint
from brain_games.logic import logic


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    number = randint(1, 1000)
    if number % 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return (correct_answer, number)


def main():
    logic(RULES, brain_even)


if __name__ == '__main__':
    main()
