from random import randint


def progression():
    progression = []
    difference = randint(1, 10)
    first_number = randint(1, 10)
    length = randint(5, 10)
    for x in range(0, length):
        progression += [str(first_number)]
        first_number += difference
    pass_index = randint(0, length - 1)
    missing_number = progression.pop(pass_index)
    progression.insert(pass_index, '..')
    numbers = ' '.join(progression)
    return (missing_number, numbers)
