from time import time
from alfabeto_sources.all_sources import *
from alfabeto_code.AlfabetoConverter import transposed_pc_chords_noMMD
from alfabeto_data.pickled_data import *
from alfabeto_data.harmonic_function_data import *
from Continuo.ContinuoConverter import figure_intervals_pc, book_converter_pc_untransposed
from Continuo.ContinuoMarkov import scale_degree_harmonization_song, scale_degree_harmonization_song_untransposed, scale_degree_harmonization
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, to_agraph
from decimal import Decimal
from scipy.spatial.distance import euclidean, cityblock
from music21 import *
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.externals import joblib
import csv, copy, os
from itertools import cycle



"""-------harmonic function----------"""

def corpus_chord_data(list_of_songs_with_keys):
    def song_chords(chord_data): #converts chordify/key data into chord/key data
        final_data = []
        for x in range(1, len(chord_data)):
            xchord1 = sorted([(i + chord_data[x-1][0])%12 for i in chord_data[x-1][1]])
            xchord2 = sorted([(i + chord_data[x][0])%12 for i in chord_data[x][1]])
            chord1 = chord_data[x-1]
            chord2 = chord_data[x]
            if chord1 != chord2 and len(chord1[-1]) >= 3 and xchord1 != xchord2:
                if chord2[0] == chord1[0] and \
                                set(chord2[-1]).issuperset(set(chord1[-1])) is False:
                    if len(final_data) >= 1:
                        if chord1[0] != final_data[-1][0]:
                            final_data.append(chord1)
                        elif set(chord1[1]).issubset(set(final_data[-1][1])) is False:
                            final_data.append(chord1)
                    else:
                        final_data.append(chord1)
                elif chord1[0] != chord2[0]:
                    if len(final_data) >= 1:
                        if chord1[0] != final_data[-1][0]:
                            final_data.append(chord1)
                        elif set(chord1[1]).issubset(set(final_data[-1][1])) is False:
                            final_data.append(chord1)
                    else:
                        final_data.append(chord1)
        if len(chord_data[-1][-1]) >= 3 and chord_data[-1] != final_data[-1] and \
                sorted([(x + chord_data[-1][0])%12 for x in chord_data[-1][1]]) != \
                        sorted([(x + final_data[-1][0])%12 for x in final_data[-1][1]]):
            final_data.append(chord_data[-1])

        return final_data
    all_song_data = []
    for x in list_of_songs_with_keys[0]:
        all_song_data.append(song_chords(x))
    return all_song_data, list_of_songs_with_keys[1]

def bigram_numbers_roots(corpus, modes): #just the alfabeto chords, no bass notes
    X = []
    for a, b in zip(corpus[0], corpus[1]):
        if b in modes:
            X.append(a)
    root_data = {}
    final_roots = []
    csv_data = []
    total_chords = 0
    for x in X:
        for y in x:
            if y in root_data:
                root_data[y] += 1
                total_chords += 1
            else:
                root_data[y] = 1
                total_chords += 1
    for x in root_data.keys():
        if root_data[x] >= .01 * total_chords:
            final_roots.append(x)
    after_labels = [' ']
    for x in final_roots:
        after_labels.append(x)
    csv_data.append(after_labels)
    for numeral in final_roots:
        csv_temp = []
        csv_temp.append(numeral)
        numeral_after_dict = {}
        for x in root_data.keys():
            numeral_after_dict[x] = 0
        for x in X:
            for y in range(1, len(x)):
                if x[y - 1] == numeral:
                    numeral_after_dict[x[y]] += 1
                    total_chords += 1
        for x in final_roots:
            csv_temp.append(numeral_after_dict[x])
        csv_data.append(csv_temp)

    print(total_chords)
    return csv_data

def hmm_sequence(corpus, modes): #just the alfabeto chords, no bass notes
    X = []
    numerals = ['I', 'i', 'bII', 'bii', 'II', 'ii',
                'bIII', 'biii', 'III', 'iii', 'IV', 'iv',
                '#IV', '#iv', 'V', 'v', 'bVI', 'bvi',
                'VI', 'vi', 'bVII', 'bvii', 'VII', 'vii']
    for book in corpus:
        for song in book.values():
            #         print(song['alfabeto'])
            attempt_mode = (song['data']['key'], song['data']['final'])
            if modes == 'all':
                num_list = transposed_pc_chords_noMMD(song['alfabeto'], 'all')
                converted = [numerals.index(a)+1 for a in num_list]
                X.append(converted)
            elif attempt_mode in modes:
                num_list = transposed_pc_chords_noMMD(song['alfabeto'], 'all')
                converted = [numerals.index(a)+1 for a in num_list]
                X.append(converted)
    Y = str(X)
    Z = '{'
    for x in Y[1:-1]:
        if x != ' ':
            Z += x
    Z += '}'
    return Z

# def python_hmm(corpus, modes):#just chords
#     X = []
#     all_numerals = ['I', 'i', 'bII', 'bii', 'II', 'ii', 'bIII', 'biii', 'III', 'iii', 'IV', 'iv',
#                     '#IV', '#iv', 'V', 'v', 'bVI', 'bvi', 'VI', 'vi', 'bVII', 'bvii', 'VII', 'vii']
#     numerals = []
#     ordered_numerals = []
#     for book in corpus:
#         for song in book.values():
#             attempt_mode = (song['data']['key'], song['data']['final'])
#             if modes == 'all':
#                 X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
#             elif attempt_mode in modes:
#                 X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
#     for x in X:
#         for y in x:
#             if y not in numerals:
#                 numerals.append(y)
#     for x in all_numerals:
#         for y in numerals:
#             if x == y:
#                 ordered_numerals.append(y)
#     XX = []
#     Xlen = []
#     for x in X:
#         Xlen.append(len(x))
#         for y in x:
#             XX.append([ordered_numerals.index(y)])
#     return np.array(XX), Xlen, ordered_numerals

def python_hmm(corpus, modes, datatype):
    X = []
    numerals = []
    ordered_numerals = []
    for book in corpus:
        for song in book.values():
            attempt_mode = (song['data']['key'], song['data']['final'])
            if modes == 'all':
                if datatype == 'chords':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif datatype == 'continuo':
                    X.append(figure_intervals_pc(song, 'all'))
            elif attempt_mode in modes:
                if datatype == 'chords':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif datatype == 'continuo':
                    X.append(figure_intervals_pc(song, 'all'))
    for x in X:
        for y in x:
            if y not in numerals:
                numerals.append(y)
    for x in ordered_numeral_list:
        for y in numerals:
            if datatype == 'chords':
                if x == y:
                    ordered_numerals.append(y)
            elif datatype == 'continuo':
                if numerals_to_data[x] == y:
                    ordered_numerals.append(x)
    XX = []
    Xlen = []
    X_temp = []
    for x in X:
        temp_list = []
        for y in x:
            if datatype == 'chords':
                temp_list.append(0)
                XX.append([ordered_numerals.index(y)])
            elif datatype == 'continuo':
                for a, b in numerals_to_data.items():
                    if y == b:
                        temp_list.append(0)
                        XX.append([ordered_numerals.index(a)])
        X_temp.append(temp_list)
    for x in X_temp:
        Xlen.append(len(x))
    return np.array(XX), Xlen, ordered_numerals

def python_hmm_corpus(corpus, modes):#continuo_data
    X = []
    numerals = []
    ordered_numerals = []
    for a, b in zip(corpus[0], corpus[1]):
        if b in modes:
            X.append(a)
    for x in X:
        for y in x:
            if y not in numerals:
                numerals.append(y)
    for x in ordered_numeral_list:
        for y in numerals:
            if numerals_to_data[x] == y:
                ordered_numerals.append(x)
    XX = []
    X_temp = []
    Xlen = []
    for x in X:
        temp_list = []
        for y in x:
            for a, b in numerals_to_data.items():
                if y == b:
                    temp_list.append(0)
                    XX.append([ordered_numerals.index(a)])
        X_temp.append(temp_list)
    for x in X_temp:
        if len(x) > 0:
            Xlen.append(len(x))
    return np.array(XX), Xlen, ordered_numerals

def hmm2(alfabeto_source, modes): #alfabeto chords with bass notes
    X = []
    X2 = []
    for book in alfabeto_source:
        for song in book.values():
            attempt_mode = (song['data']['key'], song['data']['final'])
            if modes == 'all':
                X.append(figure_intervals_pc(song, 'all'))
            elif attempt_mode in modes:
                X.append(figure_intervals_pc(song, 'all'))
    all_chords = {}
    all_chord_numbers = 0
    for x in X:
        for y in x:
            all_chord_numbers += 1
    for x in X:
        for y in x:
            if str(y) not in all_chords.keys():
                all_chords[str(y)] = 1
            else:
                all_chords[str(y)] += 1
    all_chords_final = []
    all_numerals_final = []
    for x, y in all_chords.items():
        if y / all_chord_numbers >= .01:
            all_chords_final.append(x)
    for x in all_chords_final:
        for i, j in numerals_to_data.items():
            if str(j) == x:
                all_numerals_final.append(i)
    final_chord_list = []
    final_numeral_list = []
    for x in X:
        song_list = []
        song_numerals = []
        for a in range(1, len(x)):
            if str(x[a-1]) in all_chords_final:
                for i, j in numerals_to_data.items():
                    if x[a-1] == j:
                        song_list.append(all_numerals_final.index(i)+1)
                        song_numerals.append(i)
        if str(x[-1]) in all_chords_final:
            for i, j in numerals_to_data.items():
                if j == x[-1]:
                    if all_numerals_final.index(i)+1 != song_list[-1]:
                        song_list.append(all_numerals_final.index(i)+1)
                        song_numerals.append(i)
        final_chord_list.append(song_list)
        final_numeral_list.append(song_numerals)
    Y = str(final_chord_list)
    Z = '{'
    for x in Y[1:-1]:
        if x != ' ':
            Z += x
    Z += '}'
    return Z, final_numeral_list, all_numerals_final


