"""
The small method for second variant of home work
"""
from random import randint


def entering_number(number=int(input('Please, enter the number from 1 to 5: '))):
    """
    This method uses for choosing number from random list from 1 to 5
    :param number: it's a number, which user enters from keyboard
    :return:
    """
    random_value = randint(1, 5)
    if number == random_value:
        print(f'You are guess the number!\nIt was number {random_value}')
    else:
        print('Sorry, you did not guess, try again latter...')


entering_number()
