"""
main.py - Contains functions to construct/explore circuit graph defined in circuit.xml
"""

from app.graph import CircuitGraph
import xml.etree.ElementTree as ET

from typing import List


def parse_circuit() -> List:
    nodes = []
    edges = []
    tree = ET.parse("circuit.xml")

    for el in tree.iter():
        attr = el.attrib
        if attr:
            id = attr["id"]
            to = attr["to"].split(" ")

            nodes.append(id)
            edges.append([(id, to) for t in to])

    return [nodes, edges]


if __name__ == "__main__":
    c = CircuitGraph()

    nodes, edges = parse_circuit()
    c.add_nodes(nodes)
    c.add_edges(edges)
    c.draw()

    print(c.find_cycles())
