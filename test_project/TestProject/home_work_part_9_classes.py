"""
Class work about class
"""
from collections import OrderedDict

list_of_students = []
students_with_certain_mark = []
list_of_names_by_group = []
marks_list_1 = []
average_grade_list = []


class Students:
    """
    Class for students
    """

    def __init__(self, first_name, last_name, *args):
        self.grades = {'1st student': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7},
                       '2nd student': {'Math': 0, 'Language': 1, 'Physics': 2, 'Fiz': 3, 'IT': 4},
                       '3rd student': {'Math': 9, 'Language': 10, 'Physics': 5, 'Fiz': 4, 'IT': 8},
                       '4th student': {'Math': 9, 'Language': 9, 'Physics': 9, 'Fiz': 7, 'IT': 6},
                       '5th student': {'Math': 4, 'Language': 5, 'Physics': 7, 'Fiz': 5, 'IT': 5}}
        self.first_name = first_name
        self.last_name = last_name
        self.group = [0, 1, 2, 3, 4, 5]
        self.args = args


class School(Students):
    """
    Class for School
    """

    def adding_students_into_the_group(self, group, grades):
        """
        The func for adding students into the group
        :param group: group
        :param grades: grades
        :return: list of students
        """
        print(f'The first name of student: {self.first_name}')
        print(f'The last name of student: {self.last_name}')
        print(f'The group of student: {self.group[group]}')
        print(f'The grades of student: {self.grades[grades]}')
        student = {'Group: ' + str(self.group[group]):
                       {(self.first_name + ' ' + self.last_name): self.grades[grades]}}
        list_of_students.append(student)
        return list_of_students


def sorting_students_by_the_marks_and_groups(mark1, mark2):
    """
    The func for sorting students by the marks and groups
    :param mark1: mark 1
    :param mark2: mark 2
    :return: the list of students, which have 5 and 6 mark
    """
    for each_student in list_of_students:
        # print(each_student)
        for group, students_def in each_student.items():
            # print(students_def)
            for name, grades in students_def.items():
                for each_mark in grades.items():
                    if mark1 or mark2 in each_mark:
                        students_with_certain_mark.append(name + ' from ' + group.lower())
    if len(students_with_certain_mark) > 0:
        print(f'There list of students and their groups, which have'
              f' {mark1} or {mark2} marks: \n'.upper() +
              f'and there are only {len(set(students_with_certain_mark))} students:'.upper())
    else:
        print('There are no such students!')
    return students_with_certain_mark


def students_sorting_by_group(group):
    """
    The func for sorting students by group
    :param group: group
    :return: The students and group the are belonged
    """
    if group not in range(0, 6):
        print(f'There is no any students in {group} group or this group did not create...')
    else:
        for each_student in list_of_students:
            # print(each_student)
            for group_in_list, students_1 in each_student.items():
                # print(group)
                if group_in_list == f'Group: {group}':
                    for name in students_1.items():
                        list_of_names_by_group.append(name)
        print(f'The list of {group} group: '.upper())
        for name in list_of_names_by_group:
            print(name)
    return list_of_names_by_group


# добавление студентов
# print('-' * 50)
# print('adding students: '.upper())
# student_1 = School('Max', 'Kazliakouski', 0, '1st student')
# adding_1_student = student_1.adding_students_into_the_group(0, '1st student')
# print(adding_1_student)
# print('-' * 50)

# student_2 = School('Nick', 'Balen', 1, '2nd student')
# adding_2_student = student_2.adding_students_into_the_group(1, '2nd student')
# print(adding_2_student)
# print('-' * 50)

# student_3 = School('Konor', 'McDavid', 3, '3rd student')
# adding_3_student = student_3.adding_students_into_the_group(3, '3rd student')
# print('-' * 50)
#
# student_4 = School('Alex', 'Draizatel', 4, '4th student')
# adding_4_student = student_4.adding_students_into_the_group(4, '4th student')
# print('-' * 50)
#
# student_5 = School('Jack', 'Russel', 5, '5th student')
# adding_5_student = student_5.adding_students_into_the_group(1, '5th student')
# print('-' * 50)

# outputting the list of students, who has 5 and 6 mark
# print(' \n'.join(list(OrderedDict.fromkeys(sorting_students_by_the_marks_and_groups(5, 6)))))
# print('-' * 50)

# outputting students by group only
# print('0'*50)
# students_sorting_by_group(0)
# print('-' * 50)


# function for defining all marks
def all_marks():
    """
    The func for getting all marks
    :return: list of all marks
    """
    for each_student in list_of_students:
        # print(each_student)
        for group, students_def in each_student.items():
            # print(Students_def)
            for name_1, grades in students_def.items():
                # print(Grades)
                for discipline, mark in grades.items():
                    for name_2 in students_def.items():
                        marks_list_1.append(mark)
                        # print(marks_list)
    return marks_list_1


# decor for computing average grade
def decor_for_average_grade(taken_func):
    """
    decor for computing the average grade
    :param taken_func: taken func
    :return: wrapper
    """

    def wrapper(student_number):
        result = sum(taken_func(student_number)) / len(taken_func(student_number))
        print(f'The average grade of {student_number} student is {result}')
        average_grade_dict = {student_number: result}
        average_grade_list.append(average_grade_dict)
        # print(average_grade_dict)
    return wrapper


@decor_for_average_grade
# function for defining marks for certain student
def marks_of_each_student(chosen_student_def):
    """
    The func for computing the marks of every student
    :param chosen_student_def: last name of student from the previous funcs
    :return: marks for certain student
    """
    all_marks()
    if chosen_student_def in (1, 'Kazliakouski'):
        return marks_list_1[:5]
    if chosen_student_def in (1, 'Balen'):
        return marks_list_1[5:10]
    if chosen_student_def in (3, 'McDavid'):
        return marks_list_1[10:15]
    if chosen_student_def in (4, 'Draizatel'):
        return marks_list_1[15:20]
    if chosen_student_def in (5, 'Russel'):
        return marks_list_1[20:25]


# writing average grade and last name into the dictionary
print('outputting the average grade by student last name'.upper())
# marks_of_each_student(student_1.last_name)
# marks_of_each_student(student_2.last_name)
# marks_of_each_student(student_3.last_name)
# marks_of_each_student(student_4.last_name)
# marks_of_each_student(student_5.last_name)
# print(average_grade_list)
print('-' * 50)
print('The list of students, who deserves autograde (average grade >= 7): '.upper())
for data in average_grade_list:
    # print(data)
    for last_name_1, grade in data.items():
        # print(Grade)
        if grade >= 7:
            print(last_name_1)

# outputting the average grade by student last name
print('-' * 50)
