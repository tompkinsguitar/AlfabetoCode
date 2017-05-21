scale_degree_converter_major = \
    {
        0: '1',
        1: '#1',
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

scale_degree_converter_minor = \
    {
        0: '1',
        1: '#1',
        2: '2',
        3: '3',
        4: '#3',
        5: '4',
        6: '#4',
        7: '5',
        8: '6',
        9: '#6',
        10: '7',
        11: '#7'
    }

ordering = ['1', '#1', 'b2', '2', '#2', 'b3', '3', '#3', 'b4', '4', '#4', 'b5', '5', '#5', 'b6', '6', '#6', 'b7', '7', '#7', '8']

diatonic_major = [0, 2, 4, 5, 7, 9, 11]
sharp_major = [1, 6]
flat_major = [3, 8, 10]

diatonic_minor = [0, 2, 3, 5, 7, 8, 10]
sharp_minor = [1, 4, 6, 9, 11]


pc_scale_degrees = \
    {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        't': 10,
        'e': 11
    }

figures_natural = \
    {
        0: '8',
        12: '8',
        1: 'b2',
        2: '2',
        3: '3',
        4: '3',
        5: '4',
        6: '#4',
        7: '5',
        8: '6',
        9: '6',
        10: '7',
        11: '7'
    }

figures_sharp = \
    {
        1: '#1',
        3: '#2',
        4: '#3',
        5: '#3',
        6: '#4',
        7: '#5',
        8: '#5',
        9: '#6',
        10: '#6',
        11: '#7',
        12: '8'
    }

figures_flat = \
    {
        1: 'b2',
        2: 'b3',
        3: 'b3',
        5: 'b5',
        6: 'b5',
        7: 'b5',
        8: 'b6',
        10: 'b7',
        11: 'b8',
        12: '8'
    }

triad_inversions_pc = [[0, 3, 7], [0, 4, 7],
                       [0, 3, 8], [0, 4, 9],
                       [0, 5, 8], [0, 5, 9]],

wrong_figures = [['#2', '#5', '8'], ['b4', '5', '8'], ['b5', '6', '8']]
right_figures = [['b3', 'b6', '8'], ['#3', '5', '8'], ['#4', '6', '8']]