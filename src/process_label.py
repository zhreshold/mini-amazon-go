import os
import cv2

image_dir = '../images/v2/'
out_dir = '../images/v4/'
filenames = os.listdir(image_dir)

for filename in filenames:
    print(filename)
    if filename.endswith('.xml'):
        fout = open(out_dir+filename, 'w')
        with open(image_dir+filename) as fin:
            while True:
                line = fin.readline()
                if not line:
                    break
                line = line.strip().replace('cocacola-zero', 'cocacola')
                fout.write(line+'\n')
        fout.close()
    elif filename.endswith('.jpg'):
        os.system('cp '+image_dir+filename+' '+out_dir+filename)
