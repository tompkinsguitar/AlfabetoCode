from alfabeto_code import chronology as ch
from alfabeto_sources import *
from alfabeto_code.AlfabetoConverter import transposed_chords_corpus as alf_chords
from alfabeto_code.AlfabetoConverter import transposed_pc_chords as alf_chords_per_song
import csv
from tab_code.TabConverter import transposed_chords_corpus as tab_chords
from alfabeto_data.all_data import numerals
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr
from scipy.spatial.distance import euclidean, cosine
import string
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import *


# all_corpus = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
#               obizzi.libro_primo, stefani.stefani, sanz.sanz_1674, abbatessa.varii]
# all_alfabeto = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
#                 obizzi.libro_primo, stefani.stefani, sanz.sanz_1674, abbatessa.varii]
all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7]
#
# all_kaps_p = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
#               palestrina_chords_22]
# all_kaps_pb = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
#                palestrina_chords_22, beethoven_10]
# def chord_freq_bach(number):

def chord_frequency(source, mode_list, progression_element, tab):
    chord_dict = {}
    chord_dict_final = {}
    for x in numerals:
        chord_dict[x] = 0
    chord_list = []
    if tab == 'guitar':
        for x in source:
            book_list = []
            for song in x.values():
                if (song['data']['key'], song['data']['final']) in mode_list:
                    book_list.append(alf_chords_per_song(song['alfabeto'], progression_element))
            chord_list.append(book_list)
    elif tab == 'bach':
        for x in source:
            chord_list.append(x)
        # chord_list = source
        # elif tab == 'theorbo':
        #     chord_list.append(tab_chords(x, progression_element))
        # elif tab == 'bach':
        #     chord_list.append(source)
    chord_number = 0
    for x in chord_list:
        for y in x:
            chord_number += len(y)
            for z in y:
                if z in chord_dict:
                    chord_dict[z] += 1
    # elif mode == 'minor':
    #     for x in chord_list:
    #         for y in x:
    #             if y[0] == 'i' or y[1] == 'i':
    #                 chord_number += len(y)
    #                 for z in y:
    #                     chord_dict[z] += 1
    # elif mode == 'other':
    #     for x in chord_list:
    #         for y in x:
    #             if y[0] != 'i' and y[1] != 'i' and y[0] != 'I' and y[1] != 'I':
    #                 chord_number += len(y)
    #                 for z in y:
    #                     chord_dict[z] += 1
    # elif mode == 'all':
    #     for x in chord_list:
    #         for y in x:
    #             chord_number += len(y)
    #             for z in y:
    #                 chord_dict[z] += 1
    for x, y in chord_dict.items():
        chord_dict_final[x] = y / chord_number * 100
    return chord_dict_final


def chord_frequency_per_song(song, mode, progression_element, tab):
    chord_dict = {}
    chord_dict_final = {}
    for x in numerals:
        chord_dict[x] = 0
    chord_list = []
    if tab == 'guitar':
        chord_list.append(alf_chords_per_song(song, progression_element))
    elif tab == 'theorbo':
        chord_list.append(tab_chords(song, progression_element))
    elif tab == 'bach':
        chord_list.append(song)
    chord_number = 0
    # print(chord_list)
    if mode == 'major':
        for y in chord_list:
            if y[0] == 'I' or y[1] == 'I':
                chord_number += len(y)
                for z in y:
                    chord_dict[z] += 1
    elif mode == 'minor':
        for y in chord_list:
            if y[0] == 'i' or y[1] == 'i':
                chord_number += len(y)
                for z in y:
                    chord_dict[z] += 1
    elif mode == 'other':
        for y in chord_list:
            if y[0] != 'i' and y[1] != 'i' and y[0] != 'I' and y[1] != 'I':
                chord_number += len(y)
                for z in y:
                    chord_dict[z] += 1
    else:
        for y in chord_list:
            chord_number += len(y)
            for z in y:
                chord_dict[z] += 1
    for x, y in chord_dict.items():
        if y > 0:
            chord_dict_final[x] = y / chord_number * 100
    # print(chord_dict)
    return chord_dict_final


def book_data(book, mode, progression_element, tab):
    all_song_data = []
    for song in book.values():
        song_data = []
        freq = chord_frequency_per_song(song, mode, progression_element, tab)
        # for numeral in numerals:
        for numeral in numerals:
            if numeral in freq:
                song_data.append(freq[numeral])
            else:
                song_data.append(0)
        all_song_data.append(song_data)
        # print(song_data)
    return all_song_data


