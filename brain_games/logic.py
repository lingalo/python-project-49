#!/usr/bin/env python3
import prompt


def main():
    print('Welcome to the Brain Games!')


def greeting():  # 3)проблема с запоминанием решена, эт я подсмотрела
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')



def logic(start_game, list):
    main()
    greeting()
    print(start_game)
    for x in range(1, 4):
        question, correct = list
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if str(correct) != str(answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break
        elif x < 3:
            print('Correct!')
        else:
            print(f'Correct!\nCongratulations, {name}!')
