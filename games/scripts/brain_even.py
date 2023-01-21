from games.logic import logic


start = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num1, num2 = None):
    print(f'Question: {num1}')
    if num1 % 2:
        return 'no'
    else:
        return 'yes'


if __name__ == '__main__':
    logic(start, is_even)