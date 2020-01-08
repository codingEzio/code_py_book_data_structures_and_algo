# Ref: https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html

import matplotlib.pyplot as plt
import networkx as nx

Graph = nx.Graph()

edges = (
    ("a", "b", 7),
    ("a", "c", 9),
    ("a", "f", 14),
    ("b", "c", 10),
    ("b", "d", 15),
    ("c", "d", 11),
    ("c", "f", 2),
    ("d", "e", 6),
    ("e", "f", 9),
)

for orig, dest, weight in edges:
    Graph.add_edge(orig, dest, weight=weight)

# These two lines were meant to show different styles for different weights.
# I still use the default params since I don't NEED that distinction!
elarge = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in Graph.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(Graph)  # positions for all nodes


# nodes
nx.draw_networkx_nodes(Graph, pos, node_size=700)

# edges
nx.draw_networkx_edges(Graph, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    Graph,
    pos,
    edgelist=esmall,
    width=6,
    alpha=0.5,
    edge_color="b",
    style="dashed",
)

# labels
nx.draw_networkx_labels(Graph, pos, font_size=20, font_family="sans-serif")

plt.axis("off")

# plt.show()
plt.savefig(fname="./images/weighted_graph.png", dpi=350)
