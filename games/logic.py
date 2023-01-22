#!/usr/bin/env python3
import prompt
from random import randint


def logic(start, func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(start)
    for x in range(1, 4):
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        right = func(num1, num2)
        ans = prompt.string('Your answer ')
        if str(ans) != str(right):
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}")
            break
        elif x < 3:
            print('Corect!')
        else:
            print(f'Correct!\nCongratulations, {name}!')
