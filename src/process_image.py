import os
import cv2

image_dir = '../images/v1/'
out_dir = '../images/v1/'
filenames = os.listdir(image_dir)

for filename in filenames:
    print(filename)
    img = cv2.imread(image_dir+filename)
    img = cv2.flip(img, -1)
    # img = img[48:-12, 60:-67]
    cv2.imwrite(out_dir+filename, img)
