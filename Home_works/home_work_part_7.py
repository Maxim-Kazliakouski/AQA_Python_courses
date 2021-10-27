"""
Home task for the 7th module
"""
print('-' * 30, '1ST TASK', '-' * 30)


def handler_for_input_first_border():
    """
    This function uses for correct input first border
    :return: variable first border
    """
    first_border = None
    while type(first_border) != int:
        try:
            first_border = int(input('Enter first border: '))
        except ValueError:
            print('Error, wrong format!'.upper())
        continue
    return first_border


def handler_for_input_second_border():
    """
    This function uses for correct input second border
    :return: variable second border
    """
    second_border = None
    while type(second_border) != int:
        try:
            second_border = int(input('Enter second border: '))
        except ValueError:
            print('Error, wrong format!'.upper())
        continue
    return second_border


def handler_for_border(first_border, second_border):
    """
    This function uses for correct input of borders
    :param first_border: variable first border
    :param second_border: variable second border
    :return: first border, second border
    """
    while first_border > second_border:
        print('The 1st border can not be more than 2nd!'.upper())
        try:
            first_border = handler_for_input_first_border()
            second_border = handler_for_input_second_border()
            if first_border < second_border:
                break
            else:
                continue
        except ValueError:
            print('Error, wrong format!'.upper())

    return [first_border, second_border]


def generator(first_border=int(handler_for_input_first_border()),
              second_border=int(handler_for_input_second_border())):
    """
    This function uses for adding 100 to input variables
    :param first_border: X
    :param second_border: Y
    :return: list of numbers with adding 100
    """
    if first_border > second_border:
        var_a = handler_for_border(first_border, second_border)
        j = [lambda number: [number + 100 for number in [number for number
                                in [number for number in range(var_a[0], var_a[1] + 1)]]]]
        return j
    else:
        j = [lambda number: [number + 100 for number in [number for number
                                in [number for number in range(first_border, second_border + 1)]]]]
    return j


for i in generator():
    print('Result is following -->', i(()))

print('-' * 30, '2ND TASK', '-' * 30)
gen_list = [x for x in range(1, 10)]


def gen(taken_list):
    """
    This function uses for taking and handling list to display only odd numbers
    :param taken_list: any list
    :return: list with odd numbers
    """
    new_list = list(filter(lambda x: x % 2 != 0, map(int, taken_list)))
    return new_list


print('The list of odd numbers --> ', gen(gen_list))