def bigram_graphs_alfabeto(corpus, modes, accompaniment):
    """accompaniment meaning "alfabeto" or "continuo\""""
    X = []
    bigram_dict = {}
    total_bigrams = 0
    for book in corpus:
        for song in book.values():
            #         print(song['alfabeto'])
            if accompaniment == 'chords':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif attempt_mode in modes:
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
            elif accompaniment == 'continuo':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(figure_intervals_pc(song, 'all'))
                elif attempt_mode in modes:
                    X.append(figure_intervals_pc(song, 'all'))
    if accompaniment == 'continuo':
        newx = []
        for song in X:
            newsong = []
            for chord in song:
                for a, b in numerals_to_data.items():
                    if chord == b:
                        newsong.append(a)
            newx.append(newsong)
        X = newx
    for song in X:
        total_bigrams += len(song)-1
    for song in X:
        for chord in range(1, len(song)):
            if song[chord-1] not in bigram_dict:
                bigram_dict[song[chord-1]] = {}
            if song[chord] not in bigram_dict[song[chord-1]] and song[chord] != song[chord-1]:
                bigram_dict[song[chord-1]][song[chord]] = 1/total_bigrams
                # total_bigrams += 1
            elif song[chord] != song[chord-1]:
                bigram_dict[song[chord-1]][song[chord]] += 1/total_bigrams
                # total_bigrams += 1
    # for a, b in bigram_dict.items():
    #     for c, d in b.items():
    #         d = d/total_bigrams
    return bigram_dict

def neato_function_bigrams(bigram_dict, threshold, path):
    """this makes a DOT graph of chord bigrams"""
    G = nx.DiGraph()
    # labels = [x + 1 for x in range(K)]
    # for x, y in zip(trans, labels):
    #     for a, b in zip(x, labels):
    #         if a >= .25:
    #             G.add_edge(y, b, penwidth=a * 8, weight=int(a * 100))
    for label, data in bigram_dict.items():
        for a, b in data.items():
            if b >= threshold:
                G.add_edge(label, a, penwidth=b*50, weight=int(b*500))
    edge_weights = []
    edges = G.edges(data=True)
    #             print('edges:', edges)
    for x in edges:
        edge_weights.append(x[2]['penwidth'])
    nodes = G.nodes()
    #             print('nodes:', nodes)
    for x in range(len(nodes)):
        # G.node[nodes[x]]['shape'] = 'none'
        # G.node[nodes[x]]['image'] = '/home/daniel/Desktop/pie/%s/%s/%s_%s.svg' % (corpus_name, mode, K, x)
        G.node[nodes[x]]['fontcolor'] = 'blue'
        G.node[nodes[x]]['fontsize'] = 12
    G = to_agraph(G)
    # G=pgv.AGraph(ranksep=10)
    G.draw(path, format='pdf', prog='dot')

def alf_function_graph_maker(accompaniment, mode, threshold, path):
    all_kaps = {'kap1': [GetComposer.all_kaps[0]], 'kap2': [GetComposer.all_kaps[1]], 'kap3': [GetComposer.all_kaps[2]],
                'kap4': [GetComposer.all_kaps[3]], 'kap5': [GetComposer.all_kaps[4]], 'kap6': [GetComposer.all_kaps[5]],
                'kap7': [GetComposer.all_kaps[6]]}
    for a, b in all_kaps.items():
        neato_function_bigrams(bigram_graphs_alfabeto(b, mode, accompaniment), threshold, path+'%s.pdf' % a)


def bigram_numbers_alfabeto(corpus, modes): #just the alfabeto chords, no bass notes
    X = []
    csv_data = []
    for book in corpus:
        for song in book.values():
            #         print(song['alfabeto'])
            attempt_mode = (song['data']['key'], song['data']['final'])
            if modes == 'all':
                X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
            elif attempt_mode in modes:
                X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
    numerals = ['I', 'i', 'bII', 'bii', 'II', 'ii',
                'bIII', 'biii', 'III', 'iii', 'IV', 'iv',
                '#IV', '#iv', 'V', 'v', 'bVI', 'bvi',
                'VI', 'vi', 'bVII', 'bvii', 'VII', 'vii']
    numeral_data = {}
    final_numerals = []
    total_chords = 0
    for x in numerals:
        numeral_data[x] = 0
    for x in X:
        for y in x:
            numeral_data[y] += 1
            total_chords += 1
    print(numeral_data)
    for x in numerals:
        if numeral_data[x] >= .01 * total_chords:
            final_numerals.append(x)
    after_labels = [' ']
    for x in final_numerals:
        after_labels.append(x)
    csv_data.append(after_labels)
    for numeral in final_numerals:
        csv_temp = []
        csv_temp.append(numeral)
        numeral_after_dict = {}
        for x in numerals:
            numeral_after_dict[x] = 0
        for x in X:
            for y in range(1, len(x)):
                if x[y - 1] == numeral:
                    numeral_after_dict[x[y]] += 1
                    total_chords += 1
        for x in final_numerals:
            csv_temp.append(numeral_after_dict[x])
        csv_data.append(csv_temp)

    print(total_chords)
    return csv_data

def trigram_function_1(corpus, accompaniment, modes):
    X = []
    # bigram_dict = {}
    # total_bigrams = 0
    for book in corpus:
        for song in book.values():
            #         print(song['alfabeto'])
            if accompaniment == 'chords':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif attempt_mode in modes:
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
            elif accompaniment == 'continuo':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(figure_intervals_pc(song, 'all'))
                elif attempt_mode in modes:
                    X.append(figure_intervals_pc(song, 'all'))
    if accompaniment == 'continuo':
        newx = []
        for song in X:
            newsong = []
            for chord in song:
                for a, b in numerals_to_data.items():
                    if chord == b:
                        newsong.append(a)
            newx.append(newsong)
        X = newx
    labels = []
    scores = []
    print('getting labels')
    for song in X:
        labels.append(song[0])
        scores.append(('beginning', song[1]))
        for chord in range(1, len(song)-1):
            labels.append(song[chord])
            scores.append((song[chord-1], song[chord+1]))
        labels.append(song[-1])
        scores.append((song[-2], 'end'))
    from difflib import SequenceMatcher
    dist_scores = []
    print('scoring, please wait a while or go get a drink of water.')
    for x in scores:
        numeral_list = []
        for y in scores:
            numeral_list.append(SequenceMatcher(None, x, y).ratio())
        dist_scores.append(numeral_list)
        print('finished a chord')
    return dist_scores, labels



def trigram_function(corpus, accompaniment, modes):
    X = []
    # bigram_dict = {}
    # total_bigrams = 0
    for book in corpus:
        for song in book.values():
            #         print(song['alfabeto'])
            if accompaniment == 'chords':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif attempt_mode in modes:
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
            elif accompaniment == 'continuo':
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(figure_intervals_pc(song, 'all'))
                elif attempt_mode in modes:
                    X.append(figure_intervals_pc(song, 'all'))
    if accompaniment == 'continuo':
        newx = []
        for song in X:
            newsong = []
            for chord in song:
                for a, b in numerals_to_data.items():
                    if chord == b:
                        newsong.append(a)
            newx.append(newsong)
        X = newx
    ant_cons = []
    labels = []
    scores = []
    number_of_chords = 0
    print('making ant_cons labels')
    for song in X:
        for chord in song:
            number_of_chords += 1
            for song_ in X:
                for chord_ in song_:
                    if (chord, chord_) not in ant_cons:
                        ant_cons.append((chord, chord_))
            if ('beginning', chord) not in ant_cons:
                ant_cons.append(('beginning', chord))
            if (chord, 'end') not in ant_cons:
                ant_cons.append((chord, 'end'))
    print('calculating data...')
    for song in X:
        print('starting song...')
        first = ('beginning', song[1]) #documents first chord
        first_list = []
        for x in ant_cons:
            if x == first:
                first_list.append(1)
            else:
                first_list.append(0)
        scores.append(first_list)
        labels.append(song[0])
        for chord in range(1, len(song)-1):
            if song[chord] != song[chord-1]:
                chord_scores = []
                ac = (song[chord-1], song[chord+1])
                labels.append(song[chord])
                for y in ant_cons:
                    if ac == y:
                        chord_scores.append(1)
                    else:
                        chord_scores.append(0)
                scores.append(chord_scores)
        last = (song[-2], 'end') #documents last chord
        labels.append(song[-1])
        last_list = []
        for x in ant_cons:
            if x == last:
                last_list.append(1)
            else:
                last_list.append(0)
        scores.append(last_list)
        print('finished %s of %s songs' % (X.index(song), len(X)))
    return scores, labels



def bigram_numbers_continuo(alfabeto_source, modes): #alfabeto chords with bass notes
    X = []
    for book in alfabeto_source:
        for song in book.values():
            attempt_mode = (song['data']['key'], song['data']['final'])
            if modes == 'all':
                X.append(figure_intervals_pc(song, 'all'))
            elif attempt_mode in modes:
                X.append(figure_intervals_pc(song, 'all'))
    all_chords = {}
    all_chord_numbers = 0
    for x in X:
        for y in x:
            all_chord_numbers += 1
    for x in X:
        for y in x:
            if str(y) not in all_chords.keys():
                all_chords[str(y)] = 1
            else:
                all_chords[str(y)] += 1
    all_chords_final = []
    for x, y in all_chords.items():
        if y / all_chord_numbers >= .01:
            all_chords_final.append(x)
    csv_data = []
    after_labels = [' ']
    for x in all_chords_final:
        after_labels.append(x)
    csv_data.append(after_labels)
    total_chords = 0
    for numeral in all_chords_final:
        csv_temp = []
        csv_temp.append(numeral)
        numeral_after_dict = {}
        for x in all_chords_final:
            numeral_after_dict[x] = 0
        for x in X:
            for y in range(1, len(x)):
                if str(x[y - 1]) == numeral and str(x[y]) in all_chords_final and str(x[y - 1]) != str(x[y]):
                    numeral_after_dict[str(x[y])] += 1
                    total_chords += 1
        for x in all_chords_final:
            csv_temp.append(numeral_after_dict[x])
        csv_data.append(csv_temp)
    return csv_data

