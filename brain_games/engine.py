import prompt
from colorama import Fore


def engine(game: callable, rule_game: callable):
    print(f'{Fore.GREEN}Welcome to the Brain Games!')
    name = prompt.string(f'{Fore.BLUE}May I have your name? ')
    print(f'{Fore.GREEN}Hello, {name}!')
    print(rule_game())

    rounds = 3

    for round in range(rounds):
        question, cor_answer = game()

        print(f'{Fore.YELLOW}Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == cor_answer:
            print(f'{Fore.GREEN}Correct!')
            continue

        bye = f"""{answer} is wrong answer ;(. Correct answer was {cor_answer}.
Let's try again, {name}!"""
        print(f'{Fore.RED}{bye}')
        break
    else:
        round = None

    if round is None:
        print(f'{Fore.GREEN}Congratulations, {name}!')
