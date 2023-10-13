from random import randint


def gcd():
    divider = randint(2, 10)
    num1 = randint(2, 10) * divider
    num2 = randint(2, 10) * divider
    question = f'{num1} {num2}'
    for x in range(min(num1, num2), divider, -1):
        if not num1 % x and not num2 % x:
            return (x, question)
    return (divider, question)
