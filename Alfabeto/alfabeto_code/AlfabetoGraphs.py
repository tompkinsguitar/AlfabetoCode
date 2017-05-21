import networkx as nx
from networkx.drawing.nx_agraph import write_dot
import matplotlib.pyplot as plt
from alfabeto_data import *
from alfabeto_code import AlfabetoMarkov as markov
from alfabeto_sources import *

all_alfabeto = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7,
                obizzi.libro_primo, stefani.stefani, sanz.sanz_1674, abbatessa.varii]

all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, kapsperger.v5, kapsperger.v6, kapsperger.v7]

kap1 = [kapsperger.v1]

kap2 = [kapsperger.v2]

kap3 = [kapsperger.v3]

kap4 = [kapsperger.v4]

kap5 = [kapsperger.v5]

kap6 = [kapsperger.v6]

kap7 = [kapsperger.v7]

sanz = [sanz.sanz_1674]


def clockface(G):
    new = {}
    for x in nx.circular_layout(G).keys():
        new[((3 - x) % 12)] = nx.circular_layout(G)[x]
    return new


def circle_fifths(G):
    new = {}
    for x in clockface(G).keys():
        new[(x * 7) % 12] = clockface(G)[x]
    return new


def node_number(book):
    lengths = {}
    for x in book.keys():
        allp = []
        for y in book[x]:
            allp.append(y)
        lengths[x] = sum(allp)
    return lengths


def node_size(corpus):
    sums = {}
    final_dict = {}
    for x in corpus:
        numbs = []
        for y in corpus[x].values():
            numbs.append(y)
        sums[x] = sum(numbs)
    for x in sums:
        final_dict[x] = sums[x] / sum(sums.values())
    return final_dict


def edge_size(book):
    lengths = {}
    for x in book.keys():
        allp = {}
        for y in book[x]:
            allp[y] = y.values()
    return lengths


def corpus_percentage(corpus):
    alls = []
    for x in corpus.values():
        for y in x.values():
            alls.append(y)
    return sum(alls)


def add_songs(corpus):
    new_dict = {}
    for x in corpus.values():
        for y in x.keys():
            if y in new_dict:
                new_dict[y] += x[y]
            else:
                new_dict[y] = x[y]
    return new_dict


def make_ngram_graph(data, mode, ngram, progression_element, tab):
    # G = nx.OrderedMultiDiGraph()
    G = nx.DiGraph()
    for x, y in all_data.numerals_tonnetz.items():
        G.add_node(x, pos=y)
    corpus_data = markov.markovMaker(data, mode, ngram, progression_element, tab)
    for x in corpus_data:
        for y in corpus_data[x]:
            if y in G.edges():
                old_percent = (G[y][x]['weight'])
                new_percent = corpus_data[x][y] / corpus_percentage(corpus_data) * 100
                G.add_edge(x, y, weight=(old_percent + new_percent), penwidth=(old_percent + new_percent))
            else:
                G.add_edge(x, y, weight=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100),
                           penwidth=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100))

    d = node_size(corpus_data)
    for x in d:
        G.add_node(x, weight=d[x])
    # print(d)
    # print(G.nodes(data=True))
    nodes = G.nodes(data=True)
    edges = G.edges(data=True)
    edge_weights = []
    for x in edges:
        edge_weights.append(x[2]['weight'])
        # print(x[2])
    node_weights = []
    for x in nodes:
        if 'weight' in x[1]:
            node_weights.append(x[1]['weight'] * 4000)
        else:
            node_weights.append(0)
    # meep = nx.spring_layout()
    # pos = nx.circular_layout(G, scale=5)
    pos = all_data.numerals_tonnetz
    # pos = nx.spring_layout(G, scale=15.0, iterations=100)
    nx.draw_networkx_edges(G, pos, edges=edges, edge_color='green', width=edge_weights, alpha=.5)
    nx.draw_networkx_nodes(G, pos, node_color='yellow', alpha=1, linewidths=0, node_size=node_weights)
    # nx.draw_networkx_nodes(G, pos, node_color='blue', alpha=.3, linewidths=0, node_size=0)
    nx.draw_networkx_labels(G, pos, font_size=15)
    write_dot(G, '/home/daniel/Desktop/tonnetz.dot')
    # print(G.nodes(data=True)[1][1])
    # # plt.grid(True)
    plt.axis('off')

    # plt.savefig('/home/daniel/Desktop/SMT proposal/kap_figs/All/kapsperger_v2_all.png', scale=5, dpi=300, bbox_inches='tight', pad_inches=0)
    # plt.title('Book 1 (1610)')
    # plt.axis([-6, 6, -6, 6])
    plt.show()