# def bigram_numbers_continuo(alfabeto_source, modes): #alfabeto chords with bass notes
#     X = []
#     for book in alfabeto_source:
#         for song in book.values():
#             attempt_mode = (song['data']['key'], song['data']['final'])
#             if modes == 'all':
#                 X.append(figure_intervals_pc(song, 'all'))
#             elif attempt_mode in modes:
#                 X.append(figure_intervals_pc(song, 'all'))
#     all_chords = {}
#     all_chord_numbers = 0
#     newx = []
#     for song in X:
#         newsong = []
#         for chord in song:
#             for a, b in numerals_to_data.items():
#                 if chord == b:
#                     newsong.append(a)
#         newx.append(newsong)
#     X = newx
#     for x in X:
#         for y in x:
#             all_chord_numbers += 1
#     for x in X:
#         for y in x:
#             if y not in all_chords.keys():
#                 all_chords[y] = 1
#             else:
#                 all_chords[y] += 1
#
#     print(all_chords)
#     all_chords_final = []
#     for x, y in all_chords.items():
#         if y / all_chord_numbers >= .01:
#             all_chords_final.append(x)
#     csv_data = []
#     after_labels = [' ']
#     for x in all_chords_final:
#         after_labels.append(x)
#     csv_data.append(after_labels)
#     total_chords = 0
#     print(all_chords_final)
#     for numeral in all_chords_final:
#         csv_temp = []
#         csv_temp.append(numeral)
#         numeral_after_dict = {}
#         for x in all_chords_final:
#             numeral_after_dict[x] = 0
#         for x in X:
#             for y in range(1, len(x)):
#                 c1 = x[y-1]
#                 c2 = x[y]
#                 if c1 == numeral and c2 in all_chords_final and c1 != c2:
#                     total_chords += 1
#                     numeral_after_dict[c1] += 1/total_chords
#         for x in all_chords_final:
#             csv_temp.append(numeral_after_dict[x])
#         csv_data.append(csv_temp)
#     return csv_data


def bigram_numbers_corpus(corpus_data_tuples, modes):  # chord/key data into csv-ready functions
    all_keys = []
    X = []
    for x, y in zip(corpus_data_tuples[0], corpus_data_tuples[1]):
        if modes == 'all':
            temp_list = []
            for z in x:
                temp_list.append(''.join(map(str, z)))
            X.append(temp_list)
            print(temp_list)
            all_keys.append(y)
        elif y in modes:
            temp_list = []
            for z in x:
                temp_list.append(str(z))
            X.append(temp_list)
            all_keys.append(y)
    all_chords = {}
    all_chord_numbers = 0
    for x in X:
        for y in x:
            all_chord_numbers += 1
    for x in X:
        for y in x:
            if str(y) not in all_chords.keys():
                all_chords[str(y)] = 1
            else:
                all_chords[str(y)] += 1
    all_chords_final = []
    for x, y in all_chords.items():
        if y / all_chord_numbers >= .01:
            all_chords_final.append(x)

    csv_data = []
    after_labels = [' ']
    for x in all_chords_final:
        after_labels.append(x)
    csv_data.append(after_labels)
    total_chords = 0
    for numeral in all_chords_final:
        csv_temp = []
        csv_temp.append(numeral)
        numeral_after_dict = {}
        for x in all_chords_final:
            numeral_after_dict[x] = 0
        for x in X:
            for y in range(1, len(x)):
                if str(x[y - 1]) == numeral and str(x[y]) in all_chords_final and str(x[y - 1]) != str(x[y]):
                    numeral_after_dict[str(x[y])] += 1
                    total_chords += 1
        for x in all_chords_final:
            csv_temp.append(numeral_after_dict[x])
        csv_data.append(csv_temp)
    print(total_chords)
    return csv_data

all_modal = [(-1, 5), (0, 0), (-1, 0), (0, 7), (-1, 10), (0, 5), (0, 2), (0, 9), (-1, 2), (-1, 7), (0, 4)]

all_flats = [('f', 5), ('f', 0), ('f', 10), ('f', 2), ('f', 7)]
all_naturals = [('n', 0), ('n', 7), ('n', 5), ('n', 2), ('n', 9), ('n', 4)]

modal_major = [('f', 5), ('n', 0), ('f', 0), ('n', 7), ('f', 10), ('n', 5),
               (-1, 5), (0, 0), (-1, 0), (0, 7), (-1, 10), (0, 5)]
modal_minor = [('n', 2), ('n', 9), ('f', 2), ('f', 7), ('n', 4),
               (0, 2), (0, 9), (-1, 2), (-1, 7), (0, 4)]
tonal_major_dict = {(0, 0): 'CM', (1, 7): 'GM', (2, 2): 'DM', (3, 9): 'AM', (4, 4): 'EM', (5, 11): 'BM', (6, 6): 'F♯M',
               (-1, 5): 'FM', (-2, 10): 'B♭M', (-3, 3): 'E♭M', (-4, 8): 'A♭M', (-5, 1): 'D♭M', (-6, 6): 'G♭M'}
tonal_minor_dict = {(0, 9): 'am', (1, 4): 'em', (2, 11): 'bm', (3, 6): 'f♯m', (4, 1): 'c♯m', (5, 8): 'g♯m',
                    (6, 3): 'd♯m', (-1, 2): 'dm', (-2, 7): 'gm', (-3, 0): 'cm', (-4, 5): 'fm', (-5, 10): 'b♭m',
                    (-6, 3): 'e♭m'}
modal_types = {'ionian': [('f', 5), (-1, 5), ('n', 0), (0, 0)],
               'dorian': [('n', 2), (0, 2), ('f', 7), (-1, 7)],
               'phrygian': [('n', 4), (0, 4), ('f', 9), (-1, 9)],
               'lydian': [('n', 5), (0, 5), ('f', 10), (0, 10)],
               'mixolydian': [('n', 7), (0, 7), ('f', 0), (-1, 0)],
               'aeolian': [('n', 9), (0, 9), ('f', 2), (-1, 2)]}
tonal_major = [x for x in tonal_major_dict.keys()]
tonal_minor = [x for x in tonal_minor_dict.keys()]

def function_mapper(corpus, modes, cluster, source, path): #saves function arrow graph as pdf
    X = []

    if source == 'alfabeto':
        for book in corpus:
            for song in book.values():
                #         print(song['alfabeto'])
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
                elif attempt_mode in modes:
                    X.append(transposed_pc_chords_noMMD(song['alfabeto'], 'all'))
    elif source == 'alfabeto continuo':
        for book in corpus:
            for song in book.values():
                attempt_mode = (song['data']['key'], song['data']['final'])
                if modes == 'all':
                    X.append(figure_intervals_pc(song, 'all'))
                elif attempt_mode in modes:
                    X.append(figure_intervals_pc(song, 'all'))
    else:
        for x, y in zip(corpus[0], corpus[1]):
            if modes == 'all':
                X.append(x)
            elif y in modes:
                X.append(x)
    function_data = []
    cluster_groupings = {}
    for a, b in cluster.items():
        cluster_groupings[a] = {}
        for c in b:
            cluster_groupings[a][c] = 0
    for x in X:
        temp_list = []
        for y in x:
            for c, d in numerals_to_data.items():
                if y == d:
                    for a, b in cluster.items():
                        # print(c, b)
                        if c in b:
                            temp_list.append(a)
                            cluster_groupings[a][c] += 1

        function_data.append(temp_list)
    cluster_dict = {}
    print(cluster_groupings)
    for x in cluster.keys():
        for y in cluster.keys():
            cluster_dict[(x, y)] = 0
    for x in function_data:
        for y in range(1, len(x)):
            cluster_dict[(x[y - 1], x[y])] += 1
    total_chord_changes = 0
    for x in cluster_dict.values():
        total_chord_changes += x
    print('total chord changes:', total_chord_changes)

    # networkx graph
    G = nx.DiGraph()
    for x, y in cluster_dict.items():
        if y > .01 * total_chord_changes:
            G.add_edge(x[0], x[1], penwidth=y / total_chord_changes * 20)  #
            #                        label=Decimal(str(y/total_chord_changes*100)).quantize(Decimal('.00')))
    edge_weights = []
    edges = G.edges(data=True)
    print('edges:', edges)
    for x in edges:
        edge_weights.append(x[2]['penwidth'])
    nodes = G.nodes()
    print('nodes:', nodes)
    for x in nodes:
        G.node[x]['shape'] = 'plaintext'
    # pos = nx.circular_layout(G)
    # nx.draw_networkx_edges(G, pos, edges=edges, edge_color='green', width=edge_weights, alpha=.5)
    # nx.draw_networkx_nodes(G, pos, node_color='green')
    # nx.draw_networkx_labels(G, pos)
    # write_dot(G, path)
    G = to_agraph(G)
    G.draw(path, format='pdf', prog='dot')
    print(cluster_dict)
    return cluster_groupings


"""---------kmeans cluster--------------"""

temp_maj = {0: 0.184, 1: 0.001, 2: 0.155, 3: 0.003, 4: 0.191,
            5: 0.109, 6: 0.005, 7: 0.214, 8: 0.001, 9: 0.078,
            10: 0.004, 11: 0.055}

temp_min = {0: 0.192, 1: 0.005, 2: 0.149, 3: 0.179, 4: 0.002,
            5: 0.144, 6: 0.002, 7: 0.201, 8: 0.038, 9: 0.012,
            10: 0.053, 11: 0.022}

t_maj = [temp_maj[x] * 100 for x in range(12)]
t_min = [temp_min[x] * 100 for x in range(12)]


def temperley_appender(corpus_data): #appends temperley's stuff to dataset
    dataset = copy.deepcopy(corpus_data)
    dataset[0].append(t_maj)
    dataset[0].append(t_min)
    dataset[1].append('TMAJ')
    dataset[1].append('TMIN')
    return dataset

# bach_kmeans_data = temperley_appender(bach_notes_data)
# pal_kmeans_data = temperley_appender(palestrina_notes_data)
# alf_kmeans_data = temperley_appender(alfabeto_notes_data)

