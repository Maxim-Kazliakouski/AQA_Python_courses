# test data for cases
class Test_data:
    # for positive cases:
    DATA_FOR_ADD_1ST_STUDENT = [{
        'Group: 0': {'Max Kazliakouski': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    INCORRECT_DATA_FOR_ADD_1ST_STUDENT = [{
        'Group: 0': {'Max Kazliakouski': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    FIRSTNAMES_SET = ['Max']
    CHECKING_FOR_1ST_STUDENT = [{'Group: 0': {'Max Ivanov': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    CHECKING_FOR_2ND_STUDENT = [{'Group: 0': {'McDavid Ivanov': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    CHECKING_GRADES_FOR_1ST_STUDENT = [{'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}]
    # STUDENT_FOR_1ST_GROUP =


    LASTNAMES_SET = ['McDavid']
    STUDENTS_GRADES = [
        ('Max', 'Kazliakouski', '1st student', 0),  # 1st test dara
    ]

    # # for negative cases:
    DATA_FOR_SORTING_STUDENTS = ['Max Kazliakouski from group: 0', 'Nick Balen from group: 1']
    DATA_FOR_SORTING_BY_GROUP = [('Max Kazliakouski', {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7})]
    STUDENT_MARK = "l';The average grade of Kazliakouski student is 7.2"
