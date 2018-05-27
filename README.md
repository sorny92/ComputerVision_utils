# ComputerVision_utils
Some facts, libraries, links, etc. Whatever can be useful to use in computer vision and is not straight-forward to realize

## Amazing links:
https://github.com/jbhuang0604/awesome-computer-vision


## How-to install RealSense on Jetson devices
https://github.com/jetsonhacks/buildLibrealsense2TX

## Rpi Gstreamer pipeline without lag to xwindow
### Emiter
```
raspivid -t 0 -h 720 -w 1280 -fps 25 -b 10000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554
```
### Receiver
```
gst-launch-1.0 -v tcpclientsrc host=YOUR_IP port=8554 ! gdpdepay ! rtph264depay ! avdec_h264 ! autovideosink
```

## Rpi pipeline to stream video without lag to opencv
### Emiter
```
raspivid -ih -t 0 -w 1280 -h 720 -fps 25 -o - | nc IP_RECEIVER PORT
```
### Receiver
```
nc -l -p 5000 | ./OPENCV_PROGRAM
```
Inside the program:
```
cap = cv2.VideoCapture("/dev/stdin")
```