tonal_fixer = {(0, 0): 'CM', (0, 9): 'am', (1, 7): 'GM', (1, 4): 'em', (2, 2): 'DM', (2, 11): 'bm',
               (3, 9): 'AM', (3, 6): 'f♯m', (4, 4): 'EM', (4, 1): 'c♯m', (5, 11): 'BM', (5, 8): 'g♯m',
               (6, 6): 'F♯M', (6, 3): 'd♯m',
               (-1, 5): 'FM', (-1, 2): 'dm', (-2, 10): 'B♭M', (-2, 7): 'gm', (-3, 3): 'E♭M', (-3, 0): 'cm',
               (-4, 8): 'A♭M', (-4, 5): 'fm', (-5, 1): 'D♭M', (-5, 10): 'b♭m', (-6, 6): 'G♭M', (-6, 3): 'e♭m'}


def label_maker(label_tuples):
    final_labels = []
    for x in label_tuples:
        if x in tonal_fixer.keys():
            final_labels.append('$' + tonal_fixer[x] + '$')
        elif x == 'TMAJ':
            final_labels.append('$M$')
        elif x == 'TMIN':
            final_labels.append('$m$')
        else:
            print('whaaaa!!!', x)
            final_labels.append('o')

    return final_labels

def scale_degree_harmonization_bach(song):
    harmonization_data = {}
    for x in song:
        if str(x) in harmonization_data:
            harmonization_data[str(x)] += 1/len(song) * 100
        else:
            harmonization_data[str(x)] = 1/len(song) * 100
    return harmonization_data

def figure_sorter(function):
    final_data = []
    other_numbers = []
    figures = [[0, 4, 7], [0, 3, 7], [0, 3, 8], [0, 4, 9], [0, 5, 9], [0, 5, 8]]
    for figure in figures:
        figure_list = []
        for number in range(12):
            fig = str([number, figure])
            if fig in function:
                figure_list.append(function[fig])
            else:
#                 figure_list.append('-')
                figure_list.append(0)
        final_data.append(figure_list)
    for number in range(12):
        numbers = 0
        for x, y in function.items():
            if x[1:3] == str(number) and x[-10:-1] not in str(figures):
                numbers += y
            elif x[1:2] == str(number) and x[-10:-1] not in str(figures):
                numbers += y
        other_numbers.append(numbers)
    other_final = []
    for x in other_numbers:
        if x > 0:
            other_final.append(x)
        else:
            other_final.append('-')
#     final_data.append(other_final) # if you want dashes instead of 0's #---none of these if no other desired
    final_data.append(other_numbers) # if you want 0's instead of dashes
    return final_data


def inversion_kmeans_corpus(corpus, mode_list, corpus_type, label_function):
    all_modes = []
    if mode_list == 'all':
        if corpus_type == 'tonal':
            each_mode = [m for m in tonal_fixer.keys()]
            for x in each_mode:
                all_modes.append(x)
        elif corpus_type == 'modal':
            each_mode = all_modal
            for x in each_mode:
                all_modes.append(x)
    else:
        for x in mode_list:
            all_modes.append(x)
    labels = []
    final_songs = []
    final_songs_reduced = []
    for x in all_modes:
        for a, b in zip(corpus[0], corpus[1]):
            if b == x:
                temp_list = []
                matrix_data = figure_sorter(scale_degree_harmonization_bach(a))
                for a in matrix_data:
                    for b in a:
                        temp_list.append(b)
                final_songs.append(temp_list)
                labels.append(x)
    final_labels = []
    if type(label_function) is None:
        for x in labels:
            final_labels.append(x)
    else:
        lab = label_function(labels)
        for x in lab:
            final_labels.append(x)
    for x in final_songs:
        for y in x:
            final_songs_reduced.append(y)

    return final_songs, final_labels


def inversion_kmeans(corpus, mode_list, label_function):
    all_modes = []
    if mode_list == 'all':
        each_mode = [('f', 0), ('f', 2), ('f', 5), ('f', 7), ('f', 9), ('f', 10),
                     ('n', 0), ('n', 2), ('n', 4), ('n', 5), ('n', 7), ('n', 9)]
        for x in each_mode:
            all_modes.append(x)
    else:
        for x in mode_list:
            all_modes.append(x)
    labels = []
    final_songs = []
    final_songs_reduced = []
    for x in all_modes:
        for y in corpus:
            for z in y.values():
                if z['data']['key'] == x[0] and z['data']['final'] == x[1]:
                    temp_list = []
                    matrix_data = (figure_sorter(scale_degree_harmonization_song(z, x)))
                    for a in matrix_data:
                        for b in a:
                            temp_list.append(b)
                    final_songs.append(temp_list)
                    labels.append(x)
    final_labels = []
    if type(label_function) is None:
        for x in labels:
            final_labels.append(x)
    else:
        lab = label_function(labels)
        for x in lab:
            final_labels.append(x)
    for x in final_songs:
        for y in x:
            final_songs_reduced.append(y)

    return final_songs, final_labels

#bass harmonization data that is untransposed
def inversion_kmeans_untransposed(corpus, mode_list, label_function):
    all_modes = []
    if mode_list == 'all':
        each_mode = [('f', 0), ('f', 2), ('f', 5), ('f', 7), ('f', 9), ('f', 10),
                     ('n', 0), ('n', 2), ('n', 4), ('n', 5), ('n', 7), ('n', 9)]
        for x in each_mode:
            all_modes.append(x)
    else:
        for x in mode_list:
            all_modes.append(x)
    labels = []
    final_songs = []
    final_songs_reduced = []
    for x in all_modes:
        for y in corpus:
            for z in y.values():
                if z['data']['key'] == x[0] and z['data']['final'] == x[1]:
                    temp_list = []
                    # print(z, x)
                    matrix_data = (figure_sorter(scale_degree_harmonization_song_untransposed(z, x)))
                    for a in matrix_data:
                        for b in a:
                            temp_list.append(b)
                    final_songs.append(temp_list)
                    labels.append(x)
    final_labels = []
    if type(label_function) is None:
        for x in labels:
            final_labels.append(x)
    else:
        lab = label_function(labels)
        for x in lab:
            final_labels.append(x)
    for x in final_songs:
        for y in x:
            final_songs_reduced.append(y)

    return final_songs, final_labels

def labeler(label_data):
    final_labels = []
    for x in label_data:
        if x == ('f', 2):
            final_labels.append('$♭:D$')
        elif x == ('n', 4):
            final_labels.append('$♮:E$')
        elif x == ('n', 9):
            final_labels.append('$♮:A$')
        elif x == ('f', 7):
            final_labels.append('$♭:G$')
        elif x == ('n', 2):
            final_labels.append('$♮:D$')
        elif x == ('f', 9):
            final_labels.append('$♭:A$')
        elif x == ('f', 0):
            final_labels.append('$♭:C$')
        elif x == ('f', 10):
            final_labels.append('$♭:B♭$')
        elif x == ('n', 5):
            final_labels.append('$♮:F$')
        elif x == ('n', 0):
            final_labels.append('$♮:C$')
        elif x == ('f', 5):
            final_labels.append('$♭:F$')
        elif x == ('n', 7):
            final_labels.append('$♮:G$')
        elif x == 'Temperley MAJOR':
            final_labels.append('$Temperley MAJOR$')
        elif x == 'Temperley MINOR':
            final_labels.append('$Temperley MINOR$')
        else:
            final_labels.append('o')
    return final_labels

def label_maker_alfabeto(corpus_list):
    alf_labels = []
    for x in corpus_list:  # do this if the tuples are in list of list
        if x == ('f', 2) or x == (-1, 2):
            alf_labels.append('$♭:D$')
        elif x == ('n', 4) or x == (0, 4):
            alf_labels.append('$♮:E$')
        elif x == ('f', 4) or x == (-1, 4):
            alf_labels.append('$♭:E$')
        elif x == ('n', 9) or x == (0, 9):
            alf_labels.append('$♮:A$')
        elif x == ('f', 7) or x == (-1, 7):
            alf_labels.append('$♭:G$')
        elif x == ('n', 2) or x == (0, 2):
            alf_labels.append('$♮:D$')
        elif x == ('f', 9) or x == (-1, 9):
            alf_labels.append('$♭:A$')
        elif x == ('f', 0) or x == (-1, 0):
            alf_labels.append('$♭:C$')
        elif x == ('f', 10) or x == (-1, 10):
            alf_labels.append('$♭:B♭$')
        elif x == ('n', 5) or x == (0, 5):
            alf_labels.append('$♮:F$')
        elif x == ('n', 0) or x == (0, 0):
            alf_labels.append('$♮:C$')
        elif x == ('f', 5) or x == (-1, 5):
            alf_labels.append('$♭:F$')
        elif x == ('n', 7) or x == (0, 7):
            alf_labels.append('$♮:G$')
        elif x == 'TMAJ':
            alf_labels.append('$M$')
        elif x == 'TMIN':
            alf_labels.append('$m$')
        else:
            alf_labels.append('o')
            print(x)
    return alf_labels

#only if you want A in front of labels
def label_maker_alfabeto_labeled(corpus_list):
    alf_labels = []
    for x in corpus_list:  # do this if the tuples are in list of list
        if x == ('f', 2) or x == (-1, 2):
            alf_labels.append('$A ♭:D$')
        elif x == ('n', 4) or x == (0, 4):
            alf_labels.append('$A ♮:E$')
        elif x == ('f', 4) or x == (-1, 4):
            alf_labels.append('$A ♭:E$')
        elif x == ('n', 9) or x == (0, 9):
            alf_labels.append('$A ♮:A$')
        elif x == ('f', 7) or x == (-1, 7):
            alf_labels.append('$A ♭:G$')
        elif x == ('n', 2) or x == (0, 2):
            alf_labels.append('$A ♮:D$')
        elif x == ('f', 9) or x == (-1, 9):
            alf_labels.append('$A ♭:A$')
        elif x == ('f', 0) or x == (-1, 0):
            alf_labels.append('$A ♭:C$')
        elif x == ('f', 10) or x == (-1, 10):
            alf_labels.append('$A ♭:B♭$')
        elif x == ('n', 5) or x == (0, 5):
            alf_labels.append('$A ♮:F$')
        elif x == ('n', 0) or x == (0, 0):
            alf_labels.append('$A ♮:C$')
        elif x == ('f', 5) or x == (-1, 5):
            alf_labels.append('$A ♭:F$')
        elif x == ('n', 7) or x == (0, 7):
            alf_labels.append('$A ♮:G$')
        elif x == 'TMAJ':
            alf_labels.append('$M$')
        elif x == 'TMIN':
            alf_labels.append('$m$')
        else:
            alf_labels.append('o')
            print(x)
    return alf_labels

