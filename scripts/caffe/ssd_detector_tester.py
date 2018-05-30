from subprocess import Popen, PIPE
import os
import cv2

caffe_root = os.environ['CAFFE_ROOT']

confidence_threshold = 0.3
deploy_file = caffe_root+"/models/SSD_512x512/deploy.prototxt"
caffe_model = caffe_root+"/models/SSD_512x512/snaps/SSD_512_iter_2000.caffemodel"
#this one should have a list of images with it's full path
test_name = "/media/esteve/1615F2A532ED483C/Ubuntu/ML/fish_dataset/imagenet_dataset/imagenet_split_renamed/labeled_images/test_names.txt"


output = Popen(["{}/build/examples/ssd/ssd_detect.bin".format(caffe_root),
      "-confidence_threshold={}".format(confidence_threshold),
      deploy_file,
      caffe_model,
      test_name],stdout =PIPE)

for line in output.stdout:
      data = line.decode().split(' ')
      img = cv2.imread(data[0])
      cv2.rectangle(img, (int(data[3]), int(data[4])), (int(data[5]), int(data[6])), (255,0,0))
      cv2.imshow("image", img)
      
      cv2.waitKey(500)
      
