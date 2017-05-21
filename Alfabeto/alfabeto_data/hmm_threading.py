import threading
from multiprocessing import Process
from queue import Queue
import time, os

import numpy as np
from hmmlearn import hmm
import alfabeto_data.dissertation_images as di
from alfabeto_data.harmonic_function_data import ordered_numeral_list
from alfabeto_sources.all_sources import *
from alfabeto_sources import *
from alfabeto_code.AlfabetoConverter import transposed_pc_chords_noMMD
from Continuo.ContinuoConverter import figure_intervals_pc
import csv
import copy

from sklearn.externals import joblib
import pickle
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, to_agraph
from scipy.spatial.distance import euclidean


'''~/pickles/hmm/corpus/mode/K'''
'''train, test, fit, total chords'''


def hmm_pickle_generator(data_type, corpus, mode_list, corpus_name, mode_name, MC, K, RANGE, start_path):
    shuffle_path = start_path+'hmm_mc/%s/%s/%s/%s' % (corpus_name, mode_name, K, MC)
    if not os.path.exists(shuffle_path):
        os.makedirs(shuffle_path)

    if os.path.exists(start_path+'hmm_mc/%s/%s/%s/%sMC.pkl' % (corpus_name, mode_name, K, MC)):
        print('already MC there')
        MC_data = joblib.load(start_path+'hmm_mc/%s/%s/%s/%sMC.pkl' % (corpus_name, mode_name, K, MC))
        X = MC_data['X']
        X_train = MC_data['X_train']
        X_test = MC_data['X_test']
        HH = 'yes'
    else:
        HH = 'no'
        if data_type == 'alfabeto continuo':
            all_songs = []
            for book in di.GetAll.all_alf:
                for numb, song in book.items():
                    if (song['data']['key'], song['data']['final']) in mode_list:
                        all_songs.append({numb:song})
            np.random.shuffle(all_songs)
            X = di.python_hmm(all_songs, mode_list, 'continuo')
            train_percent = int(len(X[1])/5)
            X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'continuo')
            X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'continuo')
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)
        elif data_type == 'alfabeto chords':
            all_songs = []
            for book in di.GetAll.all_alf:
                for numb, song in book.items():
                    if (song['data']['key'], song['data']['final']) in mode_list:
                        all_songs.append({numb:song})
            np.random.shuffle(all_songs)
            X = di.python_hmm(all_songs, mode_list, 'chords')
            train_percent = int(len(X[1])/5)
            X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'chords')
            X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'chords')
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)
        else:
            corpus_lengths = [x for x in range(len(corpus[0]))]
            np.random.shuffle(corpus_lengths)
            mc_corpus = ([corpus[0][x] for x in corpus_lengths], [corpus[1][x] for x in corpus_lengths])
            X = di.python_hmm_corpus(mc_corpus, mode_list)
            train_percent = int(len(X[1]) / 5)
            X_train = di.python_hmm_corpus((mc_corpus[0][train_percent:], mc_corpus[1][train_percent:]), mode_list)
            X_test_temp = di.python_hmm_corpus((mc_corpus[0][:train_percent], mc_corpus[1][:train_percent]), mode_list)
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)

    Z = hmm.MultinomialHMM(n_components=K, verbose=False, n_iter=500, tol=.01)
    pickle_path = start_path+'hmm_mc/%s/%s/%s/%s' % (corpus_name, mode_name, K, MC)
    #pickle_path = 'pickles/hmm/%s/%s/%s' % (corpus_name, mode_name, K)
    if not os.path.exists(pickle_path):
        os.makedirs(pickle_path)

    for worker in RANGE:
        print(HH)
        path = pickle_path+'/%s.pkl' % worker
        if not os.path.exists(path):
            print('starting!', K, worker)
            s_time = time.time()
            Y = copy.deepcopy(Z)
            Y.n_features = len(X[2])
            a = Y.fit(X_train[0], X_train[1])
            c = a.decode(X_test[0], lengths=X_test[1], algorithm='viterbi')
            dict_data = {'train': X_train, 'test': X_test, 'fit': a, 'decode': c, 'total_chords': len(X[2])}
            e_time = time.time() - s_time
            print('K=%s number %s done in %s seconds' % (K, worker, e_time))
            joblib.dump(dict_data, path, compress=True)
        else:
            print(K, worker, 'already exists... :)')


