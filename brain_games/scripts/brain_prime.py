#!/usr/bin/env python3
from brain_games.games.prime import prime
from brain_games.logic import logic


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    logic(RULES, prime)


if __name__ == '__main__':
    main()
