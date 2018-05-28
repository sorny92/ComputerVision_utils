import glob
from random import shuffle
from PIL import Image
from progress.bar import Bar 
import sys
import os
sys.path.insert(0, 'scripts')
import utils.LabelConverter as LabelConverter
from subprocess import call

input_train_folders = ['/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images']
input_test_folders = ['']
output_folder = '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images'
label_map_path= '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images/label_map.prototxt'

isRandomTestSet = True
testset_percentage = 0.1

if not isRandomTestSet:
    for input_test_folder in input_test_folders:
        pass

train_data = []
bar = Bar('Processing input folders', max=len(input_train_folders))
for input_train_folder in input_train_folders:
    bar.next()
    labels_paths = glob.glob('{}/labels_voc/*'.format(input_train_folder))
    if len(labels_paths) == 0:
        raise Exception('ARE YOU SURE THERE IS LABELS IN THE FOLDER {}/labels_voc/ ?'.format(input_train_folder))
    bar2 = Bar('Processing labels in {}'.format(input_train_folder), max=len(labels_paths))
    for label_path in labels_paths:
        image_path = LabelConverter.get_image_path_from_label_path(label_path)
        train_data.append([image_path, label_path])
        bar2.next()
    bar2.finish()
bar.finish()


shuffle(train_data)
if isRandomTestSet:
    test_set = train_data[:int(len(train_data)*testset_percentage)]
    train_set = train_data[int(len(train_data)*testset_percentage):]
print('The dataset has a total of {} images, splitted across {} training images and {} test images'.format(len(train_data), len(train_set), len(test_set)))

train_file = open('{}/train.txt'.format(output_folder), 'w')
test_file = open('{}/test.txt'.format(output_folder), 'w')
test_names_file = open('{}/test_names.txt'.format(output_folder), 'w')

bar = Bar('Writing train dataset', max=len(train_set))
for line in train_set:
    train_file.write('{} {}\n'.format('/'.join(line[0].split('/')[-3:]), '/'.join(line[1].split('/')[-3:])))
    bar.next()
bar.finish()
bar = Bar('Writing test dataset', max=len(test_set))
for line in test_set:
    test_file.write('{} {}\n'.format('/'.join(line[0].split('/')[-3:]), '/'.join(line[1].split('/')[-3:])))
    width, height = Image.open(line[0]).size
    test_names_file.write('{} {} {}\n'.format('/'.join(line[0].split('/')[-3:]), width, height))
    bar.next()
bar.finish()
train_file.close()
test_file.close()

caffe_root = os.environ['CAFFE_ROOT']
if not len(caffe_root):
    raise Exception('Have you declared CAFFE_ROOT in your environment?')
call(["{}/build/tools/convert_annoset".format(caffe_root), 
      "-anno_type=detection", 
      "-check_label",  
      "-encode_type=jpg",  
      "-encoded", 
      "-label_map_file={}".format(label_map_path),
      "-shuffle",
      '{}/'.format('/'.join(input_train_folders[0].split('/')[:-1])),
      "{}/train.txt".format(output_folder),
      "{}/train_db".format(output_folder)])

call(["{}/build/tools/convert_annoset".format(caffe_root), 
      "-anno_type=detection", 
      "-check_label",  
      "-encode_type=jpg",  
      "-encoded", 
      "-label_map_file={}".format(label_map_path),
      "-shuffle",
      '{}/'.format('/'.join(input_train_folders[0].split('/')[:-1])),
      "{}/test.txt".format(output_folder),
      "{}/test_db".format(output_folder)])