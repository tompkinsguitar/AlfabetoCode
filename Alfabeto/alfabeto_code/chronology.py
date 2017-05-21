import matplotlib.pyplot as plt
from alfabeto_code import AlfabetoMarkov as markov
from alfabeto_sources import *
from alfabeto_code import AlfabetoGraphs as ag
import numpy as np
from scipy.stats.stats import pearsonr
# from scipy.spatial.distance import cosine


# all_corpus = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, , kapsperger.v5, kapsperger.v6, kapsperger.v7,
#              obizzi.libro_primo, stefani.stefani, sanz.sanz_1674]
all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7]
obi = [obizzi.libro_primo]
ste = [stefani.stefani]
kap1 = [kapsperger.v1]
kap2 = [kapsperger.v2]
kap3 = [kapsperger.v3]
kap4 = [kapsperger.v4]
kap5 = [kapsperger.v5]
kap6 = [kapsperger.v6]
kap7 = [kapsperger.v7]
sanz = [sanz.sanz_1674]


def stats(corpus, mode, ngram, number, progression_element, tab):
    corpus_data = markov.markovMaker(corpus, mode, ngram, progression_element, tab)
    all_numbers = []
    final = []
    if ngram == 2:
        for a in corpus_data.keys():
            for y in corpus_data[a].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])

    elif ngram == 3:
        for a, b in corpus_data.keys():
            for y in corpus_data[(a, b)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])

    elif ngram == 4:
        for a, b, c in corpus_data.keys():
            for y in corpus_data[(a, b, c)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])

    elif ngram == 5:
        for a, b, c, d in corpus_data.keys():
            for y in corpus_data[(a, b, c, d)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])
    elif ngram == 6:
        for a, b, c, d, e in corpus_data.keys():
            for y in corpus_data[(a, b, c, d, e)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])
    elif ngram == 7:
        for a, b, c, d, e, f in corpus_data.keys():
            for y in corpus_data[(a, b, c, d, e, f)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        for i in ranking[0:number]:
            for a in corpus_data.keys():
                for (x, y) in corpus_data[a].items():
                    if y == i:
                        if [a, x, y/ag.corpus_percentage(corpus_data)*100] not in final:
                            final.append([a, x, y/ag.corpus_percentage(corpus_data)*100])

    return final[0:number]


def tops(corpus, mode, ngrams, number, progression_element, tab):
    corpus_data = markov.markovMaker(corpus, mode, ngrams, progression_element, tab)
    all_numbers = []
    top = []
    if ngrams == 2:
        for a in corpus_data.keys():
            for y in corpus_data[a].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)
    elif ngrams == 3:
        for a, b in corpus_data.keys():
            for y in corpus_data[(a, b)].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)
    elif ngrams == 4:
        for a, b, c in corpus_data.keys():
            for y in corpus_data[(a, b, c)].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)
    elif ngrams == 5:
        for a, b, c, d in corpus_data.keys():
            for y in corpus_data[(a, b, c, d)].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)
    elif ngrams == 6:
        for a, b, c, d, e in corpus_data.keys():
            for y in corpus_data[(a, b, c, d, e)].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)
    elif ngrams == 7:
        for a, b, c, d, e, f in corpus_data.keys():
            for y in corpus_data[(a, b, c, d, e, f)].values():
                all_numbers.append(y)
        percent = [x / ag.corpus_percentage(corpus_data) * 100 for x in all_numbers]
        ranking = sorted(percent, reverse=True)
        for x in ranking[0:number]:
            top.append(x)

    return top


def plotter(corpus, mode, ngram, number, color, progression_element, tab):
    data = stats(corpus, mode, ngram, number, progression_element, tab)
    x = [s for s in range(number)]
    y = []
    labels = []
    for i in data:
        print(i)
        y.append(i[-1])
        # labels.append((i[0:-1]))
    plt.plot(x, y, color)
    # You can specify a rotation for the tick labels in degrees or with keywords.
    # plt.xticks(x, labels, rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.2)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    plt.show()


