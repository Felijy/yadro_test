from readXML import *
from makeConfig import *
from makeMeta import *

if __name__ == '__main__':
    with open('input/test_input.xml', 'r') as f:
        xml = f.read()
        classes, root_classes = parse_xml(xml)
        config_xml = make_xml(root_classes)
        with open('out/config.xml', 'w') as f:
            print(config_xml, file=f)
        json_result = make_json(root_classes, classes)
        with open('out/meta.json', 'w') as f:
            print(json_result, file=f)
