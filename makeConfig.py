import xml.etree.ElementTree as ET
from xml.dom import minidom

def make_xml(root_classes):
    for rootClass in root_classes:
        root = ET.Element(rootClass.name)
        for attribute in rootClass.attributes:
            elem = ET.SubElement(root, attribute.name)
            elem.text = attribute.attr_type

        for connection in rootClass.target_connections:
            build_xml(root, connection.source)

    xml_str = ET.tostring(root, encoding="unicode")
    final_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
    return final_xml


def build_xml(root, target):
    element = ET.SubElement(root, target.name)
    try:
        for attribute in target.attributes:
            elem = ET.SubElement(element, attribute.name)
            elem.text = attribute.attr_type
    except AttributeError:
        pass
    except TypeError:
        pass
    for connection in target.target_connections:
        build_xml(element, connection.source)