#only if you want P in front of labels
def label_maker_pal(corpus_list):
    alf_labels = []
    for x in corpus_list:  # do this if the tuples are in list of list
        if x == ('f', 2) or x == (-1, 2):
            alf_labels.append('$P ♭:D$')
        elif x == ('n', 4) or x == (0, 4):
            alf_labels.append('$P ♮:E$')
        elif x == ('f', 4) or x == (-1, 4):
            alf_labels.append('$P ♭:E$')
        elif x == ('n', 9) or x == (0, 9):
            alf_labels.append('$P ♮:A$')
        elif x == ('f', 7) or x == (-1, 7):
            alf_labels.append('$P ♭:G$')
        elif x == ('n', 2) or x == (0, 2):
            alf_labels.append('$P ♮:D$')
        elif x == ('f', 9) or x == (-1, 9):
            alf_labels.append('$P ♭:A$')
        elif x == ('f', 0) or x == (-1, 0):
            alf_labels.append('$P ♭:C$')
        elif x == ('f', 10) or x == (-1, 10):
            alf_labels.append('$P ♭:B♭$')
        elif x == ('n', 5) or x == (0, 5):
            alf_labels.append('$P ♮:F$')
        elif x == ('n', 0) or x == (0, 0):
            alf_labels.append('$P ♮:C$')
        elif x == ('f', 5) or x == (-1, 5):
            alf_labels.append('$P ♭:F$')
        elif x == ('n', 7) or x == (0, 7):
            alf_labels.append('$P ♮:G$')
        elif x == 'TMAJ':
            alf_labels.append('$M$')
        elif x == 'TMIN':
            alf_labels.append('$m$')
        else:
            alf_labels.append('o')
            print(x)
    return alf_labels

#only if you want B in front of labels
def label_maker_bach(label_tuples):
    final_labels = []
    for x in label_tuples:
        if x in tonal_fixer.keys():
            #             print('$'+'B '+tonal_fixer[x]+'$')
            final_labels.append('$' + 'B ' + tonal_fixer[x] + '$')
        elif x == 'TMAJ':
            final_labels.append('$M$')
        elif x == 'TMIN':
            final_labels.append('$m$')
    return final_labels #o

#saves PDF (or whatever given in path) file of k-means cluster
def k_means_data(list_of_lists, cluster_number, label_markers, path):
    np.random.seed(42)

    digits = np.array(list_of_lists)
    # data = scale(digits)
    data = digits
    label_dict = {}
    label_numbers = []
    n = 0
    label_dict[label_markers[0]] = 0
    for j in range(1, len(label_markers)):
        if label_markers[j] not in label_dict:
            label_dict[label_markers[j]] = n+1
            n += 1

    for i in label_markers:
        label_numbers.append(label_dict[i])
    n_samples, n_features = data.shape
    n_digits = cluster_number
    labels = np.array(label_numbers)
    # print('label numbers', label_numbers)
    # sample_size = 300

    sample_size = len(data)
    # print(sample_size, 'Sample Size')


    print("n_digits: %d, \t n_samples %d, \t n_features %d"
          % (n_digits, n_samples, n_features))

    print(55 * '_')
    print('% 4s' % 'init'' time inertia homo  compl v-meas ARI  AMI  silhouette')

    def bench_k_means(estimator, name, data):
        t0 = time()
        estimator.fit(data)
        print('% 4s %.2fs  %i %.3f %.3f %.3f %.3f %.3f  %.3f'
              % (name, (time() - t0), estimator.inertia_,
                 metrics.homogeneity_score(labels, estimator.labels_),
                 metrics.completeness_score(labels, estimator.labels_),
                 metrics.v_measure_score(labels, estimator.labels_),
                 metrics.adjusted_rand_score(labels, estimator.labels_),
                 metrics.adjusted_mutual_info_score(labels, estimator.labels_),
                 metrics.silhouette_score(data, estimator.labels_,
                                          metric='euclidean',
                                          sample_size=sample_size)))


    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10, precompute_distances=True, n_jobs=-1),
                  name="k++", data=data)

    bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10, precompute_distances=True, n_jobs=-1),
                  name="rand", data=data)

    # in this case the seeding of the centers is deterministic, hence we run the
    # kmeans algorithm only once with n_init=1
    pca = PCA(n_components=n_digits).fit(data)
    bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1, precompute_distances=True, n_jobs=-1),
                  name="PCA",
                  data=data)
    print(55 * '_')

    ###############################################################################
    # Visualize the results on PCA-reduced data

    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 2, reduced_data[:, 0].max() + 2
    y_min, y_max = reduced_data[:, 1].min() - 2, reduced_data[:, 1].max() + 2
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    # plt.set_size_inches(6, 4)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    centroids = kmeans.cluster_centers_

    for x, y, z in zip(reduced_data[:, 0], reduced_data[:, 1], label_markers):
        if z == '$Temperley MAJOR$' or z == '$M$':
            plt.plot(x, y, 'k.', marker='$M$', color='white', markeredgecolor='none', markersize=40)
        elif z == '$Temperley MINOR$' or z == '$m$':
            plt.plot(x, y, 'k.', marker='$m$', color='white', markeredgecolor='none', markersize=40)
        elif z[0] == '*':
            # plt.plot(x, y, 'k.', marker=z[1:], color='white', markeredgecolor='none', markersize=40)
            plt.plot(x, y, 'k.', marker='o', color='white', markeredgecolor='none', markersize=10)
        else:
            plt.plot(x, y, 'k.', marker=z, alpha=.3, markersize=len(z)*4)
            # plt.plot(x, y, 'k.', marker='.', alpha=.4)
#     plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.')
        # plt.plot(x, y, 'k.')
    for i, c in enumerate(centroids):
        cent_label = i+1
        plt.plot(c[0], c[1], marker='$%d$' % cent_label, color='w', markeredgecolor='b', markersize=30)
    # for x in alf_labels:
    #         plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', marker = x, markersize=5)
    #     print('reduced data:', reduced_data)
    # Plot the centroids as a white X

    # plt.scatter(centroids[:, 0], centroids[:, 1],
    #             marker='x', s=169, linewidths=3,
    #             color='w', zorder=10)
    # plt.title('PCA-reduced data\n'
    #           'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(path, bbox_inches='tight')
    plt.show()
    # plt.close()
    # k_data = KMeans(init='k-means++', n_clusters=n_digits, n_init=10).fit(data)
    # return {'silhouette': metrics.silhouette_score(data, k_data.labels_, metric='euclidean', sample_size=sample_size),
    #         'completeness': metrics.completeness_score(data, k_data.labels_),
    #         'pca': PCA(n_components=2).fit_transform(data)}
    return kmeans

def k_means_data2(list_of_lists, cluster_number, label_markers, path):
    digits = np.array(list_of_lists)
    # data = scale(digits)
    data = digits
    label_dict = {}
    label_numbers = []
    n = 0
    label_dict[label_markers[0]] = 0
    for j in range(1, len(label_markers)):
        if label_markers[j] not in label_dict:
            label_dict[label_markers[j]] = n+1
            n += 1

    for i in label_markers:
        label_numbers.append(label_dict[i])
    n_samples, n_features = data.shape
    n_digits = cluster_number
    labels = np.array(label_numbers)
    # print('label numbers', label_numbers)
    # sample_size = 300

    sample_size = len(data)
    # print(sample_size, 'Sample Size')


    print("n_digits: %d, \t n_samples %d, \t n_features %d"
          % (n_digits, n_samples, n_features))

    print(55 * '_')
    print('% 4s' % 'init'' time inertia homo  compl v-meas ARI  AMI  silhouette')

    def bench_k_means(estimator, name, data):
        t0 = time()
        estimator.fit(data)
        print('% 4s %.2fs  %i %.3f %.3f %.3f %.3f %.3f  %.3f'
              % (name, (time() - t0), estimator.inertia_,
                 metrics.homogeneity_score(labels, estimator.labels_),
                 metrics.completeness_score(labels, estimator.labels_),
                 metrics.v_measure_score(labels, estimator.labels_),
                 metrics.adjusted_rand_score(labels, estimator.labels_),
                 metrics.adjusted_mutual_info_score(labels, estimator.labels_),
                 metrics.silhouette_score(data, estimator.labels_,
                                          metric='euclidean',
                                          sample_size=sample_size)))


    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10, precompute_distances=True, n_jobs=-1),
                  name="k++", data=data)

    bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10, precompute_distances=True, n_jobs=-1),
                  name="rand", data=data)

    # in this case the seeding of the centers is deterministic, hence we run the
    # kmeans algorithm only once with n_init=1
    pca = PCA(n_components=n_digits).fit(data)
    bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1, precompute_distances=True, n_jobs=-1),
                  name="PCA",
                  data=data)
    print(55 * '_')

    ###############################################################################
    # Visualize the results on PCA-reduced data

    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 2, reduced_data[:, 0].max() + 2
    y_min, y_max = reduced_data[:, 1].min() - 2, reduced_data[:, 1].max() + 2
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    # plt.set_size_inches(6, 4)
    plt.clf()
    # plt.imshow(Z, interpolation='nearest',
    #            extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    #            cmap=plt.cm.Paired,
    #            aspect='auto', origin='lower')
    centroids = kmeans.cluster_centers_

    for x, y, z in zip(reduced_data[:, 0], reduced_data[:, 1], label_markers):
        if z == '$Temperley MAJOR$' or z == '$M$':
            plt.plot(x, y, 'k.', marker='$M$', color='blue', markeredgecolor='none', markersize=30)
        elif z == '$Temperley MINOR$' or z == '$m$':
            plt.plot(x, y, 'k.', marker='$m$', color='blue', markeredgecolor='none', markersize=30)
        elif z[0] == '*':
            # plt.plot(x, y, 'k.', marker=z[1:], color='white', markeredgecolor='none', markersize=40)
            plt.plot(x, y, 'k.', marker='o', color='white', markeredgecolor='none', markersize=10)
    #     else:
    #         plt.plot(x, y, 'k.', marker=z, alpha=.3, markersize=len(z)*3)
            # plt.plot(x, y, 'k.', marker='.', alpha=.4)
    #     plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.')
        # plt.plot(x, y, 'k.')
    # for i, c in enumerate(centroids):
    #     cent_label = i+1
    #     plt.plot(c[0], c[1], marker='$%d$' % cent_label, color='w', markeredgecolor='b', markersize=30)
    # for x in alf_labels:
    #         plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', marker = x, markersize=5)
    #     print('reduced data:', reduced_data)
    # Plot the centroids as a white X

    # plt.scatter(centroids[:, 0], centroids[:, 1],
    #             marker='x', s=169, linewidths=3,
    #             color='w', zorder=10)
    # plt.title('PCA-reduced data\n'
    #           'Centroids are marked with white cross')
    n_clusters_ = cluster_number
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        col = 'k'
        class_members = kmeans.labels_ == k
        cluster_center =centroids[k]
        plt.plot(reduced_data[class_members, 0], reduced_data[class_members, 1], col + '.')

        for x in reduced_data[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], 'k', alpha=.5)
        plt.plot(cluster_center[0], cluster_center[1], 's', markerfacecolor='white',
                 markeredgecolor='black', markersize=18, alpha=.8)
        plt.plot(cluster_center[0], cluster_center[1], marker='$%d$' %(k+1), markerfacecolor='k',
                 markeredgecolor='k', markersize=15)

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.axis('off')
    plt.savefig(path, bbox_inches='tight')
    plt.show()
    plt.close()
    return kmeans

