"""Graph Data Structure Module"""

from typing import List, Tuple, Hashable, Set


class Graph:
    """Base Class for Graphs."""
    def __init__(self):
        self._graph = {}  # Keep track of vertices' adjacency (we don't know who's the source or destination)

    @property
    def vertices(self) -> List[Hashable]:
        return list(self._graph.keys())

    @property
    def edges(self) -> List[Tuple[Hashable, Hashable]]:
        return [(vertex, adj_vertex) for vertex in self.vertices for adj_vertex in self.adjacent_vertices(vertex)]

    def get_graph(self):
        return self._graph

    def add_vertex(self, vertex) -> None:
        if vertex not in self.vertices:
            self._graph[vertex] = []

    def add_edge(self, vertex_1, vertex_2) -> None:
        self.add_vertex(vertex_1)
        self.add_vertex(vertex_2)

        self._graph[vertex_1].append(vertex_2)  # Add to Adjacency
        self._graph[vertex_2].append(vertex_1)  # Add to Adjacency

    def adjacent_vertices(self, vertex) -> List[Hashable]:
        return list(set(self._graph[vertex])) if vertex in self.vertices else []

    def is_adjacent(self, vertex_1, vertex_2) -> bool:
        return vertex_1 in self._graph[vertex_2] or vertex_2 in self._graph[vertex_1]


class DirectedGraph(Graph):
    """Digraph Data Structure"""
    def __init__(self):
        super().__init__()
        # self._allow_multi_edge = allow_multi_edge
        self._edges: List[Tuple[Hashable, Hashable]] = []  # List[Tuple[Hashable, Hashable]]

    @property
    def edges(self) -> List[Tuple[Hashable, Hashable]]:
        return self._edges

    def add_edge(self, source, destination) -> None:
        if (source, destination) not in self.edges:
            super().add_edge(source, destination)  # Add the adjacency
            self._edges.append((source, destination))

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            # 1. Remove the vertex from the graph dictionary
            adjacency_list = self._graph.pop(vertex)

            # 2. Remove any adjacency of the vertex
            for adjacent_vertex in adjacency_list:
                self._graph[adjacent_vertex].remove(vertex)

            for tup in self._edges:
                if tup[0] == vertex or tup[1] == vertex:
                    self._edges.remove(tup)

    def remove_edge(self, source, destination):
        if (source, destination) in self._edges:
            self._edges.remove((source, destination))
            self._graph[source].remove(destination)
            self._graph[destination].remove(source)

    def out_degree(self, vertex) -> List[Hashable]:
        # Where vertex is the source
        return [destination for (source, destination) in self.edges if source == vertex]

    def in_degree(self, vertex) -> List[Hashable]:
        # where vertex is the terminal or destination
        return [source for (source, destination) in self.edges if destination == vertex]


class UndirectedGraph(Graph):
    """Undirected Graph Data Structure."""
    def __init__(self):
        super().__init__()
        self._edges = []

    @property
    def edges(self) -> List[Set[Hashable]]:
        return self._edges

    def add_edge(self, vertex_1, vertex_2) -> None:
        new_2_set = {vertex_1, vertex_2}
        if new_2_set not in self._edges:
            super().add_edge(vertex_1, vertex_2)  # For Adjacency Bookkeeping
            self._edges.append(new_2_set)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            adjacency_list = self._graph.pop(vertex)

            for adjacent_vertex in adjacency_list:
                self._graph[adjacent_vertex].remove(vertex)

            for set_ in self._edges:
                if vertex in set_:
                    self._edges.remove(set_)

    def remove_edge(self, vertex_1, vertex_2):
        if {vertex_1, vertex_2} in self._edges:
            self._edges.remove({vertex_1, vertex_2})
            self._graph[vertex_1].remove(vertex_2)
            self._graph[vertex_2].remove(vertex_1)
