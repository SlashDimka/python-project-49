import random


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_round():
    question = random.randint(1, 99)
    correct_answer = str(is_even(question))
    return question, correct_answer
