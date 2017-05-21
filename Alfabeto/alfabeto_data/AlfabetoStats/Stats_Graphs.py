from alfabeto_data.AlfabetoStats import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

freq = stats.mds_graph_chordFQ(stats.all_alfabeto, 'major', 'all', 'guitar')


def dict_maker(korpus, frequency):
    corpus_dict = {}
    for x, y in zip(korpus, frequency):
        temp_dict = {}
        for a, b in zip(korpus, y):
            temp_dict[a] = b
        corpus_dict[x] = temp_dict
    return corpus_dict


def sorted_freq(frequency):
    all_freq = []
    for x in frequency:
        for y in x:
            all_freq.append(y)
    nonzero_freq = []
    for x in all_freq:
        if x != 0.0:
            nonzero_freq.append(x)
    return sorted(set(nonzero_freq))

# corpus = [i for i in range(len(stats.all_kaps))]
corpus = ['k1', 'k2', 'k3', 'k4',
          'obizzi', 'stefani', 'sanz', 'abbatessa',
          'palestrina', 'monteverdi', 'bach',
          'haydn', 'mozart', 'beethoven']
corp_dict = dict_maker(corpus, freq)
sort_freq = sorted_freq(freq)


def list_maker():
    final_list = []
    for x in sort_freq:
        for a, b in corp_dict.items():
            for c, d in b.items():
                if d == x:
                    final_list.append([a, c, d])
    for x in final_list[1::2]:
        print(x[0], x[1], x[2])
    return final_list[1::2] # removes duplicates

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = []
Y = []
Z = []
X_labels = []
Y_labels = []

for i in list_maker():
    # X.append(range(len(list_maker())))
    # Y.append(range(len(list_maker())))
    X.append(i[0])
    Y.append(i[1])
    Z.append(i[2])


ax.plot(X, Y, Z, c='b', marker='o')
# ax.bar(X, Y, Z, zdir='x')
ax.set_xlabel('corpus a')
ax.set_ylabel('corpus b')
ax.set_zlabel('similarity distance')
# plt.xticks(X, X_labels)
# plt.yticks(Y, Y_labels)

plt.show()
"""