def hmm_randomizer(data_type, corpus, mode_list, corpus_name, mode_name, MC, K, RANGE, start_path):
    shuffle_path = start_path+'hmm_mc/%s/%s/%s/%s' % (corpus_name, mode_name, K, MC)
    if not os.path.exists(shuffle_path):
        os.makedirs(shuffle_path)

    if os.path.exists(start_path+'hmm_mc/%s/%s/%s/%sMC.pkl' % (corpus_name, mode_name, K, MC)):
        print('already MC there')
        MC_data = joblib.load(start_path+'hmm_mc/%s/%s/%s/%sMC.pkl' % (corpus_name, mode_name, K, MC))
        X = MC_data['X']
        X_train = MC_data['X_train']
        X_test = MC_data['X_test']
        HH = 'yes'
    else:
        HH = 'no'
        if data_type == 'alfabeto continuo':
            all_songs = []
            for book in di.GetAll.all_alf:
                for numb, song in book.items():
                    if (song['data']['key'], song['data']['final']) in mode_list:
                        all_songs.append({numb:song})
            np.random.shuffle(all_songs)
            X = di.python_hmm(all_songs, mode_list, 'continuo')
            train_percent = int(len(X[1])/5)
            X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'continuo')
            X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'continuo')
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)
        elif data_type == 'alfabeto chords':
            all_songs = []
            for book in di.GetAll.all_alf:
                for numb, song in book.items():
                    if (song['data']['key'], song['data']['final']) in mode_list:
                        all_songs.append({numb:song})
            np.random.shuffle(all_songs)
            X = di.python_hmm(all_songs, mode_list, 'chords')
            train_percent = int(len(X[1])/5)
            X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'chords')
            X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'chords')
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)
        else:
            corpus_lengths = [x for x in range(len(corpus[0]))]
            np.random.shuffle(corpus_lengths)
            mc_corpus = ([corpus[0][x] for x in corpus_lengths], [corpus[1][x] for x in corpus_lengths])
            X = di.python_hmm_corpus(mc_corpus, mode_list)
            train_percent = int(len(X[1]) / 5)
            X_train = di.python_hmm_corpus((mc_corpus[0][train_percent:], mc_corpus[1][train_percent:]), mode_list)
            X_test_temp = di.python_hmm_corpus((mc_corpus[0][:train_percent], mc_corpus[1][:train_percent]), mode_list)
            decode_data = []
            for x in X_test_temp[0]:
                main_label = X[2].index(X_test_temp[2][x[0]])
                decode_data.append([main_label])
            X_test = (decode_data, X_test_temp[1])
            pickle_data = {'X': X, 'X_train': X_train, 'X_test': X_test}
            joblib.dump(pickle_data, shuffle_path + 'MC.pkl', compress=True)

