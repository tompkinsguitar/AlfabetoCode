import random
from collections import defaultdict
from alfabeto_code.AlfabetoConverter import transposed_chords_corpus as alf_chords
from Continuo import ContinuoConverter as CC
from tab_code.TabConverter import transposed_chords_corpus as tab_chords

# from alfabeto_data.all_data import numeral_converter
from alfabeto_sources import *
# import pprint

all_kaps = [kapsperger.v1_continuo, kapsperger.v2_continuo, kapsperger.v3_continuo,
            kapsperger.v5_continuo, kapsperger.v6_continuo, kapsperger.v7_continuo]
all_milanuzzi = [milanuzzi.Milanuzzi_1622a, milanuzzi.Milanuzzi_1625]
all_alf = [kapsperger.v1_continuo, kapsperger.v2_continuo, kapsperger.v3_continuo,
           kapsperger.v5_continuo, kapsperger.v6_continuo, kapsperger.v7_continuo,
           milanuzzi.Milanuzzi_1622a, milanuzzi.Milanuzzi_1625,
           obizzi.libro_primo_continuo, giaccio.Giaccio_1618]

def get_ngrams(data, n):
    for i in range(len(data) - (n - 1)):
        yield data[i:i + n]
    return None


# def get_bigrams(data):
#     for i in range(len(data) - 1):
#         yield data[i:i + 2]
#     return None


def weighted_choice(states):
    """
    Helper function that, when given a dictionary of keys and weights, chooses a random key based on its weight.
    """
    n = random.uniform(0, sum(states.values()))
    for key, val in states.items():
        if n < val:
            return key
        n -= val

    # Something went wrong, don't make a choice.
    return None


def most_used(data, number):
    for a, b in data.items():
        for c, d in b.items():
            if d >= number:
                print(a, c, d)


def markovMaker(source, mode, ngrams, figure_choice):
    markov = defaultdict(lambda: defaultdict(int))
    # source_material = transposed_roots(source)
    continuo_corpus = []
    for x in source:
        # continuo_corpus.append(CC.book_converter(x, mode))
        continuo_corpus.append(CC.book_converter_pc(x, mode))
    # print(continuo_corpus)
    if figure_choice == 'joined':
        for w in continuo_corpus:
            for x in w:
                if ngrams == 2:
                    for (w1, w2) in get_ngrams(x, ngrams):
                        # Update the tally for this combination.
                        print(str(w1), str(w2))
                        markov[str(w1)][str(w2)] += 1
                elif ngrams == 3:
                    for (x1, x2, x3) in get_ngrams(x, ngrams):
                        markov[str(x1), str(x2)][str(x3)] += 1
                elif ngrams == 4:
                    for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                        markov[str(x1), str(x2), str(x3)][str(x4)] += 1
                elif ngrams == 5:
                    for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                        markov[str(x1), str(x2), str(x3), str(x4)][str(x5)] += 1
                elif ngrams == 6:
                    for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                        markov[str(x1), str(x2), str(x3), str(x4), str(x5)][str(x6)] += 1
                elif ngrams == 7:
                    for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                        markov[str(x1), str(x2), str(x3), str(x4), str(x5), str(x6)][str(x7)] += 1
                else:
                    print('not set up for that yet. try 2 or 3')
    elif figure_choice == 'separate':
        for w in continuo_corpus:
            for x in w:
                if ngrams == 1:
                    for w1 in get_ngrams(x, ngrams):
                        markov[str(w1[0])][str(w1[1])] += 1
                elif ngrams == 2:
                    for (w1, w2) in get_ngrams(x, ngrams):
                        # Update the tally for this combination.
                        markov[str(w1[0]), str(w2[0])][str(w1[1]), str(w2[1])] += 1
                elif ngrams == 3:
                    for (x1, x2, x3) in get_ngrams(x, ngrams):
                        markov[str(x1[0]), str(x2[0]), str(x3[0])][str(x1[1]), str(x2[1]), str(x3[1])] += 1
                elif ngrams == 4:
                    for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                        markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0])]\
                            [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1])] += 1
                elif ngrams == 5:
                    for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                        markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0])]\
                            [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1]), str(x5[1])] += 1
                elif ngrams == 6:
                    for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                        markov[str(x1[0]), str(x2[0]), str(x3[0],), str(x4[0]), str(x5[0]), str(x6[0])]\
                            [str(x1[1]), str(x2[1]), str(x3[1],), str(x4[1]), str(x5[1]), str(x6[1])] += 1
                elif ngrams == 7:
                    for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                        markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0]), str(x6[0]), str(x7[0])]\
                            [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1]), str(x5[1]), str(x6[1]), str(x7[1])] += 1
                else:
                    print('not set up for that yet. try 2 or 3')
    elif figure_choice == 'continuo':
        for x in continuo_corpus:
            if ngrams == 2:
                for (w1, w2) in get_ngrams(x, ngrams):
                    # Update the tally for this combination.
                    print(str(w1), str(w2))
                    markov[str(w1[0])][str(w2[0])] += 1
            elif ngrams == 3:
                for (x1, x2, x3) in get_ngrams(x, ngrams):
                    markov[str(x1[0]), str(x2[0])][str(x3[0])] += 1
            elif ngrams == 4:
                for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                    markov[str(x1[0]), str(x2[0]), str(x3[0])][str(x4[0])] += 1
            elif ngrams == 5:
                for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                    markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0])][str(x5[0])] += 1
            elif ngrams == 6:
                for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                    markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0])][str(x6[0])] += 1
            elif ngrams == 7:
                for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                    markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0]), str(x6[0])][str(x7[0])] += 1
            else:
                print('not set up for that yet. try 2 or 3')
    data_dict = {}
    for x in markov:
        temp_dict = {}
        for z, y in markov[x].items():
            temp_dict[z] = y
        data_dict[x] = temp_dict
    # You can use the following code for a preview of the Markov Chain probabilites:
    # for state in markov:
    #     # print('%r => %r' % (state, markov[state]))
    #     print(dict({state: markov[state]}))
    #     pprint.pprint({state: markov[state]})
    return data_dict


def chord_frequency(source, mode):
    chord_dict = {}
    chord_dict_final = {}
    # for x in numerals:
    #     chord_dict[x] = 0
    chord_list = []
    for x in source:
        # chord_list.append(CC.book_converter(x, mode))
        chord_list.append(CC.book_converter_pc(x, mode))
    chord_number = 0
    for y in chord_list:
        chord_number += len(y)
        for z in y:
            if str(z) in chord_dict:
                chord_dict[str(z)] += 1
            else:
                chord_dict[str(z)] = 1
    for x, y in chord_dict.items():
        chord_dict_final[x] = y / chord_number * 100
    return chord_dict_final
