def yaml(a):
    a = a.replace('"null"', 'qnullq')
    a = a.replace('"None"', 'qNoneq')
    a = a.replace('"', '')
    a = a.replace('\\', '"')

    y = {}
    lines = a.split('\n')

    for l in lines:
        if l == '':
            continue

        d = l.split(':')

        for i in range(len(d)):
            d[i] = d[i].strip()
            if d[i].isdigit():
                d[i] = int(d[i])
            elif d[i] == 'false':
                d[i] = False
            elif d[i] == 'true':
                d[i] = True
            elif d[i] == '' or d[i] == 'null':
                d[i] = None
            elif d[i] == 'qnullq':
                d[i] = 'null'
            elif d[i] == 'qNoneq':
                d[i] = 'None'
            elif d[i] == '' or d[i] == 'null':
                d[i] = None

        y[d[0]] = d[1]

        sorty = {}
        for key in sorted(y):
            sorty[key] = y[key]
        print(sorty)
    return sorty


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")