"""
Main module for DipDap.

Data structures containing all data to build a forms from.

Genre is the data structure containing all the genre and sub-
genre available. It is a list of tuples.

new_book_form is the form for adding a new book to db.
Generally a book entry should hold the following informaton:
    'title': title,
    'author': author,
    'genre': genre,
    'genre2': genre2,
    'finish_date': finish_date,
    'score': score,
    'comment': comment

To_do:
#-> Dictionary keys for html, GUI and commandline specifics.
#-> Elements grouped under an 'elements' key for better logic.
#-> Genre should be read from a database/file to facilitate modification.
"""

# Don't change the order of these, add to the end! The db works by list index.
genre = [
    ('Fact/textbook', 'Mathematics'),
    ('Fact/textbook', 'Biology'),
    ('Fact/textbook', 'Mechanics'),
    ('Fact/textbook', 'Geekyscience'),
    ('Fact/textbook', 'Aerodynamics'),
    ('Fiction', 'Fantasy'),
    ('Fiction', 'Sci-fi'),
    ('Fiction', 'Detective'),
    ('Fiction', 'Horror'),
    ('Language', 'French'),
    ('Language', 'Arabic'),
    ('Language', 'German'),
    ('Language', 'Swahili'),
    ('Sport', 'Kayaking'),
    ('Sport', 'Climbing'),
    ('Sport', 'Sailing'),
    ('Sport', 'Hiking'),
    ('undef.', 'undef.')
]

new_book_form = (
    './ddcgi.py', # HTML Submit action.
    'post',  # HTML Submit method.
    {
        'element-1': {
            'label': 'Title: ',
            'attributes': {
                'id': 'input_title',
                'class': '',
                'type': 'text',
                'name': 'title',
                'class': 'input',
                'value': ''
            },
            'validation': ['not-empty', 'string'],
            'messages': ''
        },
        'element-2': {
            'label': 'Author: ',
            'attributes': {
                'id': 'input_author',
                'class': '',
                'type': 'text',
                'name': 'author',
                'class': 'input',
                'value': ''
            },
            'validation': ['pass'],
            'messages': 'I am a little message...'

        },
        'element-3': {
            'label': 'Genre: ',
            'attributes': {
                'id': 'input_genre',
                'class': '',
                'type': 'select',
                'name': 'genre',
                'class': 'input_select',
                'options': genre
            },
            'validation': ['not-empty', 'select-list'],
            'messages': 'Fool! IT cannot be empty.'
        }
    }
)


# genre = {
#     1: {
#         'title': 'Fact/textbook',
#         1: 'Mathematics',
#         2: 'Biology',
#         3: 'Mechanics',
#         4: 'Geekyscience'
#         5: 'Aerodynamics'
#     },
#     2: {
#         'title': 'Fiction',
#         1: 'Fantasy',
#         2: 'Sci-fi',
#         3: 'Detective',
#         4: 'Horror'
#     },
#     3: {
#         'title': 'Dictionary'
#         1: 'French',
#         2: 'Arabic',
#         3: 'German',
#         4: 'Swahili'
#     },
#     4: {
#         'title': 'Sport',
#         1: 'Kayaking',
#         2: 'Climbing',
#         3: 'Sailing',
#         4: 'Hiking'
#     }
    
# }
