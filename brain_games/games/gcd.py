from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def game_rule() -> str:
    return 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divides(num_1: int, num_2: int) -> int:
    max_num = max(num_1, num_2)
    min_num = min(num_1, num_2)
    remainder = max_num % min_num

    if remainder == 0:
        return min_num

    return get_greatest_common_divides(min_num, remainder)


def gcd() -> tuple[str, str]:
    num_1 = rnd(range(1, 100))
    num_2 = rnd(range(1, 100))
    question = f'{num_1} {num_2}'
    correct_answer = get_greatest_common_divides(num_1, num_2)
    return (question, str(correct_answer))


def run() -> callable:
    return engine(gcd, game_rule)
