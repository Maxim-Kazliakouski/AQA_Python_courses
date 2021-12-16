import pytest


@pytest.fixture(autouse=True)
def printing_name_case():
    print('\nStarting new positive case...')
    list_of_students = []
    students_with_certain_mark = []
    list_of_names_by_group = []
    marks_list_1 = []
    average_grade_list = []
    yield
    print('\nEnding new positive case...')