#for neato graphs (averages of key profiles)
def averaged_octave_harmonization(flattened_list_with_labels, label_function):
    averaged_chunks = []
    all_keys = []
    for x in flattened_list_with_labels[1]:
        if x not in all_keys:
            all_keys.append(x)
    for x in all_keys:
        a_key = []
        for a, b in zip(flattened_list_with_labels[0], flattened_list_with_labels[1]):
            if b == x:
                a_key.append(a)
        averaged_chunks.append([sum(col) / len(col) for col in zip(*a_key)])

    return averaged_chunks, all_keys

#do this for neato graphs then call neato_graph_whatever(neato_maker(whatever), labeled_nodes)
def neato_maker(lists_tuple):
    DIST = []
    for x in lists_tuple[0]:
        dist_temp = []
        for y in lists_tuple[0]:
            dist_temp.append(euclidean(x, y))
        DIST.append(dist_temp)
    return DIST, label_maker(lists_tuple[1])

#neato graph with temperley data
def neato_graph_FQ(list_of_lists, label_lists, path):
    dt = [('len', float)]

    A = (np.array(list_of_lists)).view(dt)
    G = nx.from_numpy_matrix(A)
    relabeled_nodes = {}
    for x, y in zip(range(len(label_lists)), label_lists):
        relabeled_nodes[x] = y[1:-1]
        # print(y[1:-1])
    G = nx.relabel_nodes(G, relabeled_nodes)

    G = to_agraph(G)

    G.node_attr.update(style='filled', fontsize=50)
    G.edge_attr.update(color='black', style='invis', width=0)
    #  ♭ ♮ ...for copy and paste

    modal_pairs = {'ionian': ('♮:C', '♭:F'), 'dorian': ('♭:G', '♮:D'), 'phrygian': ('♮:E', '♭:A'),
                   'lydian': ('♮:F', '♭:B♭'), 'mixolydian': ('♮:G', '♭:C'), 'aeolian': ('♮:A', '♭:D')}
    modal_pairs_reversed = {'ionian': ('♭:F', '♮:C'), 'dorian': ('♮:D', '♭:G'), 'phrygian': ('♭:A', '♮:E'),
                            'lydian': ('♭:B♭', '♮:F'), 'mixolydian': ('♭:C', '♮:G'), 'aeolian': ('♭:D', '♮:A')}
    major_modes = ('♮:C', '♭:F', '♮:F', '♭:B♭', '♮:G', '♭:C',
                   'CM', 'GM', 'DM', 'AM', 'EM', 'BM', 'F♯M', 'FM', 'B♭M', 'E♭M', 'A♭M', 'D♭M', 'G♭M')
    minor_modes = ('♭:G', '♮:D', '♮:E', '♭:A', '♮:A', '♭:D',
                   'am', 'em', 'bm', 'f♯m', 'c♯m', 'g♯m', 'd♯m', 'dm', 'gm', 'cm', 'fm', 'b♭m', 'e♭m')
    temp_letters = ('M', 'm')
    for a in modal_pairs.values():
        if a in G.edges():
            b = G.get_edge(a[0], a[1])
            b.attr['penwidth'] = 15
            b.attr['style'] = 'bold'

    for a in modal_pairs_reversed.values():
        if a in G.edges():
            b = G.get_edge(a[0], a[1])
            b.attr['penwidth'] = 15
            b.attr['style'] = 'bold'

    for x in major_modes:
        if x in G.nodes():
            if 'M' in G.nodes():
                b = G.get_edge('M', x)
                b.attr['color'] = 'blue'
                b.attr['penwidth'] = 5
                b.attr['style'] = 'dashed'
    for x in minor_modes:
        if x in G.nodes():
            if 'm' in G.nodes():
                b = G.get_edge('m', x)
                b.attr['color'] = 'green'
                b.attr['penwidth'] = 5
                b.attr['style'] = 'dashed'
    for node in G.nodes():
        #         print(node)
        if node not in modal_pairs.values() and node not in major_modes and \
                        node not in minor_modes and node not in temp_letters:
            G.remove_node(node)
            print('removed:', node)
    if 'M' in G.nodes():
        M = G.get_node('M')

        M.attr['shape'] = 'square'
        M.attr['fontsize'] = 100
    if 'm' in G.nodes():
        m = G.get_node('m')

        m.attr['shape'] = 'square'
        m.attr['fontsize'] = 100
    G.draw(path, format='pdf', prog='neato')

def function_thing(csv_making_function, data_type):
    numeral_data = []
    numeral_ave = []
    numeral_labels = []
    bi = csv_making_function
    for x in bi[1:]:
        numeral_data.append(x[1:])
        if data_type == 'numerals':
            numeral_labels.append(x[0])
        else:
            labs = 0
            for a, b in numerals_to_data.items():
                if x[0] == str(b):
                    numeral_labels.append(a)
                    labs += 1
            if labs == 0:
                print('missing:', x[0])
            elif labs > 1:
                print('duplicate:', x[0])
    for x in numeral_data:
        numeral_ave.append([100 * (y/sum(x)) for y in x])
    return numeral_data, numeral_labels, numeral_ave

def neato_plain(list_of_lists, label_lists, path):
    dt = [('len', float)]

    A = (np.array(list_of_lists)/10).view(dt)
    # print(A)
    G = nx.from_numpy_matrix(A)
    relabeled_nodes = {}
    for x, y in zip(range(len(label_lists)), label_lists):
        relabeled_nodes[x] = y[1:-1]
        # print(y[1:-1])
    G = nx.relabel_nodes(G, relabeled_nodes)

    G = to_agraph(G)

    G.node_attr.update(style='filled', fontsize=20)
    G.edge_attr.update(color='black', style='invis')
    #  ♭ ♮ ...for copy and paste

    G.draw(path, format='pdf', prog='neato')

#neato graph for comparing all corpora
def neato_graph_big(list_of_lists, label_lists, path):
    dt = [('len', float)]

    A = (np.array(list_of_lists)).view(dt)

    G = nx.from_numpy_matrix(A)
    relabeled_nodes = {}
    for x, y in zip(range(len(label_lists)), label_lists):
        relabeled_nodes[x] = y[1:-1]
        print(y[1:-1])
    G = nx.relabel_nodes(G, relabeled_nodes)

    G = to_agraph(G)

    G.node_attr.update(style='filled', fontsize=50)
    #     G.edge_attr.update(color="black", width=0.5)
    G.edge_attr.update(color='black', style='invis', width=0)
    # G.graph_attr.update(landscape='true', ranksep='0.1')
    #  ♭ ♮ ...for copy and paste

    modal_pairs = {'ionian': ('♮:C', '♭:F'), 'dorian': ('♭:G', '♮:D'), 'phrygian': ('♮:E', '♭:A'),
                   'lydian': ('♮:F', '♭:B♭'), 'mixolydian': ('♮:G', '♭:C'), 'aeolian': ('♮:A', '♭:D')}
    modal_pairs_reversed = {'ionian': ('♭:F', '♮:C'), 'dorian': ('♮:D', '♭:G'), 'phrygian': ('♭:A', '♮:E'),
                            'lydian': ('♭:B♭', '♮:F'), 'mixolydian': ('♭:C', '♮:G'), 'aeolian': ('♭:D', '♮:A')}
    major_modes = ('♮:C', '♭:F', '♮:F', '♭:B♭', '♮:G', '♭:C',
                   'CM', 'GM', 'DM', 'AM', 'EM', 'BM', 'F♯M', 'FM', 'B♭M', 'E♭M', 'A♭M', 'D♭M', 'G♭M')
    minor_modes = ('♭:G', '♮:D', '♮:E', '♭:A', '♮:A', '♭:D',
                   'am', 'em', 'bm', 'f♯m', 'c♯m', 'g♯m', 'd♯m', 'dm', 'gm', 'cm', 'fm', 'b♭m', 'e♭m')
    temp_letters = ('M', 'm')
    tonal_keys = {}
    for a in modal_pairs.values():
        for x in G.edges():
            #             print('edge', x)
            if (x[0][2:], x[1][2:]) == a or x == a:
                b = x
                b.attr['penwidth'] = 15
                b.attr['style'] = 'bold'

    for a in modal_pairs_reversed.values():
        for x in G.edges():
            if (x[0][2:], x[1][2:]) == a or x == a:
                b = x
                b.attr['penwidth'] = 15
                b.attr['style'] = 'bold'

    for a in major_modes:
        for x in G.nodes():
            if x[2:] == a or x == a:
                print('yes, major')
                if 'M' in G.nodes():
                    b = G.get_edge('M', x)
                    b.attr['color'] = 'blue'
                    b.attr['penwidth'] = 5
                    b.attr['style'] = 'dashed'
    for a in minor_modes:
        for x in G.nodes():
            if x[2:] == a or x == a:
                print('yes, minor')
                if 'm' in G.nodes():
                    b = G.get_edge('m', x)
                    b.attr['color'] = 'green'
                    b.attr['penwidth'] = 5
                    b.attr['style'] = 'dashed'
    for node in G.nodes():
        #         print(node)
        if node[2:] not in modal_pairs.values() and node[2:] not in major_modes and \
                        node[2:] not in minor_modes and node not in temp_letters:
            G.remove_node(node)
            print('removed:', node)
    if 'M' in G.nodes():
        M = G.get_node('M')
        M.attr['shape'] = 'square'
        M.attr['fontsize'] = 100
    if 'm' in G.nodes():
        m = G.get_node('m')
        m.attr['shape'] = 'square'
        m.attr['fontsize'] = 100
    G.draw(path, format='pdf', prog='neato')

