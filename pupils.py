pupils = [{
    'firstname': 'Masha',
    'group': 42,
    'physics': 7,
    'informatics': 6,
    'history': 8

},
    {'firstname': 'Sergei',
    'group': 42,
    'physics': 9,
    'informatics': 10,
    'history': 5},

    {'firstname': 'Ales',
    'group': 42,
    'physics': 4,
    'informatics': 3,
    'history': 3}

]

for pupil in pupils:
    count = 0
    count_1 = 0
    for key, value in pupil.items():
        if key not in ('firstname', 'Group'):
            count += value
            count_1 += 1
    pupil['avg'] = count / count_1

for i in pupils:
    if i['avg'] >= 4:
        print(i['firstname'], i['avg'])
