from math import sqrt

numeral_converter = \
    {
        '[0, 3, 7]': 'i',
        '[0, 4, 7]': 'I',

        '[1, 4, 8]': r'$\flat$ii',
        '[1, 5, 8]': r'$\flat$II',

        '[2, 5, 9]': 'ii',
        '[2, 6, 9]': 'II',

        '[3, 6, 10]': r'$\flat$iii',
        '[3, 7, 10]': r'$\flat$III',

        '[4, 7, 11]': 'iii',
        '[4, 8, 11]': 'III',

        '[0, 5, 8]': 'iv',
        '[0, 5, 9]': 'IV',

        '[1, 6, 9]': r'$\sharp$iv',
        '[1, 6, 10]': r'$\sharp$IV',

        '[2, 7, 10]': 'v',
        '[2, 7, 11]': 'V',

        '[3, 8, 11]': r'$\flat$vi',
        '[0, 3, 8]': r'$\flat$VI',

        '[0, 4, 9]': 'vi',
        '[1, 4, 9]': 'VI',

        '[1, 5, 10]': r'$\flat$vii',
        '[2, 5, 10]': r'$\flat$VII',

        '[2, 6, 11]': 'vii',
        '[3, 6, 11]': 'VII'
    }

numeral_converter_plain = \
    {
        '[0, 3, 7]': 'i',
        '[0, 4, 7]': 'I',

        '[1, 4, 8]': 'bii',
        '[1, 5, 8]': 'bII',

        '[2, 5, 9]': 'ii',
        '[2, 6, 9]': 'II',

        '[3, 6, 10]': 'biii',
        '[3, 7, 10]': 'bIII',

        '[4, 7, 11]': 'iii',
        '[4, 8, 11]': 'III',

        '[0, 5, 8]': 'iv',
        '[0, 5, 9]': 'IV',

        '[1, 6, 9]': '#iv',
        '[1, 6, 10]': '#IV',

        '[2, 7, 10]': 'v',
        '[2, 7, 11]': 'V',

        '[3, 8, 11]': 'bvi',
        '[0, 3, 8]': 'bVI',

        '[0, 4, 9]': 'vi',
        '[1, 4, 9]': 'VI',

        '[1, 5, 10]': 'bvii',
        '[2, 5, 10]': 'bVII',

        '[2, 6, 11]': 'vii',
        '[3, 6, 11]': 'VII'
    }

numerals = ['I', 'i', r'$\flat$II', r'$\flat$ii', 'II', 'ii',
            r'$\flat$III', r'$\flat$iii', 'III', 'iii', 'IV', 'iv',
            r'$\sharp$IV', r'$\sharp$iv', 'V', 'v', r'$\flat$VI', r'$\flat$vi',
            'VI', 'vi', r'$\flat$VII', r'$\flat$vii', 'VII', 'vii']

fifth_numerals = [r'$\flat$II', r'$\flat$ii', r'$\flat$VI', r'$\flat$vi', r'$\flat$III', r'$\flat$iii', r'$\flat$VII', r'$\flat$vii', 'IV', 'iv', 'I', 'i', 'V', 'v', 'II', 'ii', 'VI', 'vi', 'III', 'iii', 'VII', 'vii', r'$\sharp$IV', r'$\sharp$iv']

numerals_tonnetz = \
    {

        'I': (0, 0),
        'i': (-1, 0),
        r'$\flat$II': (4, 0),
        r'$\flat$ii': (3, 0),
        'II': (2, -3),
        'ii': (1, -3),
        r'$\flat$III': (-2, 1),
        r'$\flat$iii': (-3, 1),
        'III': (2, 1),
        'iii': (1, 1),
        'IV': (0, -2),
        'iv': (-1, -2),
        r'$\sharp$IV': (-4, 2),
        r'$\sharp$iv': (-5, 2),
        'V': (0, 2),
        'v': (-1, 2),
        r'$\flat$VI': (-2, -1),
        r'$\flat$vi': (-3, -1),
        'VI': (2, -1),
        'vi': (1, -1),
        r'$\flat$VII': (0, -4),
        r'$\flat$vii': (-1, -4),
        'VII': (-4, 0),
        'vii': (-5, 0)

    }
def tonnetz():
    final_dict = {}
    for x, y in numerals_tonnetz.items():
        final_dict[x] = (y[0]*8, y[1]*8)
    return final_dict


scale_degree_converter = \
    {
        0: '1',
        1: 'b2',
        2: '2',
        3: 'b3',
        4: '3',
        5: '4',
        6: '#4',
        7: '5',
        8: 'b6',
        9: '6',
        10: 'b7',
        11: '7'
    }

lower_tuning = \
    {
        '+':'E',
        'A':'G',
        'B':'H',
        'C':'B',
        'D':'O',
        'E':'L',
        'F':'C',
        'G':'M',
        'H':'N',
        'I':'A',
        'K':'none',
        'L':'K',
        'M':'none',
        'N':'none',
        'O':'P',
        'P':'none',
        'Q':'F',
        'R':'I',
        'S':'C',
        'T':'A',
        'V':'+',
        'X':'D',
        'Y':'G',
        'Z':'H',
        '&':'R'
    }

def lower_tuning_fixer(alfabeto_string):
    fixed = []
    for x in alfabeto_string:
        if x in lower_tuning:
            fixed.append(lower_tuning[x])
        else:
            fixed.append(x)
    a = str(fixed)
    b = a.replace("'", '')
    c = b.replace(", ", '')
    d = c.replace("[", '')
    e = d.replace("]", '')
    return e