import xml_parser
import cv2
import math
import shutil
import xml.etree.ElementTree as ET
import random
import numpy as np

# if len(sys.argv) != 2:
#     raise "exact two arguments needed"
#
# img_path = sys.argv[0]
# xml_path = sys.argv[1]

foo = 20
img_path = f'images/{foo}.jpg'
xml_path = f'annotations_temp/{foo}.xml'
temp = xml_parser.parse_xml(xml_path)
tr = 1.5

for i in enumerate(temp['object']):
    for j in enumerate(temp['object']):
        if i == j:
            break
        else:
            src = i[0]
            target = j[0]
            random_name = random.randint(170, 999)
            img_path_new = f'augmented_images/{foo}/'
            img_name = img_path_new + str(random_name) + ".jpg"
            xml_path_new = f'augmented_xml/{foo}/'
            xml_name = str(random_name) + ".xml"

            src_name = temp['object'][src]['name']
            src_x1, src_y1, src_x2, src_y2 = temp['object'][src]['coordinates']
            target_name = temp['object'][target]['name']
            target_x1, target_y1, target_x2, target_y2 = temp['object'][target]['coordinates']
            src_area = math.trunc((math.sqrt((int(src_x2) - int(src_x1)) ^ 2 + (int(src_y2) - int(src_y1)) ^ 2)) *
                                  (math.sqrt((int(src_x2) - int(src_x1)) ^ 2 + (int(src_y2) - int(src_y1)) ^ 2)))

            target_area = math.trunc(
                (math.sqrt((int(target_x2) - int(target_x1)) ^ 2 + (int(target_y2) - int(target_y1)) ^ 2)) *
                (math.sqrt((int(target_x2) - int(target_x1)) ^ 2 + (int(target_y2) - int(target_y1)) ^ 2)))

            # if (abs(src_area - target_area)) / 100 <= tr:
            img = cv2.imread(img_path)
            img_copy = img.copy()

            # y1 y2 x1 x2
            # row columns
            src_block = img_copy[int(src_y1):int(src_y2), int(src_x1):int(src_x2)]
            target_block = img_copy[int(target_y1):int(target_y2), int(target_x1):int(target_x2)]

            resized_src_block = cv2.resize(src_block, dsize=(target_block.shape[1], target_block.shape[0]),
                                           interpolation=cv2.INTER_NEAREST)

            resized_target_block = cv2.resize(target_block, dsize=(src_block.shape[1], src_block.shape[0]),
                                              interpolation=cv2.INTER_AREA)

            img_copy[int(target_y1):int(target_y2), int(target_x1):int(target_x2)] = resized_src_block
            img_copy[int(src_y1):int(src_y2), int(src_x1):int(src_x2)] = resized_target_block

            cv2.imwrite(img_name, img_copy)

            modified_xml_path = 'annotations_temp/10_modified.xml'
            shutil.copyfile(xml_path, modified_xml_path)

            tree = ET.parse(modified_xml_path)
            root = tree.getroot()

            for object in root.findall('object'):
                xmin, ymin, xmax, ymax = object[4][0].text, object[4][1].text, object[4][2].text, object[4][3].text
                if src_x1 == xmin and src_y1 == ymin and src_x2 == xmax and src_y2 == ymax:
                    object[0].text = target_name
                elif target_x1 == xmin and target_y1 == ymin and target_x2 == xmax and target_y2 == ymax:
                    object[0].text = src_name
            xml_path = xml_path_new + xml_name
            tree.write(xml_path)

            # else:
            #     print('area bigger than threshold')
