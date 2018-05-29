from subprocess import Popen, PIPE
import os

caffe_root = os.environ['CAFFE_ROOT']

confidence_threshold = 0.3
deploy_file = caffe_root+"/models/SSD_512x512/deploy.prototxt"
caffe_model = caffe_root+"/models/SSD_512x512/snaps/SSD_512_iter_2000.caffemodel"
#this one should have a list of images with it's full path
test_name = "/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images/test_names.txt"


output, err = Popen(["{}/build/examples/ssd/ssd_detect.bin".format(caffe_root),
      "-confidence_threshold={}".format(confidence_threshold),
      deploy_file,
      caffe_model,
      test_name],stdout =PIPE, stderr=PIPE).communicate()


output = output.split('\n')
print(output)