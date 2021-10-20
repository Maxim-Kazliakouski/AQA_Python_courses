# guess the number
"""
This game was developing only for educational purposes
and doesn't care out any licenses for using it :)
"""
from random import randint
print(__doc__)
print('-' * 20, 'Guess the number', '-' * 20)
print('Rules of the game:\nYou should guess the'
      ' number from 1 to 100 for 10 ATTEMPTS, by the entering\n'
      'one by one your answer')
ALL_ATTEMPTS = 10
ATTEMPTS = 10
CONFIRMATION = None
random_number = randint(0, 100)
#print(random_number)
YOUR_CHOICE = 0
print('Please, enter "YES", if you understood the rule\n'
      'and want to play or "NO", if you do not want to play\n'
      'and want to exit from the game.\n')
while CONFIRMATION not in ('YES', 'NO'):
    CONFIRMATION = input('Please, enter "YES" or "NO": ').upper()
    if CONFIRMATION not in ('YES', 'NO'):
        print('Please, try again to enter correct answer!')
        continue
    elif CONFIRMATION == 'NO':
        print('GoodBuy!')
        break

    while YOUR_CHOICE != random_number:
        try:
            YOUR_CHOICE = int(input('Please, enter a number from 1 to 100: '))
            ATTEMPTS -= 1
        except ValueError:
            print('You enter wrong format, enter a number!')
            continue
        if YOUR_CHOICE == random_number:
            print('Congratulation, you are win!\n'
                  f'You spent {ALL_ATTEMPTS - ATTEMPTS} '
                  f'attempts from {ALL_ATTEMPTS} for guessing! ')
        if ATTEMPTS == 0:
            print('Unfortunately, you do not guess!! ')
            break
        if YOUR_CHOICE > random_number:
            print('Your answer more than random number! Try to enter less number...')
            print(f'You have left {ATTEMPTS} ATTEMPTS...')
        elif YOUR_CHOICE < random_number:
            print('Your answer less than random number! Try to enter more number...')
            print(f'You have left {ATTEMPTS} ATTEMPTS...')
            continue
