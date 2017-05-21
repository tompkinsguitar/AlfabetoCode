from alfabeto_code import chronology as ch
from alfabeto_sources import *
from alfabeto_code.AlfabetoConverter import transposed_chords_corpus as alf_chords
from tab_code.TabConverter import transposed_chords_corpus as tab_chords
from alfabeto_data.all_data import numerals
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr
import string
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import bach_all_chorales as CHO
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import palestrina_chords_22 as pal
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import monteverdi as mon
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import haydn
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import mozart
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import beethoven_10 as beet
from scipy.spatial.distance import euclidean

all_corpus = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4,
              obizzi.libro_primo, stefani.stefani, abbatessa.varii, sanz.sanz_1674,
              CHO, pal, mon, haydn, mozart, beet]
all_alfabeto = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4,
                obizzi.libro_primo, stefani.stefani, abbatessa.varii, sanz.sanz_1674]
all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4]
obi = [obizzi.libro_primo]
ste = [stefani.stefani]
kap1 = [kapsperger.v1]
kap2 = [kapsperger.v2]
kap3 = [kapsperger.v3]
kap4 = [kapsperger.v4]
sanz = [sanz.sanz_1674]


# def chord_freq_bach(number):


def chord_frequency(source, mode, progression_element, tab):
    chord_dict = {}
    chord_dict_final = {}
    for x in numerals:
        chord_dict[x] = 0
    chord_list = []
    for x in source:
        if tab == 'guitar':
            chord_list.append(alf_chords(x, progression_element))
        elif tab == 'theorbo':
            chord_list.append(tab_chords(x, progression_element))
        elif tab == 'bach':
            chord_list.append(source)
    chord_number = 0
    # print(chord_list)
    if mode == 'major':
        for x in chord_list:
            for y in x:
                if y[0] == 'I' or y[1] == 'I':
                    chord_number += len(y)
                    for z in y:
                        chord_dict[z] += 1
    elif mode == 'minor':
        for x in chord_list:
            for y in x:
                if y[0] == 'i' or y[1] == 'i':
                    chord_number += len(y)
                    for z in y:
                        chord_dict[z] += 1
    elif mode == 'other':
        for x in chord_list:
            for y in x:
                if y[0] != 'i' or y[1] != 'i' or y[0] != 'I' or y[1] != 'I':
                    chord_number += len(y)
                    for z in y:
                        chord_dict[z] += 1
    else:
        for x in chord_list:
            for y in x:
                chord_number += len(y)
                for z in y:
                    chord_dict[z] += 1
    for x, y in chord_dict.items():
        chord_dict_final[x] = y / chord_number * 100
    return chord_dict_final

#
# k1_data = []
# k2_data = []
# k3_data = []
# k4_data = []
# sanz_data = []
# mean_data = []
# bach_data = []
#
# X = [i for i in range(len(numerals))]
#
# for numeral in numerals:
#     k1_data.append(chord_frequency(kap1, 'major', 'all', 'guitar')[numeral])
#     k2_data.append(chord_frequency(kap2, 'major', 'all', 'guitar')[numeral])
#     k3_data.append(chord_frequency(kap3, 'major', 'all', 'guitar')[numeral])
#     k4_data.append(chord_frequency(kap4, 'major', 'all', 'guitar')[numeral])
#     bach_data.append(chord_frequency(JSB, 'major', 'all', 'bach')[numeral])
#     sanz_data.append(chord_frequency(sanz, 'major', 'all', 'guitar')[numeral])

"""

for w, x, y, z in zip(k1_data, k2_data, k3_data, k4_data):
    mean_data.append(np.mean([w, x, y, z]))

plt.plot(k1_data, 'g', linewidth=2.0, label='Book 1 (1610)')
plt.plot(k2_data, 'b', linewidth=2.0, label='Book 2 (1619)')
plt.plot(k3_data, 'r--', linewidth=2.0, label='Book 3 (1619)')
plt.plot(k4_data, 'y', linewidth=2.0, label='Book 4 (1623)')
# plt.plot(sanz_data, 'b--', linewidth=2.0, label='Sanz (1674)')
# plt.plot(bach_data, 'b--', linewidth=2.0, label='Bach Chorales')
# plt.plot(mean_data, 'black', linewidth=8.0, alpha=.1, label='Mean(Average)')
plt.xlabel('Chord')
plt.ylabel('Frequency (Percent)')
plt.title('Chord Frequency')
legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
legend.get_frame().set_facecolor('#00FFCC')
plt.xticks(X, numerals, size=16)
plt.show()

"""


def mds_graph_chordFQ(comparison_list, mode, progression_element, tab):
    # k1, k2, k3, k4, sanz1
    source_distances = []
    source_percentages = []
    # for x in comparison_list:
    #     source_list.append(chord_frequency([x], mode, progression_element, tab))
    for x in comparison_list:
        temp_list = []
        for numeral in numerals:
            if type(x) == list:
                print('this is bach')
                temp_list.append(chord_frequency(x, mode, 'all', 'bach')[numeral])
            else:
                print('not bach')
                temp_list.append(chord_frequency([x], mode, progression_element, tab)[numeral])
        source_percentages.append(temp_list)
    print(source_percentages)
    for x in source_percentages:
        distance_list = []
        for y in source_percentages:
            distances = euclidean(x, y)
            # distances = 100 - pearsonr(x, y)[0] * 100
            distance_list.append(distances)
        source_distances.append(distance_list)
    print(source_distances)
    A = np.array(source_distances)
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
            distances = 100 - pearsonr(x, y)[0] * 100
            distance_list.append(distances)
        source_distances.append(distance_list)
    print(source_distances)
    A = np.array(source_distances)
    print('A', A)
    return A



dt = [('len', float)]
# A = (mds_graph_chordFQ(all_corpus, 'major', 'all', 'guitar')/3).view(dt)
A = (mds_graph_ngram(all_alfabeto, 3, 'all', 10, 'all', 'guitar')/2).view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, {0:'kap 1610', 1:'kap 1619a', 2:'kap 1619b', 3:'kap 1623', 4:'obizzi 1627', 5: 'stefani 1621',
                         6: 'abbatessa 1650', 7:'sanz 1674',
                         8: 'bach', 9: 'palestrina', 10: 'monteverdi', 11: 'haydn', 12: 'mozart', 13: 'beethoven'})

G = to_agraph(G)

G.node_attr.update(color="green", style="filled")
G.edge_attr.update(color="blue", line_width=0.03)

G.draw('/home/daniel/Desktop/euclidean_DIS_bigram_maj.svg', format='svg', prog='neato')
# G.draw('test321.png')
    # nx.draw(G, prog='neato')
# plt.show()
