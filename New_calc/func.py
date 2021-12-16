"""
It's module for calculator methods
"""

from main import EnterNumber


class Methods(EnterNumber):
    """
    Class for methods for calculating
    """
    def addition(self):
        """
        Func for addition method
        :return: addition result
        """
        result = EnterNumber.input_number_1st(self) + EnterNumber.input_number_2nd(self)
        print(f'The result of addition --> {round(result,2)}')
        return result

    def subtraction(self):
        """
        Func for subtraction
        :return: subtraction result
        """
        result = EnterNumber.input_number_1st(self) - EnterNumber.input_number_2nd(self)
        print(f'The result of subtraction --> {round(result,2)}')
        return result

    def multiplication(self):
        """
        Func for multiplication
        :return: multiplication result
        """
        result = EnterNumber.input_number_1st(self) * EnterNumber.input_number_2nd(self)
        print(f'The result of multiplication --> {round(result,2)}')
        return result

    def division(self):
        """
        Func for division
        :return: division result
        """
        while ZeroDivisionError:
            try:
                result = EnterNumber.input_number_1st(self) / EnterNumber.input_number_2nd(self)
                print(f'The result of division --> {round(result,2)}')
                break
            except ZeroDivisionError:
                print("ERROR! You can't divide by zero!\nPlease, try again and"
                      " enter another number differ from 0")
                while EnterNumber.input_number_2nd(self) == 0:
                    print('Error!!!')
                    if self.b_1 != 0:
                        return self.b_1
                result = self.a_1 / self.b_1
                print(f'The result of division --> {round(result,2)}')
                break

    def exponentiation(self):
        """
        Func for exponentiation
        :return: exponentiation result
        """
        while ValueError:
            try:
                self.a_1 = float(input('Please, enter the number for exponentiation: '))
                break
            except ValueError:
                print('You entered wrong format for valuable!\n' + 'Please, try again!\n')
        self.b_1 = None
        while ValueError:
            try:
                self.b_1 = float(input('Please, enter degree for number: '))
                break
            except ValueError:
                print('You entered wrong format for valuable!\n' + 'Please, try again!\n')
        result = pow(self.a_1, self.b_1)
        print(f'The exponentiation result --> {round(result, 2)}')
        return result


calc = Methods()
# uncomment string below for addition operation
# calc.addition()
# uncomment string below for subtraction operation
# calc.subtraction()
# uncomment string below for division operation
calc.division()
# uncomment string below for multiplication operation
# calc.multiplication()
# uncomment string below for exponentiation operation
# calc.exponentiation()
