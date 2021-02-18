#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

from cv_bridge import CvBridge, CvBridgeError
class ORB_detector:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows,cols,channels) = cv_image.shape
        self.centerx = int(cols/2)

        frame = cv_image
        #percent by which the image is resized
        scale_percent = 50

        #calculate the 50 percent of original dimensions
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        frame = cv2.resize(frame, dsize)
        cv2.imshow('res',self.getDescriptors(frame))
        cv2.waitKey(2)

        #create orb
        self.orb = cv2.ORB_create(nfeatures=200)

    def getDescriptors(self, img):
        #create orb
        orb = cv2.ORB_create(nfeatures=200)

        # find keypoints ORB
        kp = orb.detect(img,None)

        # compute descriptors ORB
        kp, des = orb.compute(img, kp)

        img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)

        return(img2)

    def getPrediction(self, model, image):
        des = getDescriptors(image)

        probs = model.predict_proba(des)

        sumProb = np.sum(probs, axis = 0)

        prob = [x / len(probs) for x in sumProb]
        return prob

def main(args):
  ic = ORB_detector()
  rospy.init_node('ORB_detector', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