def kaps_scatter_plot(mode):
    k1_data = []
    k2_data = []
    k3_data = []
    k4_data = []
    k5_data = []
    k6_data = []
    k7_data = []
    sanz_data = []
    mean_data = []
    # bach_data = []
    #
    X = [i for i in range(len(numerals))]
    #
    for numeral in numerals:
        k1_data.append(chord_frequency([all_kaps[0]], mode, 'all', 'guitar')[numeral])
        k2_data.append(chord_frequency([all_kaps[1]], mode, 'all', 'guitar')[numeral])
        k3_data.append(chord_frequency([all_kaps[2]], mode, 'all', 'guitar')[numeral])
        k4_data.append(chord_frequency([all_kaps[3]], mode, 'all', 'guitar')[numeral])
        k5_data.append(chord_frequency([all_kaps[4]], mode, 'all', 'guitar')[numeral])
        k6_data.append(chord_frequency([all_kaps[5]], mode, 'all', 'guitar')[numeral])
        k7_data.append(chord_frequency([all_kaps[6]], mode, 'all', 'guitar')[numeral])
        # bach_data.append(chord_frequency(JSB, 'major', 'all', 'bach')[numeral])
        # sanz_data.append(chord_frequency([sanz.sanz_1674], 'major', 'all', 'guitar')[numeral])
    #
    #
    # #
    for a, b, c, d, e, f, g in zip(k1_data, k2_data, k3_data, k4_data, k5_data, k6_data, k7_data):
        mean_data.append(np.mean([a, b, c, d, e, f, g]))
    #
    # plt.plot(k1_data, 'b-', linewidth=4.0, alpha=.6)
    # plt.plot(k2_data, 'r-', linewidth=4.0, alpha=.6)
    # plt.plot(k3_data, 'y-', linewidth=4.0, alpha=.6)
    # plt.plot(k4_data, 'k-', linewidth=4.0, alpha=.6)
    # plt.plot(sanz_data, 'b--', linewidth=2.0, label='Sanz (1674)')
    # # plt.plot(bach_data, 'b--', linewidth=2.0, label='Bach Chorales')
    plt.plot(mean_data, 'black', linewidth=8.0, alpha=.3, label='Mean(Average)')
    #
    plt.scatter(X, k1_data, marker='$1$', s=350, c='blue', alpha=.6, label='Book 1 (1610)')
    plt.scatter(X, k2_data, marker='$2$', s=350, c='green', alpha=.6, label='Book 2 (1619)')
    plt.scatter(X, k3_data, marker='$3$', s=350, c='blue', alpha=.6, label='Book 3 (1619)')
    plt.scatter(X, k4_data, marker='$4$', s=350, c='green', alpha=.6, label='Book 4 (1623)')
    plt.scatter(X, k5_data, marker='$5$', s=350, c='blue', alpha=.6, label='Book 5 (1630)')
    plt.scatter(X, k6_data, marker='$6$', s=350, c='green', alpha=.6, label='Book 6 (1632)')
    plt.scatter(X, k7_data, marker='$7$', s=350, c='blue', alpha=.6, label='Book 7 (1640)')

    # plt.scatter(X, k1_data, marker='o', s=350, c='blue', alpha=.6, label='Book 1 (1610)')
    # plt.scatter(X, k2_data, marker='o', s=350, c='green', alpha=.6, label='Book 2 (1619)')
    # plt.scatter(X, k3_data, marker='^', s=350, c='blue', alpha=.6, label='Book 3 (1619)')
    # plt.scatter(X, k4_data, marker='^', s=350, c='green', alpha=.6, label='Book 4 (1623)')
    # plt.scatter(X, k5_data, marker='p', s=350, c='blue', alpha=.6, label='Book 5 (1630)')
    # plt.scatter(X, k6_data, marker='p', s=350, c='green', alpha=.6, label='Book 6 (1632)')
    # plt.scatter(X, k7_data, marker='s', s=350, c='blue', alpha=.6, label='Book 7 (1640)')
    # plt.scatter(X, sanz_data, marker='p', s=350, c='cyan', alpha=.6)
    # # plt.scatter(sanz_data, 'b--', linewidth=2.0, label='Sanz (1674)')
    # # plt.scatter(bach_data, 'b--', linewidth=2.0, label='Bach Chorales')
    # # plt.scatter(mean_data, 'black', linewidth=8.0, alpha=.1, label='Mean(Average)')
    #
    # k1 = book_data(all_kaps[0], 'major', 'all', 'guitar')
    # k2 = book_data(all_kaps[1], 'major', 'all', 'guitar')
    # k3 = book_data(all_kaps[2], 'major', 'all', 'guitar')
    # k4 = book_data(all_kaps[3], 'major', 'all', 'guitar')
    # k5 = book_data(all_kaps[4], 'major', 'all', 'guitar')
    # k6 = book_data(all_kaps[5], 'major', 'all', 'guitar')
    # k7 = book_data(all_kaps[6], 'major', 'all', 'guitar')
    # # sanz = book_data(sanz.sanz_1674, 'major', 'all', 'guitar')
    #
    # for x in k1:
    #     plt.scatter(X, x, marker='$k1$', c='yellow', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k2:
    #     plt.scatter(X, x, marker='$k2$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k3:
    #     plt.scatter(X, x, marker='$k3$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k4:
    #     plt.scatter(X, x, marker='$k4$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k4:
    #     plt.scatter(X, x, marker='$k5$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k4:
    #     plt.scatter(X, x, marker='$k6$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in k4:
    #     plt.scatter(X, x, marker='$k7$', c='blue', alpha=.4)
    #     plt.plot(x, 'b--', linewidth=0.5, alpha=.1)
    # for x in sanz:
    #     plt.scatter(X, x, marker='p', c='cyan', alpha=.4)
    #     plt.plot(x, 'c--', linewidth=0.5, alpha=.2)
    plt.xlabel('Chord', size=20)
    plt.ylabel('Frequency (Percent)', size=20)
    plt.title('Chord Frequency', size=30)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    plt.xticks(X, numerals, size=20)
    plt.yticks(size=20)
    plt.subplots_adjust(bottom=0.2)
    plt.show()


