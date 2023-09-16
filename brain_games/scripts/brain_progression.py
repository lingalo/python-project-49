#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.logic import logic


RULES = 'What number is missing in the progression?'


def main():
    logic(RULES, progression)


if __name__ == '__main__':
    main()
