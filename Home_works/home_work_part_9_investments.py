"""
App for investments calculating
"""
print('-'*30, 'Investments'.upper(), '-'*30)


def _decorator(taken_func):
    """
    Decor for wrapping function for more information about deposit
    :param taken_func: user_count
    :return: wrapper with info about deposit
    """
    def wrapper(self):
        print('Full info about deposit:'.upper())
        print(f'Contribution sum is {self.sum_inv}$')
        print(f'Period for deposit is {self.period} months or'
              f' {round(self.period / 12, 1)} year(s)')
        print(f'Interest rate is {self.interest_rate}%')
        print(f'Deposit sum is {self.deposit()}$\n')
        return taken_func(self)
    return wrapper


class Investment:
    """
    Class for initiating variables
    """
    def __init__(self, sum_inv, period, interest_rate):
        self.sum_inv = sum_inv
        self.period = period
        self.interest_rate = interest_rate

    def deposit(self):
        """
        Func for deposit calculating
        :return: monthly profit
        """
        month_profit = round((self.sum_inv * self.period
                              * (1 / 12) * self.interest_rate / 100), 2)
        return month_profit


class Bank(Investment):
    """
    Class for displaying user count
    """
    # without decorator will be less info about deposit (you turn off/on decor for visibility)
    @_decorator
    def user_count(self):
        """
        Func for calculating user count
        :return: info about user count
        """
        user_count_var = f'Your count is {self.deposit()}$ for {self.period}' \
                         f' months (or {round(self.period / 12, 1)}' \
                         f' year(s)) with an investment of {self.sum_inv}$' \
                         f' with interest rate equals {self.interest_rate}%'
        print('SHORT info about deposit:'.upper(), f'\n{user_count_var}')


invest = Bank(1230, 7, 8)
invest.user_count()
