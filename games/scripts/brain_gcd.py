from games.logic import logic


start = 'Find the greatest common divisor of given numbers.'


def what_is_gcd(num1, num2):
    print(f'Question {num1} {num2}')
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


if __name__ == '__main__':
    logic(start, what_is_gcd)
