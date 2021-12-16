# test data for cases
class Test_data:
    # for positive cases:
    DATA_FOR_ADD_1ST_STUDENT = [{
        'Group: 0': {'Max Kazliakouski': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    INCORRECT_DATA_FOR_ADD_1ST_STUDENT = [{
        'Group: 0': {'Max Kazliakouski': {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7}}}]
    FIRSTNAMES_SET = ['Max', 'Alex', 'Conor']
    LASTNAMES_SET = ['Ivanov', 'McDavid', 'Backstrom']
    STUDENTS_GRADES = [
        ('Max', 'Kazliakouski', '1st student', 0),  # 1st test dara
        ('David', 'Macmillan', '2nd student', 1),  # 2nd test data
        ('Oscar', 'Balen', '3rd student', 2)  # 3rd test data
    ]

    # # for negative cases:
    DATA_FOR_SORTING_STUDENTS = ['Max Kazliakouski from group: 0', 'Nick Balen from group: 1']
    DATA_FOR_SORTING_BY_GROUP = [('Max Kazliakouski', {'Math': 4, 'Language': 6, 'Physics': 9, 'Fiz': 10, 'IT': 7})]
    STUDENT_MARK = "l';The average grade of Kazliakouski student is 7.2"