def make_graph(corpus_data):
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    for w in range(12):
        if w in corpus_data:
            for x in corpus_data[w]:
                if x in G[w]:
                    old_percent = (G[w][x]['weight'])
                    new_percent = corpus_data[w][x] / corpus_percentage(corpus_data) * 100
                    G.add_edge(w, x, weight=(old_percent + new_percent))
                else:
                    G.add_edge(w, x, weight=((corpus_data[w][x] / corpus_percentage(corpus_data)) * 100))

    d = node_size(corpus_data)
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]  # for x in all_numbers:
    #     G.add_node(x[0], weight=x[-1], category='ant')
    #     G.add_node(x[1], weight=3, category='con')
    # for x in nodes:
    #     if x[1]['category'] == 'ant':
    #         node_colors.append('blue')
    #     else:
    #         node_colors.append('red')
    color_map = {'ant': 'blue', 'con': 'yellow'}
    pos = clockface(G)
    # nx.draw(G, pos, edges=edges, edge_color='green', width=weights, node_size=[v*400 for v in d.values()], node_color='blue', alpha=.6)
    nx.draw_networkx_edges(G, pos, edges=edges, edge_color='green', width=weights, alpha=.9)
    nx.draw_networkx_nodes(G, pos, node_color='green', alpha=.6, linewidths=0, node_size=[v * 400 for v in d.values()])
    nx.draw_networkx_labels(G, pos)
    # print(weights)


