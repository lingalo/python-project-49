from games.logic import logic
from random import randint, choice

start = 'What number is missing in the progression?'


def what_missing(num1, num2):
    question = []
    for x in range(1, 11):
        question += [num1]
        num1 += num2
    ind = randint(1, 9)
    correct = question[ind]
    question[ind] = '..'
    print(f'Qustion: {" ".join(str(x) for x in question)}')
    print(correct)
    return correct

if __name__ == '__main__':
    logic(start, what_missing)