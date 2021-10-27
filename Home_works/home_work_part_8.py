"""
Home task for the 7th module
"""
from functools import wraps

print('-' * 30, '1ST TASK', '-' * 30)


def decor_adding_number(taken_func):
    """
    Decor for adding 1
    :param taken_func: func for decor
    :return: wrapper
    """
    def wrapper():
        """
        Wrapper for perfoming changes
        :return: wrapper
        """
        print('Starting wrapper')
        print(f'The result of output --> {taken_func() + 1}')
        print('Ending wrapper...')

    return wrapper


@decor_adding_number
def input_number():
    """
    Func for entering number
    :return: number
    """
    x = int(input('Please, input number: '))
    return x


input_number()

print('-' * 30, '2ND TASK', '-' * 30)


def decor_upper_case(taken_func):
    """
    Decor for uppercase
    :param taken_func: incoming func
    :return: wrapper
    """
    def wrapper():
        print('Starting wrapper')
        print(f'The result of output --> {taken_func().upper()}')
        print('Ending wrapper...')

    return wrapper


@decor_upper_case
def input_text():
    """
    Func for entering text
    :return: text
    """
    x = input('Please, input the text: ')
    return x


input_text()

print('-' * 30, '3RD TASK', '-' * 30)


def change(taken_func):
    """
    func for changing arguments order
    :param taken_func: incoming func
    :return: new func
    """
    @wraps(taken_func)
    def new_func_with_reverse_args(*args):
        """
        Creating new func
        :param args: arguments
        :return: new func
        """
        return taken_func(*args[::-1])

    return new_func_with_reverse_args


@change
def func(a, b, c):
    """
    Func for math operation
    :param a: A
    :param b: B
    :param c: C
    :return: result
    """
    return round((a + b / c), 2)


print('Before converting --> ', func(10, 20, 30))
new_value = change(func)
print('After converting --> ', new_value(10, 20, 30))
