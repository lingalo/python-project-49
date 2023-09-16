#!/usr/bin/env python3
from brain_games.games.even import even
from brain_games.logic import logic


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    logic(RULES, even)


if __name__ == '__main__':
    main()
