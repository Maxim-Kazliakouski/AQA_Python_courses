import unittest
import data_school
from home_work_part_9_classes import School
from collections import OrderedDict
import home_work_part_9_classes


class Test_suit_positive_tests(unittest.TestCase):
    def setUp(self):
        print('\nNew positive test...')

    def test_sorting_students_by_the_marks_and_groups(self):
        # precondition for case
        (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        # case
        self.assertEqual(
            list(OrderedDict.fromkeys(home_work_part_9_classes.sorting_students_by_the_marks_and_groups(5, 6))),
            data_school.Test_data.DATA_FOR_SORTING_STUDENTS, '\nError, sorting does not work')

    def test_sorting_only_by_group(self):
        (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        self.assertEqual(home_work_part_9_classes.students_sorting_by_group(0),
                         data_school.Test_data.DATA_FOR_SORTING_BY_GROUP, '\nError! There is no such group!')


    def test_adding_student(self):
        self.assertEqual(
            (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student')),
            data_school.Test_data.DATA_FOR_ADD_1ST_STUDENT, '\nError! Student not created')
        # print(School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))

    def tearDown(self):
        home_work_part_9_classes.list_of_students = []


class Test_suit_negative_tests(unittest.TestCase):
    def setUp(self):
        print('\nNew negative test...')

    def test_group(self):
        try:
            (School('Max', 'Kazliakouski', 10, '1st student').adding_students_into_the_group(10, '1st student'))
        except:
            raise AssertionError('There is no such group')

    def test_firstname(self):
        try:
            (School('Kazliakouski', 0, '1st student').adding_students_into_the_group(10, '1st student'))
        except:
            raise AssertionError('The first name of student is missed')

    def test_lastname(self):
        try:
            (School('Max', 0, '1st student').adding_students_into_the_group(10, '1st student'))
        except:
            raise AssertionError('The lastname of student is missed')

    def test_grades(self):
        try:
            (School('Max', 0, '1st student').adding_students_into_the_group(10, '10st student'))
        except:
            raise AssertionError('There is no student with such marks')

    def tearDown(self):
        home_work_part_9_classes.list_of_students = []
