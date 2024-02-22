from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def game_rule() -> str:
    return 'What number is missing in the progression?'


def progression() -> tuple[str, str]:
    start = rnd(range(1, 100))
    length = 10
    step = rnd(range(1, 10))
    end = start + (length - 1) * step
    hide_symbol = '..'
    random_index = rnd(range(0, length - 1))
    progression = list(range(start, end, step))
    correct_answer = progression[random_index]
    question = []

    for element in progression:
        if element == correct_answer:
            question.append(hide_symbol)
            continue
        question.append(str(element))

    return (' '.join(question), str(correct_answer))


def run() -> callable:
    return engine(progression, game_rule)
