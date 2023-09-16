#!/usr/bin/env python3
from random import randint
from brain_games.logic import logic


RULES = 'What number is missing in the progression?'


def brain_progression():
    progression = []
    correct_answer = randint(1, 10)
    start = randint(1, 10)
    end = randint(5, 10)
    for x in range(0, end):
        progression += [str(start)]
        start += correct_answer
    ind = randint(0, end - 1)
    progression.pop(ind)
    progression.insert(ind, '..')
    numbers = ' '.join(progression)
    return (correct_answer, numbers)


def main():
    logic(RULES, brain_progression)


if __name__ == '__main__':
    main()
