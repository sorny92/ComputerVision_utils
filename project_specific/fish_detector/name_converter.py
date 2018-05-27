import glob
import os
working_folder = 'INSERT FOLDER'
folders_path = glob.glob('{}/*/*'.format(working_folder))

for folder_path in folders_path:
    images_path = glob.glob('{}/*_url*/*'.format(folder_path))
    out_folder_name = '{}/images'.format(working_folder)
    if not os.path.exists(out_folder_name):
        os.makedirs(out_folder_name)
    counter = 0
    for image_path in images_path:
        cls_type = folder_path.split('/')[-2]
        cls = folder_path.split('/')[-1]
        new_path = '{}/{}_{}_{}.jpg'.format(out_folder_name, cls_type, cls, counter)
        print(new_path, cls_type, len(images_path))
        os.rename(image_path, new_path)
        counter +=1