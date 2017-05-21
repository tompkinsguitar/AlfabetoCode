from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import sklearn.preprocessing as sklp

from music21 import *
from Continuo import ContinuoMarkov as CM
from alfabeto_sources import all_sources
from alfabeto_data.AlfabetoStats.Bach_Choral_Chords import bach_note_counter, corpus_note_counter
from scipy.spatial.distance import euclidean
from alfabeto_data.AlfabetoStats.stats import book_data, all_kaps
# from alfabeto_data.pickled_data import alfabeto_notes_final

''' -----only for corpus-------------------'''
# final_notes_bach = bach_note_counter()
# final_notes_corpus = corpus_note_counter(corpus.getComposer('palestrina'))
# corpus_labels = []
#
# # for x in range(len(final_notes_corpus)):
# #     corpus_labels.append('0')
# corpus_labels.append('Temperley MAJOR')
# corpus_labels.append('Temperley MINOR')
''' --------------------------------------'''

'''kaps chords------------------------------'''
def corpus_converter(corpus_list):
    final_list = []
    final_notes_list = []
    final_final = []
    for i in corpus_list:
        final_list.append(book_data(i, 'all', 'all', 'guitar'))
    for a in final_list:
        for b in a:
            final_final.append(b)
    for x in final_list:
        temp_notes_list = []
        for y in range(12):
            if y in x:
                temp_notes_list.append(x[y])
            else:
                temp_notes_list.append(0)
    return final_final

# all_corpus_data = corpus_converter(all_alfabeto)


def alf_notes_and_labels(corpus_list):
    final_notes_list = []
    real_final_notes = []
    final_notes_labels = []
    for x in corpus_list:
        for z in x.values():
            final_notes_list.append(CM.note_frequency_song(z))
            final_notes_labels.append((z['data']['key'], z['data']['final']))
    for x in final_notes_list:
        temp_notes_list = []
        for y in range(12):
            if y in x:
                temp_notes_list.append(x[y])
            else:
                temp_notes_list.append(0)
        real_final_notes.append(temp_notes_list)
    return real_final_notes, final_notes_labels


# all_notes = []
# # for x in all_sources.GetComposer.all_vitali:
# for x in all_sources.GetAll.all_alf:
#     for z in x.values():
#         all_notes.append(CM.note_frequency_song(z))
#         label = (z['data']['key'], z['data']['final'])
#         corpus_labels.append(label)
#
# named_labels = corpus_labels
# alf_labels = []

# for x in range(len(all_corpus_data)):
#     alf_labels.append('o')

# for x in named_labels:
#     if x == ('f', 2):
#         alf_labels.append('$♭:D$')
#     elif x == ('n', 4):
#         alf_labels.append('$♮:E$')
#     elif x == ('n', 9):
#         alf_labels.append('$♮:A$')
#     elif x == ('f', 7):
#         alf_labels.append('$♭:G$')
#     elif x == ('n', 2):
#         alf_labels.append('$♮:D$')
#     elif x == ('f', 9):
#         alf_labels.append('$♭:A$')
#     elif x == ('f', 0):
#         alf_labels.append('$♭:C$')
#     elif x == ('f', 10):
#         alf_labels.append('$♭:B♭$')
#     elif x == ('n', 5):
#         alf_labels.append('$♮:F$')
#     elif x == ('n', 0):
#         alf_labels.append('$♮:C$')
#     elif x == ('f', 5):
#         alf_labels.append('$♭:F$')
#     elif x == ('n', 7):
#         alf_labels.append('$♮:G$')
#     elif x == 'Temperley MAJOR':
#         alf_labels.append('$Temperley MAJOR$')
#     elif x == 'Temperley MINOR':
#         alf_labels.append('$Temperley MINOR$')
#
#     else:
#         alf_labels.append('o')
#
# temp_maj = {0: 0.184, 1: 0.001, 2: 0.155, 3: 0.003, 4: 0.191,
#             5: 0.109, 6: 0.005, 7: 0.214, 8: 0.001, 9: 0.078,
#             10: 0.004, 11: 0.055}
#
# temp_min = {0: 0.192, 1: 0.005, 2: 0.149, 3: 0.179, 4: 0.002,
#             5: 0.144, 6: 0.002, 7: 0.201, 8: 0.038, 9: 0.012,
#             10: 0.053, 11: 0.022}

# t_maj = [temp_maj[x] * 100 for x in range(12)]
# t_min = [temp_min[x] * 100 for x in range(12)]
#
# final_notes = []
# # final_notes.append(t_maj)
# # final_notes.append(t_min)
#
# # final_notes_corpus.append(t_maj)
# # final_notes_corpus.append(t_min)
#
# for x in all_notes:
#     temp_list = []
#     for y in range(12):
#         temp_list.append(x[y])
#     final_notes.append(temp_list)
#
# final_alf_notes = final_notes
# final_alf_labels = alf_labels

