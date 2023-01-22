#!/usr/bin/env python3
from games.logic import logic
from random import randint


start = 'What number is missing in the progression?'


def what_missing(num1, num2):
    question = []
    for x in range(1, 11):
        question += [num1]
        num1 += num2
    ind = randint(0, 9)
    correct = question[ind]
    question[ind] = '..'
    print(f'Question: {" ".join(str(x) for x in question)}')
    #print(correct)
    return correct


def main():
    logic(start, what_missing)


if __name__ == '__main__':
    main()
