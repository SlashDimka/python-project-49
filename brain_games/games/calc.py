import operator
import random
GUIDE = 'What is the result of the expression?'
operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator_symb = random.choice(list(operators))
    question = f"{number1} {operator_symb} {number2}"
    correct_answer = str(operators.get(operator_symb)(number1, number2))
    return question, correct_answer
