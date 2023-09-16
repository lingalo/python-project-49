#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.logic import logic


RULES = 'Find the greatest common divisor of given numbers.'


def main():
    logic(RULES, gcd)


if __name__ == '__main__':
    main()
