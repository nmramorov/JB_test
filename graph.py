from data_getter import get_data

import matplotlib.pyplot as plt

import networkx as nx


LOGIN = '<login>'
PASSWORD = '<password>'
graph_data = get_data(LOGIN, PASSWORD)
nodes = []
totals = []
edges = []

for info in graph_data:
    nodes.append(info['login'])
    totals.append(info['total'])

nodes.append(1)

G = nx.Graph()

G.add_nodes_from(nodes)

ebunches = []
for node, total in zip(nodes, totals):
    ebunches.append((
        node,
        1,
        {'weight': total}
    ))

G.add_edges_from(ebunches)
nx.draw_shell(G, with_labels=True, font_weight='bold')
plt.show()

