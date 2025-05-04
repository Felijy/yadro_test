from xml.etree import ElementTree
from classes.models import *
from classes.attribute import *
from classes.aggregation import *

def parse_xml(xml_file):
    tree = ElementTree.fromstring(xml_file)
    classes = []
    root_classes = []

    for element in tree.findall('Class'):
        if element.attrib['isRoot'] == "true":
            attributes_list = []
            for attribute in element:
                if attribute.tag == 'Attribute':
                    attributes_list.append(Attribute(attribute.attrib['name'], attribute.attrib['type']))
            if len(attributes_list) == 0:
                root_classes.append(RootClass(element.attrib['name'], element.attrib['documentation']))
            else:
                root_classes.append(RootClass(element.attrib['name'], element.attrib['documentation'], attributes_list))

        else:
            attributes_list = []
            for attribute in element:
                if attribute.tag == 'Attribute':
                    attributes_list.append(Attribute(attribute.attrib['name'], attribute.attrib['type']))
            if len(attributes_list) == 0:
                classes.append(NotRootClass(element.attrib['name'], element.attrib['documentation']))
            else:
                classes.append(NotRootClass(element.attrib['name'], element.attrib['documentation'], attributes_list))

    for element in tree.findall('Aggregation'):
        if '..' in element.attrib['sourceMultiplicity']:
            nums = element.attrib['sourceMultiplicity'].split('..')
            source_multiplicity = [nums[0], nums[1]]
        else:
            source_multiplicity = element.attrib['sourceMultiplicity']
        if '..' in element.attrib['targetMultiplicity']:
            nums = element.attrib['targetMultiplicity'].split('..')
            target_multiplicity = [nums[0], nums[1]]
        else:
            target_multiplicity = element.attrib['targetMultiplicity']
        aggregation = Aggregation(element.attrib['source'], element.attrib['target'],
                                  source_multiplicity, target_multiplicity)
        current_source_class = list(obj for obj in classes if obj.name == aggregation.source)
        if len(current_source_class) > 0:
            aggregation.source = current_source_class[0]
            current_source_class[0].source_connections.append(aggregation)
        current_target_class = list(obj for obj in classes if obj.name == aggregation.target)
        if len(current_target_class) > 0:
            aggregation.target = current_target_class[0]
            current_target_class[0].target_connections.append(aggregation)
        current_target_class = list(obj for obj in root_classes if obj.name == aggregation.target)
        if len(current_target_class) > 0:
            aggregation.target = current_target_class[0]
            current_target_class[0].target_connections.append(aggregation)

    return classes, root_classes