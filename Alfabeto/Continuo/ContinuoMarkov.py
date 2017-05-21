import random
from collections import defaultdict
from alfabeto_code.AlfabetoConverter import transposed_chords_corpus as alf_chords
from Continuo import ContinuoConverter as CC
from tab_code.TabConverter import transposed_chords_corpus as tab_chords
from alfabeto_sources.all_sources import *


def get_ngrams(data, n):
    for i in range(len(data) - (n - 1)):
        yield data[i:i + n]
    return None


def scale_degree_harmonization(data, mode):
    data_list = {}
    data_list_final = {}
    total_sums = 0
    for x in data:
        a = CC.book_converter_pc(x, mode)
        for b in a:
            for z in b:
                total_sums += 1
                if str(z) not in data_list:
                    data_list[str(z)] = 1
                else:
                    data_list[str(z)] += 1
    # print('number of chords', total_sums)
    for x, y in data_list.items():
        data_list_final[x] = (y / total_sums)*100
    # print(data_list_final)
    return data_list_final

def scale_degree_harmonization_untransposed(data, mode_list):
    data_list = {}
    data_list_final = {}
    total_sums = 0
    for x in data:
        a = CC.book_converter_pc_untransposed(x, mode_list)
        for b in a:
            for z in b:
                total_sums += 1
                if str(z) not in data_list:
                    data_list[str(z)] = 1
                else:
                    data_list[str(z)] += 1
    # print('number of chords', total_sums)
    for x, y in data_list.items():
        data_list_final[x] = (y / total_sums)*100
    # print(data_list_final)
    return data_list_final

def scale_degree_harmonization_song(song, mode):
    data_list = {}
    data_list_final = {}
    total_sums = 0
    a = CC.figure_intervals_pc(song, mode)
    for z in a:
        total_sums += 1
        if str(z) not in data_list:
            data_list[str(z)] = 1
        else:
            data_list[str(z)] += 1
    print('number of chords', total_sums)
    for x, y in data_list.items():
        data_list_final[x] = (y / total_sums)*100
    # print(data_list_final)
    return data_list_final


def scale_degree_harmonization_song_untransposed(song, mode):
    data_list = {}
    data_list_final = {}
    total_sums = 0
    a = CC.figure_intervals_pc_untransposed(song, mode)
    for z in a:
        total_sums += 1
        if str(z) not in data_list:
            data_list[str(z)] = 1
        else:
            data_list[str(z)] += 1
    # print('number of chords', total_sums)
    for x, y in data_list.items():
        data_list_final[x] = (y / total_sums)*100
    # print(data_list_final)
    return data_list_final


def octave_harmonization(data, mode):
    final_octave = {}
    final_octave_final = {}
    data_dict = scale_degree_harmonization(data, mode)
    for x, y in data_dict.items():
        percents = []
        if x[1:4] not in final_octave:
            final_octave[x[1:4]] = 0
        for a, b in data_dict.items():
            if a[1:4] == x[1:4]:
                percents.append(b)
        # print(percents)
        if data_dict[x] == max(percents):
            final_octave_final[x] = max(percents)
    return final_octave_final


def key_frequency(corpus_list):
    key_list = {}
    for book in corpus_list:
        for song in book.keys():
            a = (book[song]['data']['key'], book[song]['data']['final'])
            print(a)
            if a not in key_list:
                key_list[a] = 1
            else:
                key_list[a] += 1
    return key_list


def note_frequency(corpus_list, mode):
    final_list = []
    final_data = {}
    for x in corpus_list:
        l = CC.book_converter_pc(x, mode)
        for y in l:
            for z in y:
                final_list.append(z[0])
                for a in z[1]:
                    final_list.append((a+z[0]) % 12)
    print('number of notes: ', len(final_list))
    for x in range(12):
        final_data[x] = 0
    for x in final_list:
        final_data[x] += 1 / len(final_list) * 100
    return final_data


def note_frequency_song(song):
    final_list = []
    final_data = {}
    l = CC.figure_intervals_pc(song, 'all')
    for x in l:
        final_list.append(x[0])
        for y in x[1]:
            final_list.append((y+x[0])%12)
    for x in range(12):
        final_data[x] = 0
    for x in final_list:
        # final_data[x] += 1
        final_data[x] += 1 / len(final_list) * 100
    return final_data



def scale_degree_frequency(corpus_list, mode):
    final_frequency = {}
    data_dict = scale_degree_harmonization(corpus_list, mode)
    choices = list(range(12))
    for x in choices:
        final_frequency[x] = 0
    for x, y in data_dict.items():
        if x[2] == ',':
            final_frequency[int(x[1])] += y
        else:
            final_frequency[int(x[1:3])] += y
    return final_frequency



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
                        # print(str(w1), str(w2))
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
                    # print(str(w1), str(w2))
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


