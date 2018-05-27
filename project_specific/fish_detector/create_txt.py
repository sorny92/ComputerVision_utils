import glob
from random import shuffle

def get_image_path_from_label_path(label_path, images_folder_name='images', label_format='xml', img_format='jpg'):
    image_path = label_path.split('/')
    image_path[-2] = images_folder_name
    image_path[-1] = image_path[-1].replace(label_format, img_format)
    image_path = '/'.join(image_path)
    return image_path

def get_label_path_from_image_path(label_path, labels_folder_name='labels_voc', label_format='xml', img_format='jpg'):
    image_path = label_path.split('/')
    image_path[-2] = labels_folder_name
    image_path[-1] = image_path[-1].replace(img_format, label_format)
    image_path = '/'.join(image_path)
    return image_path

input_train_folders = ['/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images']
input_test_folders = ['']
output_folder = '/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images/'

isRandomTestSet = True
testset_percentage = 0.1

if not isRandomTestSet:
    for input_test_folder in input_test_folders:
        pass

train_data = []
print('There is a total of {} input training folders'.format(len(input_train_folders)))
for input_train_folder in input_train_folders:
    labels_paths = glob.glob('{}/labels_voc/*'.format(input_train_folder))
    if len(labels_paths) == 0:
        raise Exception('ARE YOU SURE THERE IS LABELS IN THE FOLDER {}/labels_voc/ ?'.format(input_train_folder))
    print('There is a total of {} labels in {}'.format(len(labels_paths), input_train_folder))
    for label_path in labels_paths:
        image_path = get_image_path_from_label_path(label_path)
        train_data.append([image_path, label_path])


shuffle(train_data)
if isRandomTestSet:
    test_set = data[:int(len(data)*testset_percentage)]
    train_set = data[int(len(data)*testset_percentage):]
print('The dataset has a total of {} images, splitted across {} training images and {} test images'.format(len(data), len(train_set), len(test_set)))
