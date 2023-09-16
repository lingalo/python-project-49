from random import randint


def prime():
    number = randint(2, 23)
    count = number
    while count > 2:
        count -= 1
        if not number % count:
            return ('no', number)
    return ('yes', number)
