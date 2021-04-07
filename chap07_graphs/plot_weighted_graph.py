# References:
# https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
# https://stackoverflow.com/questions/56597840/drawing-weighted-graph-from-adjacency-matrix-with-edge-labels
from data import edges_with_weights as edges

import matplotlib.pyplot as plt
import networkx as nx

# Graph = nx.Graph()
Graph = nx.DiGraph(directed=True)

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
nx.draw_networkx_edges(Graph, pos, edgelist=elarge, width=3)
nx.draw_networkx_edges(
    Graph,
    pos,
    edgelist=esmall,
    width=3,
    alpha=0.5,
    edge_color="b",
    style="dashed",
)

# labels
nx.draw_networkx_labels(Graph, pos, font_size=15, font_family="sans-serif")

weight_labels = nx.get_edge_attributes(Graph, "weight")
nx.draw_networkx_edge_labels(Graph, pos, weight_labels)

plt.axis("off")

# plt.show()
plt.savefig(fname="./images/weighted_graph.png", dpi=230)
