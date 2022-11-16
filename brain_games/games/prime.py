from random import randint


GUIDE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            return False
    return True


def generate_round():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