def list_maker(corpus, ngram):
    list_list = []
    if ngram == 2:
        for x in corpus:
            a_list = []
            a_list.append('  '.join(x[0:2]))
            a_list.append(x[-1])
            list_list.append(a_list)
    else:
        for x in corpus:
            first_list = []
            hmm = []
            for y in x[0]:
                hmm.append(y)
            hmm.append(x[1])
            first_list.append('  '.join(hmm))
            first_list.append(x[-1])
            list_list.append(first_list)
    return list_list


def kaps_plotter(ngram, mode, number, title, progression_element, tab):
    top_list = []
    top_stats = list_maker(stats(all_kaps, mode, ngram, number, progression_element, tab), ngram)
    for x in top_stats:
        top_list.append(x[0])
    k1 = list_maker(stats(kap1, mode, ngram, None, progression_element, tab), ngram)
    k2 = list_maker(stats(kap2, mode, ngram, None, progression_element, tab), ngram)
    k3 = list_maker(stats(kap3, mode, ngram, None, progression_element, tab), ngram)
    k4 = list_maker(stats(kap4, mode, ngram, None, progression_element, tab), ngram)
    k5 = list_maker(stats(kap5, mode, ngram, None, progression_element, tab), ngram)
    k6 = list_maker(stats(kap6, mode, ngram, None, progression_element, tab), ngram)
    k7 = list_maker(stats(kap7, mode, ngram, None, progression_element, tab), ngram)


    # obi_corp = list_maker(stats(obi, mode, ngram, None, progression_element, tab), ngram)
    # ste_corp = list_maker(stats(ste, mode, ngram, None, progression_element, tab), ngram)
    # sanz_corp = list_maker(stats(sanz, mode, ngram, None, progression_element, tab), ngram)

    k1_data = []
    k2_data = []
    k3_data = []
    k4_data = []
    k5_data = []
    k6_data = []
    k7_data = []

    obi_data = []
    ste_data = []
    sanz_data = []

    mean_data = []
    X = [i for i in range(number)]

    def data_appender(corpus, data):
        for x in top_stats:
            z = 0
            for y in corpus:
                if x[0] == y[0]:
                    z += 1
                    data.append(y[1])
            if z == 0:
                data.append(0)

    data_appender(k1, k1_data)
    data_appender(k2, k2_data)
    data_appender(k3, k3_data)
    data_appender(k4, k4_data)
    data_appender(k5, k5_data)
    data_appender(k6, k6_data)
    data_appender(k7, k7_data)

    # data_appender(ste_corp, ste_data)
    # data_appender(obi_corp, obi_data)
    # data_appender(sanz_corp, sanz_data)

    for w, x, y, z, a, b, c in zip(k1_data, k2_data, k3_data, k4_data, k5_data, k6_data, k7_data):
        mean_data.append(np.mean([w, x, y, z, a, b, c]))
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
    # plt.plot(k1_data, 'g', linewidth=2.0, label='Book 1 (1610)')
    # plt.plot(k2_data, 'b', linewidth=2.0, label='Book 2 (1619)')
    # plt.plot(k3_data, 'r--', linewidth=2.0, label='Book 3 (1619)')
    # plt.plot(k4_data, 'y', linewidth=2.0, label='Book 4 (1623)')
    plt.plot(mean_data, 'black', linewidth=8.0, alpha=.3, label='Mean(Average)')
    plt.xlabel('Harmonic progression by occurrence', size=24)
    plt.ylabel('Percent Occurrence', size=24)
    plt.title(title, size=30)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    # plt.plot(x, y, 'g')
    plt.xticks(X, top_list, rotation=45, size=20, family='serif')
    # Y = [x for x in range(10)]
    plt.yticks(size=20)
    plt.subplots_adjust(bottom=0.2)
    #
    plt.show()
    return {'k1': k1_data, 'k2': k2_data, 'k3': k3_data, 'k4': k4_data, 'k5': k5_data, 'k6': k6_data, 'k7': k7_data,
            'mean': mean_data}


