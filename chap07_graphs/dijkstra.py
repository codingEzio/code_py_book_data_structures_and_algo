# Ref: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
from data import edges_with_weights as edges

from collections import deque, namedtuple
from math import inf

Edge = namedtuple(typename="Edge", field_names=["start", "end", "cost"])


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        """
        Validate & give tuples a name
        """
        # Validate given tuples
        wrong_edges = [i for i in edges if len(i) not in (2, 3)]
        if wrong_edges:
            raise ValueError(f"Wrong edges data: {wrong_edges}")

        # Returns a list of tuples (with a name called 'Edge')
        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        """Return a set of strings that stands for vertices/nodes."""
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    @property
    def neighbours(self):
        # Assign a default value (set()),     i.e. { "a": set(), .. }
        neighbours = {vertex: set() for vertex in self.vertices}

        # Assign a tuple (END, WEIGHT) to each vertices/nodes
        # what we're doing: loop << VERTEX[START].add((END, WEIGHT)) >>
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, destination):
        """
        During my step-by-step, I found that some of the steps(routes)
        might not be seemed clever or efficient, BUT, the final result
        still achieves "the shortest route", amazing! (well, I think it's
        mainly due to I havn't really fully understand this algorithm XD)
        """

        # Validaton on whether your `source` is in the nodes
        assert source in self.vertices, "Such source node does not exist"

        # Assign a default value (Infinity), i.e. { "a": Infinity, .. }
        distances = {vertex: inf for vertex in self.vertices}

        # Assign a default value (None),     i.e. { "a": None, .. }
        previous_vertices = {vertex: None for vertex in self.vertices}

        # Assign 0 to the source node (therefore became the smallest)
        distances[source] = 0

        # A copy of set of strings for calc the cost (del one after each loop)
        vertices = self.vertices.copy()

        # This whole algorithm takes about 779 steps, 553 of them in this loop.
        while vertices:
            # Each round the loop would do these things:
            # 1) record the length of the route
            # 2) store  the map between START to NEXT_DEST
            # 3) finally, remove the key after done two things above

            # find the vertex (=> a string) holds the smallest distance
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex]
            )

            # Ignore if vertex is inf (== "is in initial state")
            if distances[current_vertex] == inf:
                break

            # for { NEXT_DEST, WEIGHT } in a set of { NODE: set(X, Y) }
            for neighbour, cost in self.neighbours[current_vertex]:
                # form a route (0 + next_dest_cost) from START to NEIGHBOUR
                # returns a integer (sum of cost (from here to there))
                alternative_route = distances[current_vertex] + cost

                # real route VERSUS default inf
                # -> update distance[NEXT_DEST] = length of real route
                # -> set_of_nodes_with_None[NEXT_DEST] = "a" (like tracing)
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # remove the string(vertex|node) from the set
            vertices.remove(current_vertex)

        path, current_vertex = deque(), destination
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        if path:
            path.appendleft(current_vertex)

        return path

    def get_node_pairs(self, node1, node2, both_ends=True):
        if both_ends is True:
            node_pairs = [[node1, node2], [node2, node1]]
        else:
            node_pairs = [[node1, node2]]

        return node_pairs

    def add_edge(self, node1, node2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(
            node1=node1, node2=node2, both_ends=True
        )
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                raise ValueError(f"Edge {node1} {node2} already exists")

        self.edges.append(Edge(start=node1, end=node2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=node2, end=node1, cost=cost))

    def remove_edge(self, node1, node2, both_ends=True):
        node_pairs = self.get_node_pairs(
            node1=node1, node2=node2, both_ends=True
        )
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)


def main() -> None:
    graph = Graph(edges)

    assert graph.dijkstra("a", "e") == deque(["a", "c", "d", "e"])


if "__main__" == __name__:
    main()