def make_ngram_graph_2(data, mode, ngram, numeral, progression_element, tab):
    # G = nx.OrderedMultiDiGraph()
    all_numbers = []
    corpus_data = markov.markovMaker(data, mode, ngram, progression_element, tab)
    G = nx.DiGraph()
    if ngram == 2:
        for x in corpus_data:
            for y, z in corpus_data[x].items():
                if y == numeral or numeral == 'all':
                    all_numbers.append([x, y, z])
                    if y in G.edges():
                        old_percent = (G[x][y]['weight'])
                        new_percent = corpus_data[x][y] / corpus_percentage(corpus_data) * 100
                        G.add_path([x, y], weight=(old_percent + new_percent), penwidth=(old_percent + new_percent))
                    else:
                        G.add_path([x, y], weight=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100),
                                   penwidth=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100))

    elif ngram == 3:
        for a, b in corpus_data.keys():
            for x, y in corpus_data[(a, b)].items():
                temp = [a, b]
                temp2 = []
                if x == numeral or numeral == 'all':
                    temp2.append(' '.join(temp))
                    temp2.append(x)
                    temp2.append(y)
                    all_numbers.append(temp2)
        for x in all_numbers:
            if x[0] in G.edges() and x[1] in G.edges():
                old_percent = (G[x[0]][x[1]]['weight'])
                new_percent = x[-1] / corpus_percentage(corpus_data) * 100
                G.add_path(x[:-1], weight=(old_percent + new_percent))
            else:
                G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))

    elif ngram == 4:
        for a, b, c in corpus_data.keys():
            for x, y in corpus_data[(a, b, c)].items():
                temp = [a, b, c]
                temp2 = []
                if x == numeral or numeral == 'all':
                    temp2.append(' '.join(temp))
                    temp2.append(x)
                    temp2.append(y)
                    all_numbers.append(temp2)
        for x in all_numbers:
            if x[0] in G.edges() and x[1] in G.edges():
                old_percent = (G[x[0]][x[1]]['weight'])
                new_percent = x[-1] / corpus_percentage(corpus_data) * 100
                G.add_path(x[:-1], weight=(old_percent + new_percent))
            else:
                G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))

    elif ngram == 5:
        for a, b, c, d in corpus_data.keys():
            for x, y in corpus_data[(a, b, c, d)].items():
                temp = [a, b, c, d]
                temp2 = []
                if x == numeral or numeral == 'all':
                    temp2.append(' '.join(temp))
                    temp2.append(x)
                    temp2.append(y)
                    all_numbers.append(temp2)
        for x in all_numbers:
            if x[0] in G.edges() and x[1] in G.edges():
                old_percent = (G[x[0]][x[1]]['weight'])
                new_percent = x[-1] / corpus_percentage(corpus_data) * 100
                G.add_path(x[:-1], weight=(old_percent + new_percent))
            else:
                G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))

    elif ngram == 6:
        for a, b, c, d, e in corpus_data.keys():
            for x, y in corpus_data[(a, b, c, d, e)].items():
                temp = [a, b, c, d, e]
                temp2 = []
                if x == numeral or numeral == 'all':
                    temp2.append(' '.join(temp))
                    temp2.append(x)
                    temp2.append(y)
                    all_numbers.append(temp2)
        for x in all_numbers:
            if x[0] in G.edges() and x[1] in G.edges():
                old_percent = (G[x[0]][x[1]]['weight'])
                new_percent = x[-1] / corpus_percentage(corpus_data) * 100
                G.add_path(x[:-1], weight=(old_percent + new_percent))
            else:
                G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))

    elif ngram == 7:
        for a, b, c, d, e, f in corpus_data.keys():
            for x, y in corpus_data[(a, b, c, d, e, f)].items():
                temp = [a, b, c, d, e, f]
                temp2 = []
                if x == numeral or numeral == 'all':
                    temp2.append(' '.join(temp))
                    temp2.append(x)
                    temp2.append(y)
                    all_numbers.append(temp2)
        for x in all_numbers:
            if x[0] in G.edges() and x[1] in G.edges():
                old_percent = (G[x[0]][x[1]]['weight'])
                new_percent = x[-1] / corpus_percentage(corpus_data) * 100
                G.add_path(x[:-1], weight=(old_percent + new_percent))
            else:
                G.add_path(x[:-1], weight=((x[-1] / corpus_percentage(corpus_data)) * 100))
    # print(all_numbers)
    nodes = G.nodes(data=True)
    node_colors = []
    for x in all_numbers:
        G.add_node(x[0], weight=x[-1], category='ant')
        G.add_node(x[1], weight=5, category='con')
    for x in nodes:
        if x[1]['category'] == 'ant':
            node_colors.append('cyan')
        else:
            node_colors.append('green')
    # color_map = {'ant': 'blue', 'con': 'yellow'}
    # print(d)
    # print(G.nodes(data=True))
    edges = G.edges(data=True)
    edge_weights = []
    for x in edges:
        edge_weights.append(x[2]['weight'])
        # print(x[2])
    node_weights = []
    for x in nodes:
        if 'weight' in x[1]:
            # print(x[1])
            node_weights.append((x[1]['weight'] * 200))
        else:
            node_weights.append(0)
    # print(node_weights)
    # pos = nx.circular_layout(G, scale=5)
    pos = nx.spring_layout(G)
    nx.draw_networkx_edges(G, pos, edges=edges, edge_color='black', width=edge_weights, alpha=1)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, alpha=1, linewidths=0, node_size=node_weights)
    # nx.draw_networkx_nodes(G, pos, node_color=[color_map[G.node[node]['category']] for node in G], alpha=.6, linewidths=0, node_size=0)
    nx.draw_networkx_labels(G, pos, font_size=18, font_family='serif')
    write_dot(G, '/home/daniel/Desktop/blobs.dot')
    # print(G.nodes(data=True)[1][1])
    # # plt.grid(True)
    plt.axis('off')
    # plt.savefig('/home/daniel/Desktop/kapsperger_v1.png', dpi=300, bbox_inches='tight')
    # plt.close(plt)
    plt.show()