def hmm_pickle_generator_2(data_type, corpus, mode_list, corpus_name, mode_name, K, RANGE):
    X = 0
    X_train = 0
    X_test = 0
    if data_type == 'alfabeto continuo':
        all_songs = []
        for book in di.GetAll.all_alf:
            for numb, song in book.items():
                if (song['data']['key'], song['data']['final']) in mode_list:
                    all_songs.append({numb:song})
        X = di.python_hmm(all_songs, mode_list, 'continuo')
        train_percent = int(len(X[1])/5)
        X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'continuo')
        X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'continuo')
        decode_data = []
        for x in X_test_temp[0]:
            main_label = X[2].index(X_test_temp[2][x[0]])
            decode_data.append([main_label])
        X_test = (decode_data, X_test_temp[1])
    elif data_type == 'alfabeto chords':
        all_songs = []
        for book in di.GetAll.all_alf:
            for numb, song in book.items():
                if (song['data']['key'], song['data']['final']) in mode_list:
                    all_songs.append({numb:song})
        X = di.python_hmm(all_songs, mode_list, 'chords')
        train_percent = int(len(X[1])/5)
        X_train = di.python_hmm(all_songs[train_percent:], mode_list, 'chords')
        X_test_temp = di.python_hmm(all_songs[:train_percent], mode_list, 'chords')
        decode_data = []
        for x in X_test_temp[0]:
            main_label = X[2].index(X_test_temp[2][x[0]])
            decode_data.append([main_label])
        X_test = (decode_data, X_test_temp[1])
    else:

        X = di.python_hmm_corpus(corpus, mode_list)
        train_percent = int(len(X[1]) / 5)
        X_train = di.python_hmm_corpus((corpus[0][train_percent:], corpus[1][train_percent:]), mode_list)
        X_test_temp = di.python_hmm_corpus((corpus[0][:train_percent], corpus[1][:train_percent]), mode_list)
        decode_data = []
        for x in X_test_temp[0]:
            main_label = X[2].index(X_test_temp[2][x[0]])
            decode_data.append([main_label])
        X_test = (decode_data, X_test_temp[1])

    Z = hmm.MultinomialHMM(n_components=K, verbose=False, n_iter=500, tol=.01)
    print_lock = threading.Lock()
    pickle_path = '/home/daniel/Desktop/hmm/%s/%s/%s' % (corpus_name, mode_name, K)
    #pickle_path = 'pickles/hmm/%s/%s/%s' % (corpus_name, mode_name, K)
    if not os.path.exists(pickle_path):
        os.makedirs(pickle_path)

    for worker in RANGE:
        path = pickle_path+'/%s.pkl' % worker
        if not os.path.exists(path):
            print('starting!', K, worker)
            s_time = time.time()
            Y = copy.deepcopy(Z)
            Y.n_features = len(X[2])
            a = Y.fit(X_train[0], X_train[1])
            c = a.decode(X_test[0], lengths=X_test[1], algorithm='viterbi')
            dict_data = {'train': X_train, 'test': X_test, 'fit': a, 'decode': c, 'total_chords': len(X[2])}
            e_time = time.time() - s_time
            print('K=%s number %s done in %s seconds' % (K, worker, e_time))
            joblib.dump(dict_data, path)
        else:
            print(K, worker, 'already exists... :)')






# if __name__ == '__main__':
#     # --- data_type, corpus, mode_list, corpus_name, mode_name
#     hmm_pickle_generator2('corpus', di.bach_continuo, di.tonal_major, 'bach', 'major')
#     hmm_pickle_generator2('corpus', di.bach_continuo, di.tonal_minor, 'bach', 'minor')
#
#     hmm_pickle_generator2('corpus', di.palestrina_continuo, [(0, 0), (-1, 5)], 'palestrina', 'major')
#     hmm_pickle_generator2('corpus', di.palestrina_continuo, [(0, 9), (-1, 2)], ' palestrina', 'minor')
#
#     hmm_pickle_generator2('alfabeto continuo', di.GetAll.all_alf, di.modal_major, 'alfabeto_continuo', 'major')
#     hmm_pickle_generator2('alfabeto continuo', di.GetAll.all_alf, di.modal_minor, 'alfabeto_continuo', 'minor')
#
#     hmm_pickle_generator2('alfabeto chords', di.GetAll.all_alf, di.modal_major, 'alfabeto_continuo', 'major')
#     hmm_pickle_generator2('alfabeto chords', di.GetAll.all_alf, di.modal_minor, 'alfabeto_continuo', 'minor')
