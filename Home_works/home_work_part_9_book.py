"""
App for rented, booking and taking the book
"""
# book statuses
is_booked = ['False']
is_taken = ['False']
is_returned = ['True']
who_take_book = ['Nobody']
# dictionary with Book:User_name type
book_user = {}


class Book:
    """
    Class for initiating variables
    """
    def __init__(self, book_name, book_author, book_pages):
        self.book_name = book_name
        self.book_author = book_author
        self.book_pages = book_pages


class Reader(Book):
    """
    Class about reader and book
    """
    def take_book(self, reader_name):
        """
        The func for taking book operation
        :param reader_name: Reader name
        :return: result of operations by book
        """
        if is_booked[0] == 'True' and is_returned[0] == 'False' and is_taken[0] == 'False':
            print(f'This book has already booked by {who_take_book[0]}')
        elif is_taken[0] == 'True' and is_booked[0] == 'False' and is_returned[0] == 'False':
            print(f'This book has already taken by {who_take_book[0]}')
        elif is_returned[0] == 'True' and is_booked[0] == 'False' and is_taken[0] == 'False':
            print(f'{reader_name} you can take or booking the book -->'
                  f' {self.book_name}!\nDo you want '
                  f'book or take this book?')
            action = input('Please, make you choice: ').lower()
            while action not in ('book', 'take'):
                print('Please, choose only BOOK or TAKE!')
                action = input('Please, make you choice: ').lower()
            if action == 'book':
                print(f'{reader_name}, you are booked the {self.book_name} book!\n')
                is_booked[0] = 'True'
                is_returned[0] = 'False'
                book_user[self.book_name] = reader_name
            elif action == 'take':
                print(f'{reader_name}, you are taking the {self.book_name} book!\n')
                is_taken[0] = 'True'
                is_returned[0] = 'False'
                book_user[self.book_name] = reader_name
        who_take_book[0] = reader_name

    def return_book(self, reader_name):
        """
        Func for returning the book
        :param reader_name: Reader name
        :return: result of operations by book
        """
        if reader_name == book_user[self.book_name]:
            is_returned[0] = 'True'
            is_booked[0] = 'False'
            is_taken[0] = 'False'
            print(f'The {self.book_name} is free now\n')


# taking a book
Reader('Harry Potter', 'J.k.Rolling', 220).take_book('Max')

# returning the book
# Reader('Harry Potter', 'J.k.Rolling', 220).return_book('Max')

# who take the book and which(Book:Name)?
# print(book_user)

# taking a book by the 2nd reader if it's free
Reader('Harry Potter', 'J.k.Rolling', 220).take_book('Alex')
