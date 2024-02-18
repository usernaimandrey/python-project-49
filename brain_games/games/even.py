from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def is_even(num: int) -> bool:
    return num % 2 == 0


def game_rule() -> str:
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even() -> tuple[str, str]:
    question = rnd(range(1, 100))
    correct_answer = 'yes' if is_even(question) else 'no'
    return (question, correct_answer)


def run() -> callable:
    return engine(even, game_rule)
