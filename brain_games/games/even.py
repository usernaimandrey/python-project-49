from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def is_even(num):
    return num % 2 == 0


def game_rule():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    question = rnd(range(1, 100))
    correct_answer = 'yes' if is_even(question) else 'no'
    return (question, correct_answer)


def run():
    return engine(even, game_rule)