def markovMaker_song(song, mode, ngrams, figure_choice):
    markov = defaultdict(lambda: defaultdict(int))
    # source_material = transposed_roots(source)
    continuo_corpus = CC.figure_intervals_pc(song, mode)
    if figure_choice == 'joined':
        if ngrams == 2:
            for (w1, w2) in get_ngrams(continuo_corpus, ngrams):
                # Update the tally for this combination.
                # print(str(w1), str(w2))
                markov[str(w1)][str(w2)] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1), str(x2)][str(x3)] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1), str(x2), str(x3)][str(x4)] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1), str(x2), str(x3), str(x4)][str(x5)] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1), str(x2), str(x3), str(x4), str(x5)][str(x6)] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1), str(x2), str(x3), str(x4), str(x5), str(x6)][str(x7)] += 1
        else:
            print('not set up for that yet. try 2 or 3')
    elif figure_choice == 'separate':
        if ngrams == 1:
            for w1 in get_ngrams(continuo_corpus, ngrams):
                markov[str(w1[0])][str(w1[1])] += 1
        elif ngrams == 2:
            for (w1, w2) in get_ngrams(continuo_corpus, ngrams):
                # Update the tally for this combination.
                markov[str(w1[0]), str(w2[0])][str(w1[1]), str(w2[1])] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0])][str(x1[1]), str(x2[1]), str(x3[1])] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0])]\
                    [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1])] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0])]\
                    [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1]), str(x5[1])] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0],), str(x4[0]), str(x5[0]), str(x6[0])]\
                    [str(x1[1]), str(x2[1]), str(x3[1],), str(x4[1]), str(x5[1]), str(x6[1])] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0]), str(x6[0]), str(x7[0])]\
                    [str(x1[1]), str(x2[1]), str(x3[1]), str(x4[1]), str(x5[1]), str(x6[1]), str(x7[1])] += 1
        else:
            print('not set up for that yet. try 2 or 3')
    elif figure_choice == 'continuo':
        if ngrams == 2:
            for (w1, w2) in get_ngrams(continuo_corpus, ngrams):
                # Update the tally for this combination.
                # print(str(w1), str(w2))
                markov[str(w1[0])][str(w2[0])] += 1
        elif ngrams == 3:
            for (x1, x2, x3) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0])][str(x3[0])] += 1
        elif ngrams == 4:
            for (x1, x2, x3, x4) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0])][str(x4[0])] += 1
        elif ngrams == 5:
            for (x1, x2, x3, x4, x5) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0])][str(x5[0])] += 1
        elif ngrams == 6:
            for (x1, x2, x3, x4, x5, x6) in get_ngrams(continuo_corpus, ngrams):
                markov[str(x1[0]), str(x2[0]), str(x3[0]), str(x4[0]), str(x5[0])][str(x6[0])] += 1
        elif ngrams == 7:
            for (x1, x2, x3, x4, x5, x6, x7) in get_ngrams(continuo_corpus, ngrams):
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


def ordered_markov(markov_function, last_pc):
    number_counter = 0
    percent_dict = {}
    for w, x in markov_function.items():
        if int(w[-1]) == last_pc or last_pc == 'all':
            for y in x.values():
                number_counter += y
    for a, b in markov_function.items():
        if int(a[-1]) == last_pc or last_pc == 'all':
            for c, d in b.items():
                percent_dict[(a+c)] = d/number_counter*100
    return percent_dict


def markov_cluster_data(continuo_source, ngrams, last_pc):
    all_ngrams = []
    key_data = []
    all_songs_ngram = []
    for book in continuo_source:
        for song in book.values():
            song_markov = ordered_markov(markovMaker_song(song, 'all', ngrams, 'separate',), last_pc)
            for x in song_markov.keys():
                if x not in all_ngrams:
                    all_ngrams.append(x)
    for book in continuo_source:
        for song in book.values():
            temp_ngram_list = []
            key_data.append((song['data']['key'], song['data']['final']))
            song_markov = ordered_markov(markovMaker_song(song, 'all', ngrams, 'separate', ), last_pc)
            for x in all_ngrams:
                if x in song_markov:
                    temp_ngram_list.append(song_markov[x])
                else:
                    temp_ngram_list.append(0)
            all_songs_ngram.append(temp_ngram_list)
    return all_songs_ngram, key_data


def chord_frequency(source, mode, key, final):
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


# k1 = octave_harmonization([all_kaps[0]], ('n', 5))
# k2 = octave_harmonization([all_kaps[1]], ('n', 5))
# k3 = octave_harmonization([all_kaps[2]], ('n', 5))
# k4 = octave_harmonization([all_kaps[3]], ('n', 5))
# k5 = octave_harmonization([all_kaps[4]], ('n', 5))
# k6 = octave_harmonization([all_kaps[5]], ('n', 5))
# k7 = octave_harmonization([all_kaps[6]], ('n', 5))