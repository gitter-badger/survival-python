cases = [
    {
        'description': 'Empty String',
        'value': ''
    },
    {
        'description': 'Non-empty String',
        'value': 'Not empty'
    },
    {
        'description': 'Empty List',
        'value': []
    },
    {
        'description': 'Non-empty List',
        'value': [1]
    },
    {
        'description': 'Empty Dictionary',
        'value': {}
    },
    {
        'description': 'Non-empty Dictionary',
        'value': {'name': 'Tony'}
    },
    {
        'description': 'Integer Zero',
        'value': 0
    },
    {
        'description': 'Integer One',
        'value': 1
    },
    {
        'description': 'Non-zero, non-one, Integer',
        'value': 2
    },
]

for case in cases:
    if case['value']:
        print('{} --> True'.format(case['description']))
    else:
        print('{} --> False'.format(case['description']))