import prompt


def logic(RULES, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)
    count = 0
    for x in range(0, 3):
        correct_answer, number = game()
        print(f'Question: {number}')
        print(f'читерство: {correct_answer}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\')')
            print(f'Let\'s try again {name}!')
            break
    if count == 3:
        print(f'Congratulations, {name}!')
