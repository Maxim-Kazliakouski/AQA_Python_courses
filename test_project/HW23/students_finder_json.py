import json
from collections import Counter

with open('../HW23/students.json') as students_json:
    template = json.load(students_json)

from_one_class = {}
most_attended_section = []


def search_by_class_and_section(clas):
    for section in template:
        # print(section)
        for key, value in section.items():
            if key == 'Class' and value == clas:
                from_one_class[section['Name']] = section['Club']
    values = from_one_class.values()
    counter = Counter(values)
    sp_section_and_amount = dict(counter)
    for key, value in sp_section_and_amount.items():
        if value >= 2:
            most_attended_section.append(key)
            print(f'The following students from {clas} class attend sport section {most_attended_section[0].upper()}:')
    try:
        for name, sp_section in from_one_class.items():
            if from_one_class[name] == most_attended_section[0]:
                print('-', name)
    except:
        print(f'There are no students in {clas} class, who attend the same sport section!')


def students_searching_by_gender(gender):
    if gender == 'M':
        print('The list of boys in class:')
    else:
        print('The list of girls in class:')
    for section in template:
        for key, value in section.items():
            if key == 'Gender' and value == gender:
                print('-', section['Name'])


def students_searching_by_the_name(part_of_name):
    names = []
    try:
        for section in template:
            for key, value in section.items():
                if part_of_name.lower() in section['Name'].lower():
                    names.append(section['Name'])
                    break
        if len(names) > 0:
            print(f'There are the following names with "{part_of_name}" word or full name:')
            for i in names:
                print('-', i)
        if len(names) == 0:
            print('There are no students with such part/full name...')
    except:
        print('ERROR')


# students searching by the class, who attend the same sport section
# necessary to enter class: 1a, 1b, 3a, 3b, 5a
search_by_class_and_section('5a')
print('-' * 50)
# sorting by the student gender
# necessary to enter gender: M, W
students_searching_by_gender('M')
print('-' * 50)
# searching by the part or full student name
students_searching_by_the_name('ko')
