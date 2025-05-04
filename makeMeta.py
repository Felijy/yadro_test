import json


def make_json(root_classes, classes):
    all_dict = []
    for class_obj in root_classes:
        all_dict.append(class_to_dict(class_obj, True))
    for class_obj in classes:
        all_dict.append(class_to_dict(class_obj, False))
    json_string = json.dumps(all_dict, indent=4)
    return json_string

def class_to_dict(class_obj, root: bool):
    if not root:

        source_multiplicity = class_obj.source_connections[0].source_multiplicity
        if type(source_multiplicity) is list:
            str_min = source_multiplicity[0]
            str_max = source_multiplicity[1]
        else:
            str_min = source_multiplicity
            str_max = source_multiplicity

        params = []

        if class_obj.attributes is not None:
            for param in class_obj.attributes:
                params.append({
                    'name': param.name,
                    'type': param.attr_type,
                })

        if len(class_obj.target_connections) > 0:
            for target in class_obj.target_connections:
                params.append({
                    'name': target.source.name,
                    'type': 'class',
                })

        return {
            'class': class_obj.name,
            'documentation': class_obj.documentation,
            'isRoot': root,
            'max': str_max,
            'min': str_min,
            'parameters': params,
        }

    else:
        params = []

        for target in class_obj.target_connections:
            params.append({
                'name': target.source.name,
                'type': 'class',
            })

        for param in class_obj.attributes:
            params.append({
                'name': param.name,
                'type': param.attr_type,
            })

        return {
            'class': class_obj.name,
            'documentation': class_obj.documentation,
            'isRoot': root,
            'parameters': params
        }