import xml.etree.ElementTree as ET

tree = ET.parse("circuit.xml")

for element in tree.iter():
    print(element.tag, element.attrib)
