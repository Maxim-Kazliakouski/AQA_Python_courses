"""
App for simple calculating
"""
print('-' * 10, 'CALCULATOR', '-' * 10)


class EnterNumber:
    """
    Class for initializing variable for entering numbers
    """
    def __init__(self):
        self.a_1 = None
        self.b_1 = None

    def input_number_1st(self):
        """
        Method for entering 1st number for calculating
        :return: entering the 1st variable for calculating
        """
        while ValueError:
            try:
                self.a_1 = float(input('Please, input 1st number: '))
                break
            except ValueError:
                print('You entered wrong format for valuable!\n' + 'Please, try again!\n')
        return self.a_1

    def input_number_2nd(self):
        """
        Method for entering 2nd number for calculating
        :return:  entering the 2nd variable for calculating
        """
        while ValueError:
            try:
                self.b_1 = float(input('Please, input 2nd number: '))
                break
            except ValueError:
                print('You entered wrong format for valuable!\n' + 'Please, try again!\n')
        return self.b_1
