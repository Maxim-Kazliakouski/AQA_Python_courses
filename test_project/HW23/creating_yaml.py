import yaml

dict_file = {'name': 'Max Kazliakouski',
             'job': 'Testser',
             'company': 'Oxagile',
             'work_sphere': 'IT',
             'employed': True,
             'skills': ['Manual testing', 'API', 'Bug report', 'Sniffers'],
             'languages': {'native': 'Russian',
                           'foreign': 'English',
                           'program_lang': 'Python'},
             'hobbies': {1: 'Sport',
                         2: 'Music',
                         3: 'Self-education',
                         4: 'Healthy lifestyle'}
             }

with open('../HW23/files_for_parsing/store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
