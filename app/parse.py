"""
parse.py - Contains parsing functions for XML structure defined in circuit.xml
"""

from app.config import _XML_FILE_PATH
import xml.etree.ElementTree as ET
from typing import List


def parse_circuit() -> List:
    """Obtains nodes and edges denoted by circuit structure in provided XML

    :return: two-element list [nodes, edges]
    """
    nodes = []
    edges = []
    tree = ET.parse(_XML_FILE_PATH)

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
