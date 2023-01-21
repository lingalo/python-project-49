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
        correct = func(num1, num2)
        answer = prompt.string('Your answer ')
        if str(answer) != str(correct):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}")
            break
        elif x < 3:
            print('Corect!')
        else:
            print(f'Correct!\nCongratulations, {name}!')