def make_ngram_graph_3(data, mode, ngram, progression_element, tab):
    # G = nx.OrderedMultiDiGraph()
    # corpus_data = markov.markovMaker(data, mode, ngram, progression_element, tab)
    corpus_data = markov.markovMaker_root(data, ngram, progression_element, tab)
    G = nx.Graph()
    for x in range(12):
        G.add_node(x, weight=0)
    if ngram == 2:
        for x in corpus_data:
            for y in corpus_data[x]:
                if y in G.edges():
                    old_percent = (G[y][x]['weight'])
                    new_percent = corpus_data[x][y] / corpus_percentage(corpus_data) * 100
                    G.add_path([x, y], weight=(old_percent + new_percent), penwidth=(old_percent + new_percent))
                else:
                    G.add_path([x, y], weight=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100),
                               penwidth=((corpus_data[x][y] / corpus_percentage(corpus_data)) * 100))
    elif ngram == 3:
        all_numbers = []
        for a, b in corpus_data.keys():
            for y in corpus_data[(a, b)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        # print(ranking)
        for a, b in corpus_data.keys():
            for x, y in corpus_data[(a, b)].items():
                if y == ranking[0]:
                    G.add_path([a, b, x], weight=((y / corpus_percentage(corpus_data)) * 100))
                elif y == ranking[1]:
                    G.add_path([a, b, x], weight=((y / corpus_percentage(corpus_data)) * 100))
    elif ngram == 4:
        all_numbers = []
        for a, b, c in corpus_data.keys():
            for y in corpus_data[(a, b, c)].values():
                all_numbers.append(y)
        ranking = sorted(all_numbers, reverse=True)
        # print(ranking)
        for a, b, c in corpus_data.keys():
            for x, y in corpus_data[(a, b, c)].items():
                if y == ranking[0]:
                    G.add_path([a, b, c, x], weight=((y / corpus_percentage(corpus_data)) * 100))
                elif y == ranking[1]:
                    G.add_path([a, b, c, x], weight=((y / corpus_percentage(corpus_data)) * 100))
    # print(G.edges(data=True))
    d = node_size(corpus_data)
    # for x in all_data.numerals:
    #     G.add_node(x, weight=0)

    node_weights = []
    nodes = G.nodes(data=True)
    print(nodes)
    for x in nodes:
        if 'weight' in x[1]:
            # print(x[1])
            node_weights.append((x[1]['weight'] * 200))
        else:
            node_weights.append(0)
    # print(d)
    # print(G.nodes(data=True))
    edges = G.edges(data=True)
    edge_weights = []
    for x in edges:
        edge_weights.append(x[2]['weight'])
        # print(x[2])
    node_weights = []
    for x in nodes:
        if 'weight' in x[1]:
            node_weights.append(x[1]['weight'] * 20000)
        else:
            node_weights.append(0)
    # pos = nx.circular_layout(G, scale=5)
    pos = clockface(G)
    # pos = nx.spring_layout(G, scale=15)
    nx.draw_networkx_edges(G, pos, edges=edges, edge_color='green', width=edge_weights, alpha=.9)
    # nx.draw_networkx_edge_labels(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color='blue', alpha=.6, linewidths=0, node_size=node_weights)
    # nx.draw_networkx_nodes(G, pos, node_color='blue', alpha=.6, linewidths=0, node_size=0)
    nx.draw_networkx_labels(G, pos, font_size=20)
    # print(G.nodes(data=True)[1][1])
    # # plt.grid(True)
    plt.axis('off')
    # plt.savefig('/home/daniel/Desktop/kapsperger_v1.png', dpi=300, bbox_inches='tight')
    # plt.close(plt)
    plt.show()


def make_table(corpus, mode, ngram, progression_element, tab):
    corpus = markov.markovMaker(corpus, mode, ngram, progression_element, tab)
    numerals = all_data.numerals
    lists = []
    total = []
    percent_data = []
    for x in numerals:
        alist = []
        if x in corpus:
            for a in numerals:
                if a in corpus[x]:
                    alist.append(corpus[x][a])
                else:
                    alist.append(0)
        # print(alist)
        else:
            for i in range(24):
                alist.append(0)
        lists.append(alist)
    # print(lists)
    for x in lists:
        for y in x:
            total.append(y)
    total_number = sum(total)
    for x in lists:
        temp_list = []
        for y in x:
            temp_list.append(y / total_number)
        percent_data.append(temp_list)
        # for x in percent_data:
        # print(x)

    return percent_data
