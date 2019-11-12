ffmpeg -f v4l2 -r 45 -video_size vga -pix_fmt yuv420p12be -i /dev/video0 -b:v 500k -c:v h264_omx -preset ultrafast -an -f flv rtmp://ec2-52-53-216-142.us-west-1.compute.amazonaws.com/live/123456