# --------averages---------#
# af0 = CM.note_frequency(CM.all_alf, ('f', 0))
# af2 = CM.note_frequency(CM.all_alf, ('f', 2))
# af5 = CM.note_frequency(CM.all_alf, ('f', 5))
# af7 = CM.note_frequency(CM.all_alf, ('f', 7))
# af9 = CM.note_frequency(CM.all_alf, ('f', 9))
# af10 = CM.note_frequency(CM.all_alf, ('f', 10))
#
# an0 = CM.note_frequency(CM.all_alf, ('n', 0))
# an2 = CM.note_frequency(CM.all_alf, ('n', 2))
# an4 = CM.note_frequency(CM.all_alf, ('n', 4))
# an5 = CM.note_frequency(CM.all_alf, ('n', 5))
# an7 = CM.note_frequency(CM.all_alf, ('n', 7))
# an9 = CM.note_frequency(CM.all_alf, ('n', 9))
#
# amaj = CM.note_frequency(CM.all_alf, 'major')
# amin = CM.note_frequency(CM.all_alf, 'minor')
# aall = CM.note_frequency(CM.all_alf, 'all')
#
#
# temp_maj = {0: 0.184, 1: 0.001, 2: 0.155, 3: 0.003, 4: 0.191,
#             5: 0.109, 6: 0.005, 7: 0.214, 8: 0.001, 9: 0.078,
#             10: 0.004, 11: 0.055}
#
# temp_min = {0: 0.192, 1: 0.005, 2: 0.149, 3: 0.179, 4: 0.002,
#               5: 0.144, 6: 0.002, 7: 0.201, 8: 0.038, 9: 0.012,
#               10: 0.053, 11: 0.022}
#
# f0 = [af0[x] for x in range(12)]
# f2 = [af2[x] for x in range(12)]
# f5 = [af5[x] for x in range(12)]
# f7 = [af7[x] for x in range(12)]
# f9 = [af9[x] for x in range(12)]
# f10 = [af10[x] for x in range(12)]
#
# n0 = [an0[x] for x in range(12)]
# n2 = [an2[x] for x in range(12)]
# n4 = [an4[x] for x in range(12)]
# n5 = [an5[x] for x in range(12)]
# n7 = [an7[x] for x in range(12)]
# n9 = [an9[x] for x in range(12)]
#
# alf_maj = [amaj[x] for x in range(12)]
# alf_min = [amin[x] for x in range(12)]
# alf_all = [aall[x] for x in range(12)]
#
# t_maj = [temp_maj[x]* 100 for x in range(12)]
# t_min = [temp_min[x]* 100 for x in range(12)]
#
# all_modes = [f0, f2, f5, f7, f9, f10, n0, n2, n4, n5, n7, n9, t_maj, t_min]
#
# named_labels = [('f', 0), ('f', 2), ('f', 5), ('f', 7), ('f', 9), ('f', 10), ('n', 0),
#               ('n', 2), ('n', 4), ('n', 5), ('n', 7), ('n', 9), 'Temperley MAJOR', 'Temperley MINOR']
# alf_labels = []
# for x in named_labels:
#     if x == ('f', 2):
#         alf_labels.append('$♭:D$')
#     elif x == ('n', 4):
#         alf_labels.append('$♮:E$')
#     elif x == ('n', 9):
#         alf_labels.append('$♮:A$')
#     elif x == ('f', 7):
#         alf_labels.append('$♭:G$')
#     elif x == ('n', 2):
#         alf_labels.append('$♮:D$')
#     elif x == ('f', 9):
#         alf_labels.append('$♭:A$')
#     elif x == ('f', 0):
#         alf_labels.append('$♭:C$')
#     elif x == ('f', 10):
#         alf_labels.append('$♭:B♭$')
#     elif x == ('n', 5):
#         alf_labels.append('$♮:F$')
#     elif x == ('n', 0):
#         alf_labels.append('$♮:C$')
#     elif x == ('f', 5):
#         alf_labels.append('$♭:F$')
#     elif x == ('n', 7):
#         alf_labels.append('$♮:G$')
#     elif x == 'Temperley MAJOR':
#         alf_labels.append('$Temperley MAJOR$')
#     elif x == 'Temperley MINOR':
#         alf_labels.append('$Temperley MINOR$')

def k_means_data(list_of_lists, cluster_number):
    np.random.seed(42)

    digits = np.array(list_of_lists)
    # data = sklp.scale(digits)
    data = digits

    label_numbers = []
    for i in range(len(list_of_lists)):
        label_numbers.append(i)

    n_samples, n_features = data.shape
    n_digits = cluster_number
    labels = np.array(label_numbers)

    # sample_size = 300

    sample_size = len(data)

    print("n_digits: %d, \t n_samples %d, \t n_features %d"
          % (n_digits, n_samples, n_features))

    print(79 * '_')
    print('% 9s' % 'init'
                   '    time  inertia    homo   compl  v-meas     ARI AMI  silhouette')

    def bench_k_means(estimator, name, data):
        t0 = time()
        estimator.fit(data)
        print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
              % (name, (time() - t0), estimator.inertia_,
                 metrics.homogeneity_score(labels, estimator.labels_),
                 metrics.completeness_score(labels, estimator.labels_),
                 metrics.v_measure_score(labels, estimator.labels_),
                 metrics.adjusted_rand_score(labels, estimator.labels_),
                 metrics.adjusted_mutual_info_score(labels, estimator.labels_),
                 metrics.silhouette_score(data, estimator.labels_,
                                          metric='euclidean',
                                          sample_size=sample_size)))

    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
                  name="k-means++", data=data)

    bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
                  name="random", data=data)

    # in this case the seeding of the centers is deterministic, hence we run the
    # kmeans algorithm only once with n_init=1
    pca = PCA(n_components=n_digits).fit(data)
    bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
                  name="PCA-based",
                  data=data)
    print(79 * '_')

    ###############################################################################
    # Visualize the results on PCA-reduced data

    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    # for w, y, z in zip(reduced_data[:, 0], reduced_data[:, 1], alf_labels):
    #     if z == '$Temperley MAJOR$' or z == '$Temperley MINOR$':
    #         plt.plot(w, y, 'k.', marker=z, color='white', markersize=len(z)*5)
    #     else:
    #         plt.plot(w, y, 'k.', marker=z, markersize=len(z) * 5, alpha=.3)
        # plt.plot(x, y, 'k.')

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', marker='o', markersize=5)
    print('reduced data:', '1', reduced_data[:, 0], '2', reduced_data[:, 0])
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering of alfabeto corpus (PCA-reduced data)\n'
              'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()


