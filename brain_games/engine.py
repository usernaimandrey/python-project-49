import prompt


def engine(game, rule_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule_game())

    rounds = 3

    for round in range(rounds):
        question, cor_answer = game()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == cor_answer:
            print('Correct!')
            continue

        bye = f"""{answer} is wrong answer ;(. Correct answer was {cor_answer}.
Let's try again, {name}!"""
        print(bye)
        break
    else:
        round = None

    if round is None:
        print(f'Congratulations, {name}!')
