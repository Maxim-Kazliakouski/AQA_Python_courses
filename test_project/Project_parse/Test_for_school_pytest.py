from home_work_part_9_classes import School
from collections import OrderedDict
import home_work_part_9_classes
import pytest
from conftest import parser


@pytest.mark.positive
class Test_positive:
    # @pytest.fixture(autouse=True)
    def test_adding_student(self):
        assert str(School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student')) == \
               parser('for positive cases', 'DATA_FOR_ADD_1ST_STUDENT'), 'Error! Student not created'

    def test_sorting_only_by_group(self):
        # (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        # (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        assert str(home_work_part_9_classes.students_sorting_by_group(
            0)) == parser('for positive cases', 'DATA_FOR_SORTING_BY_GROUP'), 'Error! There is no such group'

    def test_sorting_students_by_the_marks_and_groups(self):
        (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        assert str(list(OrderedDict.fromkeys(home_work_part_9_classes.sorting_students_by_the_marks_and_groups(5, 6)))) \
               == parser('for positive cases', 'DATA_FOR_SORTING_STUDENTS'), 'Error, sorting does not work'

    @pytest.mark.parametrize('firstname', parser('for positive cases', 'FIRSTNAMES_SET').split(','))
    def test_firstname(self, firstname):
        try:
            School(firstname, 'Ivanov', 0, '1st student').adding_students_into_the_group(0, '1st student')
        except:
            raise AssertionError('The first name of student is missed')

    @pytest.mark.parametrize('lastname', parser('for positive cases', 'LASTNAMES_SET').split(','))
    def test_lastname(self, lastname):
        try:
            School('Max', lastname, 1, '2nd student').adding_students_into_the_group(1, '2nd student')
        except:
            raise AssertionError('The lastname of student is missed')

    @pytest.mark.parametrize('students', (parser('for positive cases', 'STUDENTS_GRADES')).split(','))
    def test_grades(self, students):
        try:
            School('Max', 'Kazliakouski', 0, students).adding_students_into_the_group(0, students)
        except:
            raise AssertionError('There is no student with such marks')


@pytest.mark.negative
class Test_negative:
    def test_group(self):
        try:
            School('Max', 'Kazliakouski', 10, '1st student').adding_students_into_the_group(10, '1st student')
        except:
            raise AssertionError('There is no such group')

    @pytest.mark.skip
    def test_firstname(self):
        try:
            School('Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student')
        except:
            raise AssertionError('The first name of student is missed')

    def test_lastname(self):
        try:
            School('Max', 0, '1st student').adding_students_into_the_group(10, '1st student')
        except:
            raise AssertionError('The lastname of student is missed')

    def test_grades(self):
        try:
            School('Max', 'Kazliakouski', 0, '10th student').adding_students_into_the_group(0, '1th student')
        except:
            raise AssertionError('There is no student with such marks')
