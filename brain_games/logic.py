import prompt


WRONG_ANSWER = ' is wrong answer ;(. Correct answer was '


def logic(RULES, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)
    count = 0
    for x in range(0, 3):
        correct_answer, question = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}'{WRONG_ANSWER}'{correct_answer}'")
            print(f'Let\'s try again, {name}!')
            break
    if count == 3:
        print(f'Congratulations, {name}!')
