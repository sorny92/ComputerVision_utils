import os
import sys
import glob
sys.path.insert(0, '/home/esteve/ComputerVision_utils/scripts')
import XmlObjectFinder

input_folder = '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed'
out_folder_name = '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images'
labels_paths = glob.glob('{}/labels_yolo/*'.format(input_folder))

os.makedirs(out_folder_name)
os.makedirs('{}/images/'.format(out_folder_name))
os.makedirs('{}/labels_voc/'.format(out_folder_name))
for label_path in labels_paths:
    image_path = label_path.split('/')
    image_path[-2] = 'images'
    image_path[-1] = image_path[-1].replace('xml', 'jpg')
    image_path = '/'.join(image_path)
    os.rename(image_path, '{}/images/{}'.format(out_folder_name, image_path.split('/')[-1]))
    os.rename(label_path, '{}/labels_voc/{}'.format(out_folder_name, label_path.split('/')[-1]))
    #os.rename(image_path)
    #os.rename(label_path)
