# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
#
#
#
# DistMatrix = np.array([[0, 17.2217257417, 15.518947638829232, 31.477213948884554],
#                        [17.2217257417, 0, 6.8100147494499055, 19.543316860132194],
#                        [15.518947638829232, 6.8100147494499055, 0, 14.78754625450533],
#                        [31.477213948884554, 19.543316860132194, 14.78754625450533, 0]])
#
#
#
# G = nx.from_numpy_matrix(DistMatrix)
# # pos = nx.spring_layout(G)
# print(G.nodes(data=True))
# print(G.edges(data=True))
# # nx.draw(G, edge_color=[i[2]['weight'] for i in G.edges(data=True)])
# nx.draw_networkx(G, with_labels=True)
# # nx.draw_networkx_edge_labels(G)
# plt.show()


import networkx as nx
import numpy as np
import string
from networkx.drawing.nx_agraph import to_agraph
import matplotlib.pyplot as plt
from alfabeto_data.AlfabetoStats.stats import chord_frequency
from alfabeto_sources import *

all_corpus = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4, obizzi.libro_primo, stefani.stefani, sanz.sanz_1674]
all_kaps = [kapsperger.v1, kapsperger.v2, kapsperger.v3, kapsperger.v4]
obi = [obizzi.libro_primo]
ste = [stefani.stefani]
kap1 = [kapsperger.v1]
kap2 = [kapsperger.v2]
kap3 = [kapsperger.v3]
kap4 = [kapsperger.v4]
sanz = [sanz.sanz_1674]

def mds_graph(comparison_list, mode, progression_element, tab):
    dt = [('len', float)]
    # k1, k2, k3, k4, sanz1
    source_distances = []
    source_percentages = []
    for x in comparison_list:
        source_percentages.append(chord_frequency([x], mode, progression_element, tab))
    print(source_percentages)
    # for x in source_percentages:
    #     for numeral in numerals:
    # A = np.array([[0, 17.2217257417, 15.518947638829232, 31.477213948884554, 21.96337643923826],
    #               [17.2217257417, 0, 6.8100147494499055, 19.543316860132194, 18.197268389163],
    #               [15.518947638829232, 6.8100147494499055, 0, 14.78754625450533, 15.950668052942902],
    #               [31.477213948884554, 19.543316860132194, 14.78754625450533, 0, 26.016208823067529],
    #               [21.96337643923826, 18.197268389163, 15.950668052942902, 26.016208823067529, 0]]) / 10
    #
    # A = A.view(dt)
    #
    # G = nx.from_numpy_matrix(A)
    # G = nx.relabel_nodes(G, {0:'k1', 1:'k2', 2:'k3', 3:'k4', 4: 'sanz'})
    #
    # G = to_agraph(G)
    #
    # G.node_attr.update(color="blue", style="filled")
    # G.edge_attr.update(color="black", width="2.0")
    #
    # G.draw('/home/daniel/Desktop/test.png', format='png', prog='neato')
    # nx.draw(G, prog='neato')
