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