#returns silhouette, completeness and PCA data for plotting
def k_means_simple(list_of_lists, cluster_number, label_markers):

    data = np.array(list_of_lists)
    label_dict = {}
    label_numbers = []
    n = 0
    label_dict[label_markers[0]] = 0
    for j in range(1, len(label_markers)):
        if label_markers[j] not in label_dict:
            label_dict[label_markers[j]] = n+1
            n += 1

    for i in label_markers:
        label_numbers.append(label_dict[i])
    n_samples, n_features = data.shape
    n_digits = cluster_number
    labels = np.array(label_numbers)
    # print('label numbers', label_numbers)
    # sample_size = 300

    sample_size = len(data)

    k_data = KMeans(init='k-means++', n_clusters=n_digits, n_init=10, precompute_distances=True, n_jobs=-1).fit(data)
    silhouette = metrics.silhouette_score(data, k_data.labels_, metric='euclidean', sample_size=sample_size)
    completeness = metrics.completeness_score(labels, k_data.labels_)
    #pca = PCA(n_components=2)
    #pca.fit_transform(data)
#     pca = PCA(n_components=2).fit(data).score(data)
    return {'silhouette': silhouette, 'completeness': completeness, 'kmeans': k_data}

#plots silhouette and completeness scores and saves them to a path (use PDF)
def fitness_plotter(corpus, corpus_labels, max_cluster, path):
    silhouette_data = []
    completeness_data = []
    X = [x for x in range(2, max_cluster+1)]
    for x in range(2, max_cluster+1):
        temp = k_means_simple(corpus, x, corpus_labels)
        silhouette_data.append(temp['silhouette'])
        completeness_data.append(temp['completeness'])
    plt.ylim([0, 1.1])
    plt.xlim([1, 13])
    plt.plot(X, completeness_data, color='blue', linestyle='-', marker='o', label='completeness score')

    plt.plot(X, silhouette_data, color='green', linestyle='-', marker='o', label='silhouette score')
    plt.title('Silhouette and Completeness Scores for 2–12 Modes', fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    legend.get_frame().set_facecolor('#00FFCC')
    plt.xlabel('number of clusters (modes)', fontsize=14)
    plt.ylabel('score', fontsize=14)
    
    plt.grid(True)
    plt.savefig(path, bbox_inches='tight')
    plt.show()
    # plt.close()
def fitness_plotter_big(corpus, corpus_labels, max_cluster, path):
    silhouette_data = []
    completeness_data = []
    X = [x for x in range(2, max_cluster+1)]
    for x in range(2, max_cluster+1):
        temp = k_means_simple(corpus, x, corpus_labels)
        silhouette_data.append(temp['silhouette'])
        completeness_data.append(temp['completeness'])
    plt.ylim([0, 1.1])
    plt.xlim([1, 13])
    plt.plot(X, completeness_data, color='blue', linestyle='-', marker='o', label='completeness score')

    plt.plot(X, silhouette_data, color='green', linestyle='-', marker='o', label='silhouette score')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    legend.get_frame().set_facecolor('#00FFCC')
    plt.xlabel('number of clusters (modes)', fontsize=24)
    plt.ylabel('score', fontsize=24)
    
    plt.grid(True)
    plt.savefig(path, bbox_inches='tight')
    plt.show()

# def ngram_to_numeral(data, mode, ngram, numeral, progression_element, tab):
#     # G = nx.OrderedMultiDiGraph()
#     all_numbers = []
#     corpus_data = markov.markovMaker(data, mode, ngram, progression_element, tab)
#     G = nx.DiGraph()
#     if ngram == 2:
#         for x in corpus_data:
#             for y, z in corpus_data[x].items():
#                 if y == numeral or numeral == 'all':
#                     all_numbers.append([x, y, z])
#                     if y in G.edges():
#                         old_percent = (G[x][y]['weight'])
#                         new_percent = corpus_data[x][y] / corpus_percentage(corpus_data) * 100
#                         G.add_path([x, y], weight=(old_percent + new_percent), penwidth=(old_percent + new_percent))
#                     else:
#                         G.add_path([x, y], weight=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100),
#                                    penwidth=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100))
#
#     elif ngram == 3:
#         for a, b in corpus_data.keys():
#             for x, y in corpus_data[(a, b)].items():
#                 temp = [a, b]
#                 temp2 = []
#                 if x == numeral or numeral == 'all':
#                     temp2.append(' '.join(temp))
#                     temp2.append(x)
#                     temp2.append(y)
#                     all_numbers.append(temp2)
#         for x in all_numbers:
#             if x[0] in G.edges() and x[1] in G.edges():
#                 old_percent = (G[x[0]][x[1]]['weight'])
#                 new_percent = x[-1] / corpus_percentage(corpus_data) * 100
#                 G.add_path(x[:-1], weight=(old_percent + new_percent))
#             else:
#                 G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
#
#     elif ngram == 4:
#         for a, b, c in corpus_data.keys():
#             for x, y in corpus_data[(a, b, c)].items():
#                 temp = [a, b, c]
#                 temp2 = []
#                 if x == numeral or numeral == 'all':
#                     temp2.append(' '.join(temp))
#                     temp2.append(x)
#                     temp2.append(y)
#                     all_numbers.append(temp2)
#         for x in all_numbers:
#             if x[0] in G.edges() and x[1] in G.edges():
#                 old_percent = (G[x[0]][x[1]]['weight'])
#                 new_percent = x[-1] / corpus_percentage(corpus_data) * 100
#                 G.add_path(x[:-1], weight=(old_percent + new_percent))
#             else:
#                 G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
#
#     elif ngram == 5:
#         for a, b, c, d in corpus_data.keys():
#             for x, y in corpus_data[(a, b, c, d)].items():
#                 temp = [a, b, c, d]
#                 temp2 = []
#                 if x == numeral or numeral == 'all':
#                     temp2.append(' '.join(temp))
#                     temp2.append(x)
#                     temp2.append(y)
#                     all_numbers.append(temp2)
#         for x in all_numbers:
#             if x[0] in G.edges() and x[1] in G.edges():
#                 old_percent = (G[x[0]][x[1]]['weight'])
#                 new_percent = x[-1] / corpus_percentage(corpus_data) * 100
#                 G.add_path(x[:-1], weight=(old_percent + new_percent))
#             else:
#                 G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
#
#     elif ngram == 6:
#         for a, b, c, d, e in corpus_data.keys():
#             for x, y in corpus_data[(a, b, c, d, e)].items():
#                 temp = [a, b, c, d, e]
#                 temp2 = []
#                 if x == numeral or numeral == 'all':
#                     temp2.append(' '.join(temp))
#                     temp2.append(x)
#                     temp2.append(y)
#                     all_numbers.append(temp2)
#         for x in all_numbers:
#             if x[0] in G.edges() and x[1] in G.edges():
#                 old_percent = (G[x[0]][x[1]]['weight'])
#                 new_percent = x[-1] / corpus_percentage(corpus_data) * 100
#                 G.add_path(x[:-1], weight=(old_percent + new_percent))
#             else:
#                 G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
#
#     elif ngram == 7:
#         for a, b, c, d, e, f in corpus_data.keys():
#             for x, y in corpus_data[(a, b, c, d, e, f)].items():
#                 temp = [a, b, c, d, e, f]
#                 temp2 = []
#                 if x == numeral or numeral == 'all':
#                     temp2.append(' '.join(temp))
#                     temp2.append(x)
#                     temp2.append(y)
#                     all_numbers.append(temp2)
#         for x in all_numbers:
#             if x[0] in G.edges() and x[1] in G.edges():
#                 old_percent = (G[x[0]][x[1]]['weight'])
#                 new_percent = x[-1] / corpus_percentage(corpus_data) * 100
#                 G.add_path(x[:-1], weight=(old_percent + new_percent))
#             else:
#                 G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
#     # print(all_numbers)
#     nodes = G.nodes(data=True)
#     node_colors = []
#     for x in all_numbers:
#         G.add_node(x[0], weight=x[-1], category='ant')
#         G.add_node(x[1], weight=5, category='con')
#     for x in nodes:
#         if x[1]['category'] == 'ant':
#             node_colors.append('cyan')
#         else:
#             node_colors.append('green')
#     # color_map = {'ant': 'blue', 'con': 'yellow'}
#     # print(d)
#     # print(G.nodes(data=True))
#     edges = G.edges(data=True)
#     edge_weights = []
#     for x in edges:
#         edge_weights.append(x[2]['weight'])
#         # print(x[2])
#     node_weights = []
#     for x in nodes:
#         if 'weight' in x[1]:
#             # print(x[1])
#             node_weights.append((x[1]['weight'] * 200))
#         else:
#             node_weights.append(0)
#     # print(node_weights)
#     # pos = nx.circular_layout(G, scale=5)
#     pos = nx.spring_layout(G)
#     nx.draw_networkx_edges(G, pos, edges=edges, edge_color='black', width=edge_weights, alpha=1)
#     nx.draw_networkx_nodes(G, pos, node_color=node_colors, alpha=1, linewidths=0, node_size=node_weights)
#     # nx.draw_networkx_nodes(G, pos, node_color=[color_map[G.node[node]['category']] for node in G], alpha=.6, linewidths=0, node_size=0)
#     nx.draw_networkx_labels(G, pos, font_size=18, font_family='serif')
#     write_dot(G, '/home/daniel/Desktop/blobs.dot')
#     # print(G.nodes(data=True)[1][1])
#     # # plt.grid(True)
#     plt.axis('off')
#     # plt.savefig('/home/daniel/Desktop/kapsperger_v1.png', dpi=300, bbox_inches='tight')
#     # plt.close(plt)
#     plt.show()


bach_continuo = corpus_chord_data(bach_continuo_data)
josquin_continuo = corpus_chord_data(josquin_continuo_data)
barbershop_continuo_data = joblib.load('pickles/barbershop.pkl')
monteverdi_continuo = corpus_chord_data(monteverdi_continuo_data)
barbershop_continuo = corpus_chord_data(barbershop_continuo_data)
zma = joblib.load('pickles/Zma_continuo.pkl')
zmo = joblib.load('pickles/Zmo_continuo.pkl')
zso = joblib.load('pickles/Zso_continuo.pkl')
# haydn_continuo = corpus_chord_data(haydn_continuo_data)
# mozart_continuo = corpus_chord_data(mozart_continuo_data)
# bach_continuo_function_major = bigram_numbers_corpus(bach_continuo, tonal_major)
# alfabeto_continuo_function_major = bigram_numbers_continuo(GetAll.all_alf, modal_major)
# alfabeto_continuo_function_minor = bigram_numbers_continuo(GetAll.all_alf, modal_minor)
# alfabeto_chord_function_major = bigram_numbers_alfabeto(GetAll.all_alf, modal_major)
# alfabeto_chord_function_minor = bigram_numbers_alfabeto(GetAll.all_alf, modal_minor)
# alfabeto_root_major = bigram_numbers_roots(alfabeto_roots, modal_major)
# alfabeto_root_minor = bigram_numbers_roots(alfabeto_roots, modal_minor)
palestrina_continuo = corpus_chord_data(palestrina_continuo_data)
zma_continuo = corpus_chord_data(zma)
zmo_continuo = corpus_chord_data(zmo)
zso_continuo = corpus_chord_data(zso)

# palestrina_continuo_function_major = bigram_numbers_corpus(palestrina_continuo, [(0, 0), (-1, 5)])

if __name__ == '__main__':
    # #variables for continuo or chord only alfabeto
    # alfabeto_continuo_function_major = bigram_numbers_continuo(GetAll.all_alf, modal_major)
    # alfabeto_continuo_function_minor = bigram_numbers_continuo(GetAll.all_alf, modal_minor)
    # alfabeto_chord_function_major = bigram_numbers_alfabeto(GetAll.all_alf, modal_major)
    # alfabeto_chord_function_minor = bigram_numbers_alfabeto(GetAll.all_alf, modal_minor)
    #
    # #variables for palestrina and bach chords
    # palestrina_chord_function_major = bigram_numbers_corpus(palestrina_chords_data, tonal_major)
    # palestrina_chord_function_minor = bigram_numbers_corpus(palestrina_chords_data, tonal_minor)
    # bach_chord_function_major = bigram_numbers_corpus(bach_chords_data, tonal_major)
    # bach_chord_function_minor = bigram_numbers_corpus(bach_chords_data, tonal_minor)
    bach_continuo = corpus_chord_data(bach_continuo_data)
    palestrina_continuo = corpus_chord_data(bach_continuo_data)
    zma_continuo = corpus_chord_data(zma_continuo_data)
    zmo_continuo = corpus_chord_data(zmo_continuo_data)
    zso_continuo = corpus_chord_data(zso_continuo_data)
    # bach_continuo_function_minor = bigram_numbers_corpus(bach_continuo, tonal_minor)
    # palestrina_continuo = corpus_chord_data(palestrina_continuo_data)
    # palestrina_continuo_function_major = bigram_numbers_corpus(palestrina_continuo, [(0, 0), (-1, 5)])
    # palestrina_continuo_function_minor = bigram_numbers_corpus(palestrina_continuo, [(0, 9), (-1, 2)])
    ##function for CSV file (information bottleneck)
    def csv_function(f_variable, path):
        with open(path, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(f_variable)

    # k_means_data(alf_kmeans_data[0], 2, label_maker_alfabeto(alf_kmeans_data[1]),
    #              '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/alfabeto_freq_2.pdf')
    # k_means_data(pal_kmeans_data[0], 5, label_maker_alfabeto(pal_kmeans_data[1]),
    #              '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/palestrina_freq_5.pdf')
    # k_means_data(bach_kmeans_data[0], 2, label_maker(bach_kmeans_data[1]),
    #              '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/bach_freq_2.pdf')
    #
    # fitness_plotter(palestrina_notes_data[0], label_maker_alfabeto(palestrina_notes_data[1]), 12,
    # fitness_plotter(palestrina_notes_data[0], label_maker_alfabeto(palestrina_notes_data[1]), 12,
    #                 '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/palestrina_score.pdf')
    # fitness_plotter(alfabeto_notes_data[0], label_maker_alfabeto(alfabeto_notes_data[1]), 12,
    #                 '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/alfabeto_score.pdf')
    # fitness_plotter(bach_notes_data[0], label_maker(bach_notes_data[1]), 12,
    #                 '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/bach_score.pdf')

    # ave_alf = averaged_octave_harmonization(alf_kmeans_data, label_maker_alfabeto)
    # ave_pal = averaged_octave_harmonization(pal_kmeans_data, label_maker_alfabeto)
    # ave_bach = averaged_octave_harmonization(bach_kmeans_data, label_maker)

    # ave_alf_labeled = averaged_octave_harmonization(alf_kmeans_data, label_maker_alfabeto_labeled)
    # ave_pal_labeled = averaged_octave_harmonization(pal_kmeans_data, label_maker_pal)
    # ave_bach_labeled = averaged_octave_harmonization(bach_kmeans_data, label_maker_bach)
    # all_ave = copy.deepcopy(ave_alf_labeled)
    # for x, y in zip(ave_pal_labeled[0], ave_pal_labeled[1]):
    #     all_ave[0].append(x)
    #     all_ave[1].append(y)
    # for x, y in zip(ave_bach_labeled[0], ave_bach_labeled[1]):
    #     all_ave[0].append(x)
    #     all_ave[1].append(y)
    # neato_graph_FQ(neato_maker(ave_alf)[0], ave_alf[1],
    #                '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/alfabeto_freq_neato.pdf')
    # print('done alf')
    # neato_graph_FQ(neato_maker(ave_pal)[0], ave_pal[1],
    #                '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/palestrina_freq_neato.pdf')
    # print('done pal')
    # neato_graph_FQ(neato_maker(ave_bach)[0], ave_bach[1],
    #                '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/bach_freq_neato.pdf')
    # print('done bach')
    # neato_graph_big(neato_maker(all_ave)[0], all_ave[1],
    #                 '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/all_freq_neato.pdf')


    '''Continuo Stuff'''
    def bach_continuo_neato_grapher(path):
        bach = inversion_kmeans_corpus(bach_continuo_data, 'all', 'tonal', label_maker)
        bachave = averaged_octave_harmonization(bach, label_maker)
        bachX = neato_maker(bachave)
        neato_graph_FQ(bachX[0], bachave[1], path)


    def alfabeto_continuo_neato_grapher(path):
        alfabeto = inversion_kmeans(GetAll.all_alf, 'all', label_maker_alfabeto)
        alfabetoave = averaged_octave_harmonization(alfabeto, label_maker)
        alfabetoX = neato_maker(alfabetoave)
        neato_graph_FQ(alfabetoX[0], alfabetoave[1], path)


    def palestrina_continuo_neato_grapher(path):
        palestrina = inversion_kmeans_corpus(palestrina_continuo_data, 'all', 'modal', label_maker_alfabeto)
        palestrinaave = averaged_octave_harmonization(palestrina, label_maker)
        palestrinaX = neato_maker(palestrinaave)
        neato_graph_FQ(palestrinaX[0], palestrinaave[1], path)

    def all_three_neato(path):
        alf_cont = inversion_kmeans(GetAll.all_alf, 'all', label_maker_alfabeto_labeled)
        alf_labeled = averaged_octave_harmonization(alf_cont, label_maker)
        palestrina = inversion_kmeans_corpus(palestrina_continuo_data, 'all', 'modal', label_maker_pal)
        palestrinaave = averaged_octave_harmonization(palestrina, label_maker)
        bach = inversion_kmeans_corpus(bach_continuo_data, 'all', 'tonal', label_maker_bach)
        bachave = averaged_octave_harmonization(bach, label_maker)
        all_chords = []
        all_labels = []
        for a, b in zip(alf_labeled[0], alf_labeled[1]):
            all_chords.append(a)
            all_labels.append(b)
        for a, b in zip(palestrinaave[0], palestrinaave[1]):
            all_chords.append(a)
            all_labels.append(b)
        for a, b in zip(bachave[0], bachave[1]):
            all_chords.append(a)
            all_labels.append(b)
        allX = neato_maker((all_chords, all_labels))
        print(len(allX[0]))
        print(len(all_labels))
        neato_graph_big(allX[0], all_labels, path)
        return all_chords, all_labels, allX
# lun = liber_usalis_notes_data
# fitness_plotter(alfabeto_notes_data[0], label_maker_alfabeto(alfabeto_notes_data[1]), 12, '/home/daniel/Dropbox/Dissertation/Latex/figures/kmeans/liber_score.pdf')
# fitness_plotter(alfabeto_notes_data[0], label_maker_alfabeto(alfabeto_notes_data[1]), 12, '/home/daniel/Desktop/alf_score.pdf')

print('ready!')