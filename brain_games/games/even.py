from random import randint


def even():
    number = randint(1, 1000)
    if number % 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return (correct_answer, number)