def mds_graph_chordFQ(comparison_list, mode, progression_element, tab):
    # k1, k2, k3, k4, sanz1
    source_percentages = []
    # for x in comparison_list:
    #     source_list.append(chord_frequency([x], mode, progression_element, tab))
    for x in comparison_list:
        temp_list = []
        for numeral in numerals:
            if type(x) == list:
                # print('this is bach')
                temp_list.append(chord_frequency(x, mode, 'all', 'bach')[numeral])
            else:
                # print('not bach')
                temp_list.append(chord_frequency([x], mode, progression_element, tab)[numeral])
        source_percentages.append(temp_list)
    print(source_percentages)
    source_percentages = np.array(source_percentages)
    from scipy.spatial.distance import cdist
    source_distances = cdist(source_percentages, source_percentages, metric='euclidean')
    # for x in source_percentages:
    #     distance_list = []
    #     for y in source_percentages:
    #         distances = euclidean(x, y)
    #         # distances = cosine(x, y)*1000
    #         # distances = 100 - pearsonr(x, y)[0] * 100
    #         distance_list.append(distances)
    #     source_distances.append(distance_list)
    print(source_distances)
    A = source_distances
    print('A', A)
    return A


def mds_graph_ngram(comparison_list, ngram, mode, number, progression_element, tab):
    top_list = []
    source_percentages = []
    ordered_percentages = []
    source_distances = []
    top_stats = ch.list_maker(ch.stats(all_kaps, mode, ngram, number, progression_element, tab), ngram)
    for x in top_stats:
        top_list.append(x[0])
    for x in comparison_list:
        source_percentages.append(ch.list_maker(ch.stats([x], mode, ngram, None, progression_element, tab), ngram))

    def data_appender(corpus, data):
        for x in top_stats:
            z = 0
            for y in corpus:
                if x[0] == y[0]:
                    z += 1
                    data.append(y[1])
            if z == 0:
                data.append(0)
    print(source_percentages)
    for x in source_percentages:
        temp_list = []
        data_appender(x, temp_list)
        ordered_percentages.append(temp_list)
    print(ordered_percentages)
    for x in ordered_percentages:
        distance_list = []
        for y in ordered_percentages:
            distances = euclidean(x, y)
            # distances = 100 - pearsonr(x, y)[0] * 100
            distance_list.append(distances)
        source_distances.append(distance_list)
    print(np.array(source_distances))
    A = np.array(source_distances)
    # print('A', A)
    return A

# path = '/home/daniel/Desktop/Updated Kaps Images/kapsFQ.png'
# function = mds_graph_ngram(all_kaps, 3, 'major', None, 'all', 'guitar')
# names = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']
def csv_writer(corpus_names, mds_function, file_name):
    corpus_data = []
    rows = ['']
    for x in corpus_names:
        rows.append(x)

    corpus_data.append(rows)
    for a, b in zip(mds_function, corpus_names):
        temp_list = []
        temp_list.append(b)
        for x in a:
            temp_list.append(x)
        corpus_data.append(temp_list)

    with open(file_name, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        final_data = corpus_data
        a.writerows(final_data)


def neato_graph(corpus_list, mode, ngram, number, path):
    dt = [('len', float)]
    x = []

    A = (mds_graph_chordFQ(corpus_list, mode, 'all', 'guitar')/1).view(dt)
    # A = (mds_graph_ngram(corpus_list, ngram, mode, number, 'all', 'guitar')/1).view(dt)

    G = nx.from_numpy_matrix(A)
    # G = nx.relabel_nodes(G, {0:'k1', 1:'k2', 2:'k3', 3:'k4', 4:'k5',5: 'k6', 6: 'k7',
    #                          7:'obizzi', 8:'stefani', 9:'sanz', 10: 'abbatessa',
    #                          11: 'palestrina', 12: 'monteverdi', 13: 'bach',
    #                          14: 'haydn', 15: 'mozart', 16: 'beethoven'})
    G = nx.relabel_nodes(G, {0:'1', 1:'2', 2:'3', 3:'4', 4:'5',5: '6', 6: '7',
                             7: 'Palestrina', 8: 'Beethoven'})
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos)

    G = to_agraph(G)

    G.node_attr.update(color="green", style="filled", fontsize=30)
    G.edge_attr.update(color="black", width="2.0")
    # G.graph_attr.update(landscape='true', ranksep='0.1')

    G.draw(path, format='png', prog='neato')


def similarity_similarity(function1, function2):
    final_list = []
    for x, y in zip(function1, function2):
        temp_list = []
        for a, b in zip(x, y):
            temp_list.append(b-a)
        final_list.append(temp_list)
    return final_list
