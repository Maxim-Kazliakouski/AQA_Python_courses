import xml.etree.cElementTree as ET
from datetime import datetime
from bs4 import BeautifulSoup

book_id_list = []
sorted_dict = {}
tree = ET.parse('task.xml')
root = tree.getroot()


def tag_text(tag):
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


# generating list of book name (title)
tag_text('title')

# generating list of book price
tag_text('price')

# converting price string to the integer
price_int = [float(x) for x in tag_text('price')]
# making dictionary book name and price
book_price = dict(zip(tag_text('title'), price_int))
# sorting the books by the price
sorted_keys = sorted(book_price, key=book_price.get)
for w in sorted_keys:
    sorted_dict[w] = book_price[w]

print('Sorting by the price: from the lowest to the highest'.upper())
for key in sorted_dict:
    print(f'The book name is {key} -> {sorted_dict[key]}$')

# parsing id attribute front tag book
with open('task.xml') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'lxml')

for element in results.find_all("catalog"):
    for stat in element.find_all("book"):
        book_id_list.append(stat['id'])
print('-' * 50)
# combining id with book name
book_and_id = dict(zip(tag_text('title'), book_id_list))
print('Book and ID:'.upper())
for key in book_and_id:
    print(f'ID of {key} -> {book_and_id[key]}')

# the amount of all books:
print('-' * 50)
print('the amount of all books'.upper())
print(f'The amount of all book is: {len(book_id_list)}')

# generating book list by date
tag_text('publish_date')

# sorted date book list by date
print('-' * 50)
print('books sorting by the date:'.upper())
tag_text('publish_date').sort(key=lambda d: datetime.strptime(d, '%Y-%m-%d'))
for each_date in tag_text('publish_date'):
    print(each_date)

# making dict with title and book date
dict_with_title_and_dates = dict(zip(find_tag_by_inner_text('publish_date', '2000'), tag_text('title')))
# printing book which produced in 2000
print('-' * 50)
print('books have been produced in 2000:'.upper())
for key in dict_with_title_and_dates:
    if '2000' in key:
        print(key, dict_with_title_and_dates[key])

# info for book with genre Computer
with open('task.xml') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'lxml')
print('-' * 50)
print('Books with genre Computer:'.upper())
for element in results.find_all("book"):
    for stat in element.find_all("genre"):
        if stat.text == 'Computer':
            print(element.text)