def kaps_plotter_2(corpus, mode, ngram, number, title, progression_element, tab):
    top_list = []
    # print(top_list)
    top_stats = list_maker(stats(corpus, mode, ngram, number, progression_element, tab), ngram)

    stats_data = []

    for x in top_stats:
        stats_data.append(x[1])

    for x in top_stats:
        top_list.append(x[0])

    X = [i for i in range(number)]
    bar_width = 0.5

    plt.bar(X, stats_data, bar_width, color='b', label=title, align='center')

    plt.xlabel('Harmonic progression by occurrence')
    plt.ylabel('Percent occurrence')
    plt.title(title)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    # plt.plot(x, y, 'g')
    plt.xticks(X, top_list, rotation=45, size=20, family='serif')
    plt.yticks(size=20)
    plt.subplots_adjust(bottom=0.2)

    plt.tight_layout()
    plt.show()


def tab_comparison(theorbo, guitar, mode, ngram, number, title, progression_element, tab_priority):
    top_list = []
    first_tab = []
    if tab_priority == 'guitar':
        first_tab.append(guitar)
    elif tab_priority == 'theorbo':
        first_tab.append(theorbo)
    top_stats = list_maker(stats(first_tab, mode, ngram, number, progression_element, tab_priority), ngram)
    for x in top_stats:
        top_list.append(x[0])
    t1 = list_maker(stats([theorbo], mode, ngram, None, progression_element, 'theorbo'), ngram)
    t2 = list_maker(stats([guitar], mode, ngram, None, progression_element, 'guitar'), ngram)
    t1_data = []
    t2_data = []
    X = [i for i in range(number)]
    # y = [0, 1, 2, 3, 3, 5, 4, 2, 6, 5]
    for x in top_stats:
        z = 0
        for y in t1:
            if x[0] == y[0]:
                z += 1
                t1_data.append(y[1])
        if z == 0:
            t1_data.append(0)
    for x in top_stats:
        z = 0
        for y in t2:
            if x[0] == y[0]:
                z += 1
                t2_data.append(y[1])
        if z == 0:
            t2_data.append(0)
    # plt.hist(X)

    plt.plot(t1_data, 'g', linewidth=2.0, label='theorbo')
    plt.plot(t2_data, 'b', linewidth=2.0, label='guitar')
    plt.xlabel('Harmonic progression by occurrence')
    plt.ylabel('Percent Occurrence')
    plt.title(title)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
    # plt.plot(x, y, 'g')
    plt.xticks(X, top_list, rotation='vertical', size=12)
    plt.subplots_adjust(bottom=0.2)
    #
    print('similarity:', pearsonr(t1_data, t2_data))
    plt.show()



# kaps1 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['k1']
# kaps2 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['k2']
# kaps3 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['k3']
# kaps4 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['k4']
# #
# obi1 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['obizzi']
# ste1 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['stefani']
# sanz1 = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['sanz']
# kmean = kaps_plotter(2, 'all', 50, 'test', 'all', 'guitar')['mean']

# kaps1 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['k1']
# kaps2 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['k2']
# kaps3 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['k3']
# kaps4 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['k4']
#
# obi1 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['obizzi']
# ste1 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['stefani']
# sanz1 = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['sanz']
# kmean = kaps_plotter(2, 'major', 50, 'test', 'all', 'guitar')['mean']

# kaps1 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['k1']
# kaps2 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['k2']
# kaps3 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['k3']
# kaps4 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['k4']
#
# obi1 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['obizzi']
# ste1 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['stefani']
# sanz1 = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['sanz']
# kmean = kaps_plotter(3, 'major', 100, 'test', 'all', 'guitar')['mean']