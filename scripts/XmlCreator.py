import xml.etree.ElementTree as ET
import os
import utils.LabelConverter as LabelConverter
from PIL import Image
from progress.bar import Bar 

input_test_data = "/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_277.jpg 1 0.603365 118 173 376 284 \n/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_278.jpg 1 0.807335 89 -8 383 354 \n/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_279.jpg 1 0.717453 122 25 438 355 \n/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_427.jpg 1 0.971344 -8 6 504 270 \n/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_280.jpg 1 0.956263 237 152 489 274 \n/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/images/easy_classes_n01497118_280.jpg 1 0.798489 49 79 418 199"

input_file = '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/out.txt'

input_data = open(input_file, 'r').read().split('\n')
bar = Bar('Creating xml files...', max=len(input_data))
for line in input_data[:]:
    bar.next()
    data = line.split(' ')
    label_file_path = LabelConverter.get_label_path_from_image_path(data[0])
    try:
        tree = ET.parse(label_file_path)
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element('annotation')
        tree = ET.ElementTree(root)

        folder = ET.SubElement(root, 'folder')
        folder.text = '/'.join(label_file_path.split('/')[:-1])

        filename = ET.SubElement(root, 'filename')
        filename.text = label_file_path.split('/')[-1]

        source = ET.SubElement(root, 'source')
        ET.SubElement(source, 'database').text = "Selflabeled"

        img = Image.open(data[0])
        width, height = img.size
        if img.mode == 'RGB':
            depth = 3
        else:
            print("IS NOT 3 CHANNEL")
            depth = 1
            continue
        size = ET.SubElement(root, 'size')
        ET.SubElement(size, 'width').text = str(width)
        ET.SubElement(size, 'height').text = str(height)
        ET.SubElement(size, 'depth').text = str(depth)

    label = "fish"
    confidence = float(data[2])
    bbox = [data[3], data[4], data[5], data[6]]
    if confidence > 0.65:
        LabelConverter.addObject(root, label, bbox)
        tree.write(label_file_path)
bar.finish()