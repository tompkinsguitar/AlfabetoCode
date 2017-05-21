from alfabeto_sources import *
from alfabeto_code.AlfabetoConverter import AlfabetoSymbols
from Continuo.ContinuoMarkov import all_alf
from Continuo.ContinuoConverter import book_converter_pc

all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7]
all_books = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
             obizzi.libro_primo, stefani.stefani, sanz.sanz_1674, abbatessa.varii]


def chord_counter(book_list, mode):
    counter = 0
    finals = []
    for x in book_list:
        finals.append(book_converter_pc(x, mode))
    for x in finals:
        for y in x:
            for z in y:
                counter += 1

    print(counter)


# for x in all_alf[0:1]:
#     for b in x.values():
#         for a in b:
#             if a in AlfabetoSymbols:
#                 counter += 1
# print(counter)

def key_frequency(book_list):
    '''what keys are used and how many'''
    total_songs = 0
    modes = {}
    for x in book_list:
        for y in x.values():
            total_songs += 1
            if 'data' in y:
                a = str(y['data']['key'])
                b = str(y['data']['final'])
                c = (a,b)
                if c not in modes.keys():
                    modes[c] = 1
                else:
                    modes[c] += 1
    print('total songs: ', total_songs)
    print(modes)
# finals = []
# for x in all_alf:
#     finals.append(book_converter_pc(x, 'all'))
# for x in finals:
#     for y in x:
#         for z in y:
#             counter+= 1
#
# print(counter)