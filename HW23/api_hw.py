import requests

# getting author list
# response1 = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
# json_response1 = response1.json()
# for each_element in json_response1:
#     for i, j in each_element.items():
#         print(i, ':', j)  # (necessary uncomment cause of too loong author list)


# getting author by id
def getting_author_by_id(id):
    response2 = requests.get(f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{id}')
    json_response2 = response2.json()
    for i, j in json_response2.items():
        print(f'{i}: {j}')


getting_author_by_id(1)
print('-' * 50)

# creating new book
data = {
    "id": 55,
    "title": "Harry Potter",
    "description": "fantasy book",
    "pageCount": 100,
    "excerpt": "string",
    "publishDate": "2021-12-29T21:30:54.997Z"
}
response3 = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books', json=data)
json_response3 = response3.json()
for i, j in json_response3.items():
    print(f'{i}: {j}')
print('-' * 50)

# creating new user
data = {
    "id": 5,
    "userName": "Max",
    "password": "0509"
}
response4 = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users', json=data)
json_response4 = response4.json()
for i, j in json_response4.items():
    print(f'{i}: {j}')
print('-' * 50)

# changing info about book:
data = {
    "id": 10,
    "title": "Book number 10",
    "description": "short description",
    "pageCount": 50,
    "excerpt": "string",
    "publishDate": "2021-12-29T21:32:44.983Z"
}
response5 = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=data)
json_response5 = response5.json()
for i, j in json_response5.items():
    print(f'{i}: {j}')
print('-' * 50)

# deleting user by id
response6 = requests.delete('https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(f'Satus code is {response6.status_code}')
