import networkx as nx
import json

from typing import List


class CircuitGraph(nx.DiGraph):
    """This class organizes graph construction when documenting circuits.
    Note that it inherits NetworkX's Graph class; thus, able to use methods and
    properties of that class.
    """

    def __init__(self, fresh: bool) -> None:
        """Constructor method

        :param fresh: set True to get fresh Graph, otherwise loads from graph.json
        """

        data = []
        if not fresh:
            with open("graph.json", "r") as f:
                data = json.load(f)

        super().__init__(data)

    def add_nodes(self, nodes: List[tuple]) -> None:
        """Adds list of nodes to graph. Nodes should be formatted as per below.
        ("group_#_type_#", {"type": "xxx", "extra_attr": "xxx"})

        :param nodes: list of tuples containing node info
        """
        self.add_nodes_from(nodes)

    def add_edges(self, edges: List[tuple]) -> None:
        """Adds list of edges to graph. Edges should be formatted as per below.
        ("id_from", "id_to", {"directed": True})

        :param nodes: list of tuples containing edge info
        """
        extra_directions = [
            (e[1], e[0])
            for e in edges
            if len(e) < 3 or ("directed" not in e[2] or not e[2]["directed"])
        ]
        all_edges = edges + extra_directions
        self.add_edges_from(all_edges)

    def find_cycles(self) -> List:
        """Finds any cycles present in graph structure.

        :return: list of cycles found in graph
        """
        temp_G = nx.DiGraph(self)
        print(nx.node_link_data(self))
        return list(nx.simple_cycles(temp_G))

    def find_paths(self, from_node: str, to_node: str) -> List:
        """Finds all paths from one node to another.

        :param from_node: id of node to start from for path traversal
        :param to_node: id of node to end at for path traversal
        :return: list of paths from one node to another
        """
        return list(nx.all_simple_paths(self, from_node, to_node))
