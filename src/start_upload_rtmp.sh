ffmpeg -f v4l2 -r 24 -video_size vga -pix_fmt yuv420p12be -i /dev/video0 -b:v 500k -c:v h264_omx -preset ultrafast -an -f flv rtmp://52.80.130.52/live/123456

