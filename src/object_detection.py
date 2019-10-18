import os
import time
import matplotlib
matplotlib.use("Pdf")
from gluoncv import model_zoo, data, utils

class ObjectDetection():

    def __init__(self):
        self.classes = ['juice', 'cocacola', 'cocacola-zero']
        self.net = model_zoo.get_model('ssd_512_resnet50_v1_custom', classes=self.classes, pretrained_base=False)
        param_files = ([x for x in os.listdir('.') if x.endswith('.params')])
        selected = param_files[0]
        self.net.load_parameters(selected)

    def detect(self, filename):
        x, img = data.transforms.presets.ssd.load_test(filename, short=512)
        class_IDs, scores, bounding_boxes = self.net(x)
        return class_IDs.asnumpy(), scores.asnumpy(), bounding_boxes.asnumpy()


if __name__ == '__main__':
    objectDetection = ObjectDetection()
    filename = '../images/test/1571183646.821318.jpg'
    start = time.time()
    class_IDs, scores, bounding_boxes = objectDetection.detect(filename)
    end = time.time()
    #print('class_IDs:', class_IDs)
    #print('scores:', scores)
    #print('bounding_boxes:', bounding_boxes)
    print('time:', end-start)
