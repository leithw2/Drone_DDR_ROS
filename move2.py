import rospy
import tf
import math
import numpy as np
import std_msgs.msg
import keyboard
from geometry_msgs.msg import Transform, Quaternion, Point, Twist, Pose

class Controller():
    def __init__(self):
        self.pose_pub = rospy.Publisher('/bebop/command/control', Pose,queue_size=1)
        self.pose = Pose()
        self.r = rospy.Rate(10)
        return

    def send(self,x,y,z,xq,yq,zq,wq):

        self.pose = Pose(Point(x,y,z), Quaternion(xq,yq,zq,wq))
        self.pose_pub.publish(self.pose)
        self.r.sleep()

        return

if __name__ == '__main__':
    rospy.init_node('Pose_controller', anonymous=False)
    rospy.loginfo('ProgramSTarted')
    poseControl = Controller()
    x=0
    y=0
    z=0

    while not rospy.is_shutdown():
        x = input("Please enter a x:\n")
        y = input("Please enter a y:\n")
        z = input("Please enter a z:\n")

        poseControl.send(x,y,z,0,0,0,0)
