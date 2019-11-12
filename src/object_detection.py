import os
import cv2
import time
import numpy as np
#import matplotlib  # only on raspberry pi
#matplotlib.use("Pdf")  # only on raspberry pi
import mxnet as mx
from gluoncv import model_zoo, data, utils

class ObjectDetection():
    def __init__(self, param_file=None):
        self.classes = ['cola', 'juice', 'noodles', 'hand']
        #self.net = model_zoo.get_model('ssd_512_resnet50_v1_custom', classes=self.classes, pretrained_base=False)
        self.net = model_zoo.get_model('yolo3_darknet53_custom', classes=self.classes, pretrained_base=False)
        if param_file is None:
            param_files = ([x for x in os.listdir('.') if x.endswith('.params')])
            selected = param_files[-1]
            param_file = selected
            print('Loaded from params file: ', selected)
        self.net.load_parameters(param_file)
        self.ctx = mx.gpu(0)
        self.net.collect_params().reset_ctx(self.ctx)
        self.net.set_nms(nms_thresh=0.3, nms_topk=20, post_nms=10)  # max objects 20
        self.net.hybridize(static_alloc=True, static_shape=True)

    def detect(self, filename):
        # x, img = data.transforms.presets.ssd.load_test(filename, short=512)
        # x, img = data.transforms.presets.ssd.transform_test([mx.nd.array(cv2.imread(filename))], short=512)
        img = cv2.imread(filename)
        img = cv2.resize(img, (512, 512))
        x = self.transform_image(img)
        class_IDs, scores, bounding_boxes = self.net(x.as_in_context(self.ctx))
        return class_IDs.asnumpy(), scores.asnumpy(), bounding_boxes.asnumpy()
    
    def detect_image(self, img):
        x, img = data.transforms.presets.yolo.transform_test([mx.nd.array(img)], short=512)
        class_IDs, scores, bounding_boxes = self.net(x.as_in_context(self.ctx))
        return class_IDs.asnumpy(), scores.asnumpy(), bounding_boxes.asnumpy()

    def transform_image(self, image):
        image = np.array(image) - np.array([123., 117., 104.])
        image /= np.array([58.395, 57.12, 57.375])
        image = image.transpose((2, 0, 1))
        image = image[np.newaxis, :]
        return mx.nd.array(image)

if __name__ == '__main__':
    objectDetection = ObjectDetection()
    filename = '../images/v1/test/frame_1571435703.4214327.jpg'
    start = time.time()
    class_IDs, scores, bounding_boxes = objectDetection.detect(filename)
    end = time.time()
    #print('class_IDs:', class_IDs)
    #print('scores:', scores)
    #print('bounding_boxes:', bounding_boxes)
    print('time:', end-start)
