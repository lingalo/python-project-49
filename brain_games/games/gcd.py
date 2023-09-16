from random import randint


def gcd():
    divider = randint(2, 10)
    num1 = randint(2, 10) * divider
    num2 = randint(2, 10) * divider
    correct_answer = divider
    for x in range(divider, min(num1, num2) + 1):
        if not num1 % x and not num2 % x:
            if x > divider:
                correct_answer = x
        x += 1
    numbers = f'{num1} {num2}'
    return (correct_answer, numbers)
