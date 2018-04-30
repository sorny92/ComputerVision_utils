# ComputerVision_utils
Some facts, libraries, links, etc. Whatever can be useful to use in computer vision and is not straight-forward to realize


## Rpi Gstreamer pipeline without lag
### Emiter
```
raspivid -t 0 -h 720 -w 1280 -fps 25 -b 10000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554
```
### Receiver
```
gst-launch-1.0 -v tcpclientsrc host=YOUR_IP port=8554 ! gdpdepay ! rtph264depay ! avdec_h264 ! autovideosink
```
