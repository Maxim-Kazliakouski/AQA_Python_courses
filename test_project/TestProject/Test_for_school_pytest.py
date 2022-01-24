import data_school
from data_school import Test_data
from home_work_part_9_classes import School
from collections import OrderedDict
import home_work_part_9_classes
import pytest


@pytest.mark.positive
class Test_positive:
    # @pytest.fixture(autouse=True)
    def test_adding_student(self):
        assert School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student') == \
               Test_data.DATA_FOR_ADD_1ST_STUDENT, 'Error! Student not created'

    def test_sorting_only_by_group(self):
        # (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        # (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        assert home_work_part_9_classes.students_sorting_by_group(
            0) == Test_data.DATA_FOR_SORTING_BY_GROUP, 'Error! There is no such group'

    def test_sorting_students_by_the_marks_and_groups(self):
        (School('Max', 'Kazliakouski', 0, '1st student').adding_students_into_the_group(0, '1st student'))
        (School('Nick', 'Balen', 1, '2nd student').adding_students_into_the_group(1, '2nd student'))
        assert list(OrderedDict.fromkeys(home_work_part_9_classes.sorting_students_by_the_marks_and_groups(5, 6))) \
               == Test_data.DATA_FOR_SORTING_STUDENTS, 'Error, sorting does not work'
        home_work_part_9_classes.list_of_students.clear()

    @pytest.mark.parametrize('firstname', data_school.Test_data.FIRSTNAMES_SET)
    def test_firstname(self, firstname):
        student1 = School(firstname, 'Ivanov', 0, '1st student')
        adding_1_student = student1.adding_students_into_the_group(0, '1st student')
        assert adding_1_student == Test_data.CHECKING_FOR_1ST_STUDENT, 'The firstname does not appear!'
        home_work_part_9_classes.list_of_students.clear()

    @pytest.mark.parametrize('lastname', data_school.Test_data.LASTNAMES_SET)
    def test_lastname(self, lastname):
        student2 = School(lastname, 'Ivanov', 0, '1st student')
        adding_2_student = student2.adding_students_into_the_group(0, '1st student')
        assert adding_2_student == Test_data.CHECKING_FOR_2ND_STUDENT, 'The lastname does not appear!'
        home_work_part_9_classes.list_of_students.clear()

    @pytest.mark.parametrize('firstname,lastname,students,group', data_school.Test_data.STUDENTS_GRADES)
    def test_grades(self, firstname, lastname, students, group):
        mark_1st_student = School(firstname, lastname, group, students).adding_students_into_the_group(group, students)
        slovar = mark_1st_student[0]
        marks = []
        for i, k in slovar.items():
            for j, l in k.items():
                marks.append(l)
        assert marks == Test_data.CHECKING_GRADES_FOR_1ST_STUDENT, 'There is no such marks!'


@pytest.mark.negative
class Test_negative:
    def test_group(self):
        try:
            student_in_first_group = School('Max', 'Kazliakouski', 10, '1st student').adding_students_into_the_group(10,
                                                                                                                     '1st student')
        except:
            student_in_first_group = 'There are no such group'
        assert student_in_first_group == 'There are no such group', 'Student was added into the group'

    @pytest.mark.skip
    def test_firstname(self):
        try:
            without_firstname = School('Kazliakouski', 0, '1st student').adding_students_into_the_group(0,
                                                                                                        '1st student')
        except:
            without_firstname = 'The student has no firstname'

        assert without_firstname == 'The student has no firstname', 'The student has all info about last and first name'

    def test_lastname(self):
        try:
            without_lastname = School('Max', 0, '1st student').adding_students_into_the_group(0, '1st student')
        except:
            without_lastname = 'The student has no lastname'
        assert without_lastname == 'The student has no lastname', 'The student has all info about last and first name'
