import xml.etree.ElementTree as ET


def parse_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    object_list = []
    dataset_dict = {}

    for child in root:
        if child.tag == 'filename':
            dataset_dict['file_name'] = child.text
        if child.tag == 'object':
            object_dict = {}
            for sub in child:
                if sub.tag == 'name':
                    object_dict['name'] = sub.text
                if sub.tag == 'bndbox':
                    bndbox_coordinates = []
                    for bndbox in sub:
                        bndbox_coordinates.append(bndbox.text)
                    object_dict['coordinates'] = bndbox_coordinates
            object_list.append(object_dict)
    dataset_dict['object'] = object_list

    return dataset_dict
