import xml.etree.cElementTree as ET

info = []
tree = ET.parse('files_for_parsing/library.xml')
root = tree.getroot()


def tag_name(tag):
    x = f'{tag}_list'
    globals()[x] = []
    for elem in root:
        for subelem in elem:
            if subelem.tag == tag:
                globals()[x].append(subelem.text)
    return globals()[x]


def find_tag_by_inner_text(tag, inner_text):
    x = f'{tag}_list'
    globals()[x] = []
    for elem in root:
        for subelem in elem:
            if subelem.tag == tag:
                if inner_text in subelem.text:
                    globals()[x].append(subelem.text)
    return globals()[x]


def collecting_info_for_book(number_of_book):
    print(f'Title of book: {tag_name("title")[number_of_book]}')
    print(f'The price of book: {tag_name("price")[number_of_book]}$')
    print(f'The author of book: {tag_name("author")[number_of_book]}')
    print(f'The description of book: {tag_name("description")[number_of_book]}')


def book_title(number_of_book):
    title = tag_name("title")[number_of_book]
    return title.split()


def book_price(number_of_book):
    price = tag_name("price")[number_of_book]
    return price.split()


def book_author(number_of_book):
    author = tag_name("author")[number_of_book]
    return author.split()


def book_description(number_of_book):
    description = tag_name("description")[number_of_book]
    return description.split()


def book_search(searching_world):
    for book in range(int(len(tag_name('title')))):
        if searching_world in ' '.join(book_title(book)):
            collecting_info_for_book(book)
            info.append(f'there if info about book {book}')
            break
        elif searching_world in ''.join(book_author(book)).lower():
            collecting_info_for_book(book)
            info.append(f'there if info about book {book}')
            break
        elif searching_world in ''.join(book_price(book)).lower():
            collecting_info_for_book(book)
            info.append(f'there if info about book {book}')
            break
        elif searching_world in book_description(book):
            collecting_info_for_book(book)
            info.append(f'there if info about book {book}')
            break
    if len(info) == 0:
        print('There is no such book, which consists of such word...')


book_search("XML Developer's Guide")  # searching by full tittle
print('-' * 50)
book_search('lls')  # searching by part of AUTHOR name
print('-' * 50)
book_search('36.75')  # searching by book price
print('-' * 50)
book_search('World')  # searching by word from description
