import random
from collections import defaultdict
from alfabeto_code.AlfabetoConverter import transposed_chords_corpus as alf_chords
from alfabeto_code.AlfabetoConverter import transposed_pc_chords_corpus_noMMD as alf_chords_plain
from alfabeto_code.AlfabetoConverter import transposed_pc_roots as alf_roots
from alfabeto_code.AlfabetoConverter import roots_corpus as rc
from tab_code.TabConverter import transposed_chords_corpus as tab_chords
from tab_code.TabConverter import transposed_pc_chords_corpus_noMMD as tab_chords_plain

# from alfabeto_data.all_data import numeral_converter
# from alfabeto_sources import kapsperger
# import pprint


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


def markovMaker(source, mode, ngrams, progression_element, tab):
    markov = defaultdict(lambda: defaultdict(int))
    # source_material = transposed_roots(source)
    alf_corpus = []
    for x in source:
        if tab == 'guitar':
            alf_corpus.append(alf_chords(x, progression_element))
        elif tab == 'theorbo':
            alf_corpus.append(tab_chords(x, progression_element))
    # alf_corpus = corpus_roots(source)
    source_material = []
    # print(alf_corpus)
    if mode == 'major':
        for x in alf_corpus:
            # print(x)
            for y in x:
                if y[0] == 'I':
                    source_material.append(y)
    elif mode == 'minor':
        for x in alf_corpus:
            for y in x:
                if y[0] == 'i':
                    source_material.append(y)
    elif mode == 'other':
        for x in alf_corpus:
            for y in x:
                if y[0] != 'i' and y[0] != 'I':
                    source_material.append(y)
    elif mode == 'all':
        for x in alf_corpus:
            for y in x:
                source_material.append(y)
    for x in source_material:
        # print(x)
        if ngrams == 2:
            for (w1, w2) in get_ngrams(x, ngrams):
                # Update the tally for this combination.
                markov[w1][w2] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(x, ngrams):
                markov[(x1, x2)][x3] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3)][x4] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4)][x5] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5)][x6] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5, x6)][x7] += 1
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

# def markovMakerContinuo(source, mode, ngrams):
#     """Source: continuo stream (Alfabeto Chords Data)"""
#     markov = defaultdict(lambda: defaultdict(int))
#     # source_material = transposed_roots(source)
#     alf_corpus = []
#     # for book in source:
#     #     for
#     for x in source:
#         if tab == 'guitar':
#             alf_corpus.append(alf_chords(x, 'all'))
#         elif tab == 'theorbo':
#             alf_corpus.append(tab_chords(x, 'all'))
#     # alf_corpus = corpus_roots(source)
#     source_material = []
#     # print(alf_corpus)
#     if mode == 'major':
#         for x in alf_corpus:
#             # print(x)
#             for y in x:
#                 if y[0] == 'I':
#                     source_material.append(y)
#     elif mode == 'minor':
#         for x in alf_corpus:
#             for y in x:
#                 if y[0] == 'i':
#                     source_material.append(y)
#     elif mode == 'other':
#         for x in alf_corpus:
#             for y in x:
#                 if y[0] != 'i' and y[0] != 'I':
#                     source_material.append(y)
#     elif mode == 'all':
#         for x in alf_corpus:
#             for y in x:
#                 source_material.append(y)
#     for x in source_material:
#         # print(x)
#         if ngrams == 2:
#             for (w1, w2) in get_ngrams(x, ngrams):
#                 # Update the tally for this combination.
#                 markov[w1][w2] += 1
#         elif ngrams == 3:
#             for (x1, x2, x3) in get_ngrams(x, ngrams):
#                 markov[(x1, x2)][x3] += 1
#         elif ngrams == 4:
#             for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
#                 markov[(x1, x2, x3)][x4] += 1
#         elif ngrams == 5:
#             for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
#                 markov[(x1, x2, x3, x4)][x5] += 1
#         elif ngrams == 6:
#             for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
#                 markov[(x1, x2, x3, x4, x5)][x6] += 1
#         elif ngrams == 7:
#             for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
#                 markov[(x1, x2, x3, x4, x5, x6)][x7] += 1
#         else:
#             print('not set up for that yet. try 2 or 3')
#     data_dict = {}
#     for x in markov:
#         temp_dict = {}
#         for z, y in markov[x].items():
#             temp_dict[z] = y
#         data_dict[x] = temp_dict
#     # You can use the following code for a preview of the Markov Chain probabilites:
#     # for state in markov:
#     #     # print('%r => %r' % (state, markov[state]))
#     #     print(dict({state: markov[state]}))
#     #     pprint.pprint({state: markov[state]})
#     return data_dict

def markovComposer(source, mode, ngrams, progression_element, tab):
    markov = defaultdict(lambda: defaultdict(int))
    # source_material = transposed_roots(source)
    alf_corpus = []
    for x in source:
        if tab == 'guitar':
            alf_corpus.append(alf_chords_plain(x, progression_element))
        if tab == 'theorbo':
            alf_corpus.append(tab_chords_plain(x, progression_element))
    # alf_corpus = corpus_roots(source)
    source_material = []
    if mode == 'major':
        for x in alf_corpus:
            for y in x:
                if y[0] == 'I':
                    source_material.append(y)
    elif mode == 'minor':
        for x in alf_corpus:
            for y in x:
                if y[0] == 'i':
                    source_material.append(y)
    elif mode == 'other':
        for x in alf_corpus:
            for y in x:
                if y[0] != 'i' and y[0] != 'I':
                    source_material.append(y)
    else:
        for x in alf_corpus:
            for y in x:
                source_material.append(y)
    for x in source_material:

        if ngrams == 2:
            for (w1, w2) in get_ngrams(x, ngrams):
                # Update the tally for this combination.
                markov[w1][w2] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(x, ngrams):
                markov[(x1, x2)][x3] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3)][x4] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4)][x5] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5)][x6] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5, x6)][x7] += 1
        else:
            print('not set up for that yet. try 2 or 3')
    return markov


def markovMaker_root(source, ngrams, progression_element, tab):
    markov = defaultdict(lambda: defaultdict(int))
    # source_material = transposed_roots(source)
    alf_corpus = []
    for x in source:
        if tab == 'guitar':
            alf_corpus.append(rc(x, progression_element))
        if tab == 'theorbo':
            alf_corpus.append(tab_chords(x, progression_element))
    # alf_corpus = corpus_roots(source)
    source_material = []
    for x in alf_corpus:
        for y in x:
            source_material.append(y)
    for x in source_material:
        # print(x)
        if ngrams == 2:
            for (w1, w2) in get_ngrams(x, ngrams):
                # Update the tally for this combination.
                markov[w1][w2] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(x, ngrams):
                markov[(x1, x2)][x3] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3)][x4] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4)][x5] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5)][x6] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(x, ngrams):
                markov[(x1, x2, x3, x4, x5, x6)][x7] += 1
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

