#!/usr/bin/env python3
from brain_games.logic import logic
from brain_games.games.calc import calc


RULES = 'What is the result of the expression?'


def main():
    logic(RULES, calc)


if __name__ == '__main__':
    main()
