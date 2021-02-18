#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from cv_bridge import CvBridge, CvBridgeError


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)

        self.vel = 1
        l_x = 125
        l_y = 400
        r_x = 125 +500
        r_y = 400
        button_size_w = 50
        button_size_h = 50

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, -100, 1280, 720))

        self.image = None

        self.pushButton_f = QtWidgets.QPushButton(Dialog)
        self.pushButton_f.setGeometry(QtCore.QRect(l_x, l_y, button_size_w, button_size_h))
        self.pushButton_f.setObjectName("pushButton")
        self.pushButton_f.setText("FRW")

        self.pushButton_b = QtWidgets.QPushButton(Dialog)
        self.pushButton_b.setGeometry(QtCore.QRect(l_x, l_y+100, button_size_w, button_size_h))
        self.pushButton_b.setObjectName("pushButton")
        self.pushButton_b.setText("BACK")

        self.pushButton_r = QtWidgets.QPushButton(Dialog)
        self.pushButton_r.setGeometry(QtCore.QRect(l_x+50, l_y+50, button_size_w, button_size_h))
        self.pushButton_r.setObjectName("pushButton")
        self.pushButton_r.setText("RIGHT")

        self.pushButton_l = QtWidgets.QPushButton(Dialog)
        self.pushButton_l.setGeometry(QtCore.QRect(l_x-50, l_y+50, button_size_w, button_size_h))
        self.pushButton_l.setObjectName("pushButton")
        self.pushButton_l.setText("LEFT")


        self.pushButton_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_up.setGeometry(QtCore.QRect(r_x, r_y, button_size_w, button_size_h))
        self.pushButton_up.setObjectName("pushButton")
        self.pushButton_up.setText("UP")

        self.pushButton_down = QtWidgets.QPushButton(Dialog)
        self.pushButton_down.setGeometry(QtCore.QRect(r_x, r_y+100, button_size_w, button_size_h))
        self.pushButton_down.setObjectName("pushButton")
        self.pushButton_down.setText("DOWN")

        self.pushButton_yaw_r = QtWidgets.QPushButton(Dialog)
        self.pushButton_yaw_r.setGeometry(QtCore.QRect(r_x+50, r_y+50, button_size_w, button_size_h))
        self.pushButton_yaw_r.setObjectName("pushButton")
        self.pushButton_yaw_r.setText("Turn.R")

        self.pushButton_yaw_l = QtWidgets.QPushButton(Dialog)
        self.pushButton_yaw_l.setGeometry(QtCore.QRect(r_x-50, r_y+50, button_size_w, button_size_h))
        self.pushButton_yaw_l.setObjectName("pushButton")
        self.pushButton_yaw_l.setText("Turn.L")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_f.clicked.connect(self.to_forward)
        self.pushButton_b.clicked.connect(self.to_backward)
        self.pushButton_l.clicked.connect(self.to_left)
        self.pushButton_r.clicked.connect(self.to_right)

        self.pushButton_up.clicked.connect(self.to_up)
        self.pushButton_down.clicked.connect(self.to_down)
        self.pushButton_yaw_l.clicked.connect(self.to_yaw_left)
        self.pushButton_yaw_r.clicked.connect(self.to_yaw_right)

        self.cmc_vel_pub = rospy.Publisher("/turtle1/cmd_vel",Twist)
        self.vel_msg = Twist()
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)


    def callback(self,data):
      try:
        cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
      except CvBridgeError as e:
        print(e)

      (rows,cols,channels) = cv_image.shape
      #self.centerx = int(cols/2)

      frame = cv_image
      self.image = QtGui.QImage(frame,frame.shape[1],frame.shape[0],frame.shape[1] * 3,QtGui.QImage.Format_RGB888)
      self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def to_forward(self):
        print("FordWard!")
        self.vel_msg.linear.x = self.vel
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0

        self.cmc_vel_pub.publish(self.vel_msg)

    def to_backward(self):
        print("BackWard!")
        self.vel_msg.linear.x = - self.vel
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0

        self.cmc_vel_pub.publish(self.vel_msg)

    def to_left(self):
        print("Left!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y =  self.vel
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.cmc_vel_pub.publish(self.vel_msg)

    def to_right(self):
        print("Right!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = - self.vel
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0

        self.cmc_vel_pub.publish(self.vel_msg)

    def to_up(self):
        print("Up!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z =  self.vel
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.cmc_vel_pub.publish(self.vel_msg)

    def to_down(self):
        print("Down!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = - self.vel
        self.vel_msg.angular.x= 0
        self.vel_msg.angular.y= 0
        self.vel_msg.angular.z= 0

        self.cmc_vel_pub.publish(self.vel_msg)

    def to_yaw_left(self):
        print("Yaw_Left!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z =  0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = self.vel

        self.cmc_vel_pub.publish(self.vel_msg)

    def to_yaw_right(self):
        print("Yaw_Right!")
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = - self.vel

        self.cmc_vel_pub.publish(self.vel_msg)

if __name__ == "__main__":
    import sys

    rospy.init_node('qt_node', anonymous=True)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
