"""
parse.py - Contains parsing functions for XML structure defined in circuit.xml
"""

import xml.etree.ElementTree as ET
from typing import List


def parse_circuit(xml_file_path: str) -> List:
    """Obtains nodes and edges denoted by circuit structure in provided XML

    :param xml_file_path: file path to XML file describing circuit
    :return: two-element list [nodes, edges]
    """
    nodes = []
    edges = []
    tree = ET.parse(xml_file_path)

    # recursively iterate all elements in XML tree
    for el in tree.iter():
        attr = el.attrib
        if attr:
            id = attr["id"]
            nodes.append(id)

            if "to" in attr:
                to = attr["to"].split(" ")
                edges.extend([(id, t) for t in to])

    return [nodes, edges]
