from brain_games.utils.rnd import rnd
from brain_games.engine import engine


def game_rule() -> str:
    return 'What is the result of the expression?'


def calc() -> tuple[str, str]:
    operators = ['+', '-', '*']
    operand_1 = rnd(range(1, 100))
    operand_2 = rnd(range(1, 100))
    random_index = rnd(range(0, 2))
    operator = operators[random_index]

    question = f'{operand_1} {operator} {operand_2}'

    match operator:
        case '+':
            correct_answer = operand_1 + operand_2
        case '-':
            correct_answer = operand_1 - operand_2
        case '*':
            correct_answer = operand_1 * operand_2
        case _:
            correct_answer = None

    return (question, str(correct_answer))


def run() -> callable:
    return engine(calc, game_rule)
