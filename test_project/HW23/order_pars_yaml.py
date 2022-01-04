import yaml
import json
import ruamel.yaml

with open('files_for_parsing/order.yaml') as f:
    my_dict = yaml.safe_load(f)
    # print(my_dict)
print('-' * 25, 'INVOICE', '-' * 25)
for key, value in my_dict.items():
    if key == 'invoice':
        print(f'Invoice number -> ', my_dict[key])
print('-' * 25, 'ADDRESS', '-' * 25)
for key, value in my_dict.items():
    if key == 'bill-to':
        new_dict = my_dict[key]
        for i, j in new_dict.items():
            # if i == 'given':
            #     print(f'Given -> {new_dict[i]}')
            # if i == 'family':
            #     print(f'Family -> {new_dict[i]}')
            if i == 'address':
                address = (new_dict[i])
                for key, value in address.items():
                    if key == 'lines':
                        print(end=f'Lines -> {address[key]}')
                    if key == 'city':
                        print(f'City -> {address[key]}')
                    if key == 'state':
                        print(f'Sate -> {address[key]}')
                    if key == 'postal':
                        print(f'Postal -> {address[key]}')

for key, value in my_dict.items():
    if key == 'product':
        new_dict = my_dict[key]
        dict1item = new_dict[0]
        dict2item = new_dict[1]
        print('-' * 25, 'DESCRIPTION, QUANTITY AND PRICE 1ST ITEM', '-' * 25)
        for key, value in dict1item.items():
            if key == 'description':
                print(f'Description of 1st item: {dict1item[key]}')
            if key == 'quantity':
                print(f'Quantity of 1st item: {dict1item[key]}')
            if key == 'price':
                print(f'Price of 1st item: {dict1item[key]}')
        print('-' * 25, 'DESCRIPTION, QUANTITY AND PRICE 2ND ITEM', '-' * 25)
        for key, value in dict2item.items():
            if key == 'description':
                print(f'Description of 2nd item: {dict2item[key]}')
            if key == 'quantity':
                print(f'Quantity of 2nd item: {dict2item[key]}')
            if key == 'price':
                print(f'Price of 2nd item: {dict2item[key]}')

# converting from YAML to JSON
in_file = 'files_for_parsing/order.yaml'
out_file = 'files_for_parsing/order.json'

yaml = ruamel.yaml.YAML(typ='safe')
with open(in_file) as fpi:
    data = yaml.load(fpi)
with open(out_file, 'w') as fpo:
    json.dump(data, fpo, indent=2)
