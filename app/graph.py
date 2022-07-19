"""
graph.py - Contains the CircuitGraph class for handling all graph operations.
"""

from app.parse import parse_circuit
import networkx as nx
from typing import List


class CircuitGraph(nx.DiGraph):
    """This class organizes graph construction when documenting circuits.
    Note that it inherits NetworkX's Graph class; thus, able to use methods and
    properties of that class.
    """

    def __init__(self, xml_file_path: str = "") -> None:
        """Constructor method

        :param xml_file_path: file path to XML file describing circuit
        """

        print("Constructing circuit graph...")
        super().__init__()
        if xml_file_path:
            [nodes, edges] = parse_circuit(xml_file_path)
            self.add_nodes(nodes)
            self.add_edges(edges)
        print("Circuit graph constructed.")

    def add_nodes(self, nodes: List[tuple]) -> None:
        """Adds list of nodes to graph. Nodes should be formatted as per below.
        ("group_#_type_#", {"type": "xxx", "extra_attr": "xxx"})

        :param nodes: list of tuples containing node info
        """
        self.add_nodes_from(nodes)

    def add_edges(self, edges: List[tuple]) -> None:
        """Adds list of edges to graph. Edges should be formatted as per below.
        ("id_from", "id_to", {"directed": True})

        :param edges: list of tuples containing edge info
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
        cycles = list(nx.simple_cycles(temp_G))
        return [cycle for cycle in cycles if len(cycle) > 2]

    def find_paths(self, from_node: str, to_node: str) -> List:
        """Finds all paths from one node to another.

        :param from_node: id of node to start from for path traversal
        :param to_node: id of node to end at for path traversal
        :return: list of paths from one node to another
        """
        return list(nx.all_simple_paths(self, from_node, to_node))

    def draw(self) -> None:
        """Produces a visual graph of circuit"""
        nx.draw(self, with_labels=True)
