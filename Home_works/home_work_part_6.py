"""
Home task for the 6th module
"""
print('-' * 30, '1ST TASK', '-' * 30)
entering_list = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [abs(x) for x in entering_list]
print(new_list, '\n')

print('-' * 30, '2ND TASK', '-' * 30, '\n')
name_list = ('Max', 'Alex', 'John', 'Nick', 'Steve', 'Conor')
numbers = (x for x in range(1, 100))
# month = (day for day in range(1, 32))
# for day in month:
#     print(day)
grouping_list = dict(zip(numbers, name_list))
print('The dictionary with serial numbers of people', grouping_list, '\n')

duty_roster = [name1 + ' - ' + str(day) + ' September' for day in (day for day in range(1, 32))
               if day <= 5 for name1 in name_list if name1 == 'Max'], \
              [name2 + ' - ' + str(day) + ' September' for day in (day for day in range(1, 32))
               if 6 <= day < 11 for name2 in name_list if name2 == 'Alex'], \
              [name3 + ' - ' + str(day) + ' September' for day in (day for day in range(1, 32))
               if 11 <= day < 16 for name3 in name_list if name3 == 'John'], \
              [name4 + ' - ' + str(day) + ' September' for day in (day for day in range(1, 32))
               if 16 <= day < 21 for name4 in name_list if name4 == 'Nick'], \
              [name5 + ' - ' + str(day) + ' September' for day in (day for day in range(1, 32))
               if 21 <= day < 26 for name5 in name_list if name5 == 'Steve']

# using loop for more comfortable and readable output
print('-' * 35, 'The schedule for duty roster on September:', '-' * 35)
for position in duty_roster:
    print(position)

print('-' * 30, '2ND TASK', '-' * 30, '\n')
SENTENCE = "the quick brown fox jumps over the lazy dog"
new_list_just_numbers = [len(word) for word in SENTENCE.split(' ') if word != 'the']
new_list_with_describes = [word.upper() + ' consists of ' + str(len(word)) + ' letters'
                           for word in SENTENCE.split(' ') if word != 'the']
print('The list contains number of letters for each word -->', new_list_just_numbers, '\n')
# print(new_list_with_describes, '\n')
# using loop for more comfortable and readable output
for word in new_list_with_describes:
    print(word)
