from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    half_num = int(num / 2)
    divider = 2
    while divider <= half_num:
        if num % divider == 0:
            return False
        divider += 1
    return True


def game_rule() -> str:
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime() -> tuple[str, str]:
    question = rnd(range(1, 100))
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def run() -> callable:
    return engine(prime, game_rule)
