#!/usr/bin/env python3
import prompt
# from brain_games.cli import welcome_user, name
from brain_games.scripts.brain_games import main
from random import randint


def greeting(): # 3)проблема с запоминанием решена, эт я подсмотрела
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')



def is_even(number):
    if not number % 2:
        return 'yes'
    else:
        return 'no'


def is_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for x in range(1, 4):
        number = randint(1, 20)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct = is_even(number)
        if correct != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!") # 2)тут тоже не помнит
            break
        elif x < 3:
            print('Correct!')
        else:
            print(f'Correct!\nCongratulations, {name}!') # 1)почему-то перезаписывает переменную name на '' ._.


if __name__ == '__main__':
    main()
    greeting()
    is_even_game()
