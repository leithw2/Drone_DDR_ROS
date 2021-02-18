#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import numpy as np
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("/cv_camera/image_raw",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)
    cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape

    frame = cv_image

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_red = np.array([150,150,0])
    upper_red = np.array([200,255,255])

    # Threshold the HSV image to get only Red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #res = cv2.imread('./src/image_processing/codes/home.png')
    #time.sleep(5)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)

    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    img, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = frame
    img = cv2.drawContours(frame,contours, -1, (255,255,0), 3)
    for cnt in contours:

        area = cv2.contourArea(cnt)
        if area >= 300:
            x,y,w,h = cv2.boundingRect(cnt)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            print (area)
            print ()
        else:
            img=frame

    cv2.imshow('Contornos',img)
    cv2.waitKey(1)

    try:
      pass
      #self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main():
  image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()

  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
