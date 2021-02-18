import rospy
import tf
import math
import numpy as np
import std_msgs.msg
from geometry_msgs.msg import Transform, Quaternion, Point, Twist
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint

class Trajectory():
    def __init__(self):
        self.traj_pub = rospy.Publisher('/bebop/command/trajectory', MultiDOFJointTrajectory,queue_size=1)
        self.traj = MultiDOFJointTrajectory()
        self.r = rospy.Rate(1)
        return

    def update(self):
        self.traj.header.frame_id =''
        self.traj.header.stamp = rospy.Time.now()
        self.traj.joint_names = ["base_link"]

        transforms =Transform()
        transforms.translation.x = 0.0
        transforms.translation.y = 0.0
        transforms.translation.z = 1.0
        velocities =Twist()
        accelerations=Twist()
        point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accelerations],rospy.Duration(0.1))
        self.traj.points.append(point)
        self.traj_pub.publish(self.traj)
        self.r.sleep()

        return

if __name__ == '__main__':
    rospy.init_node('Trajectory_Test', anonymous=False)
    rospy.loginfo('ProgramSTarted')
    trajectory = Trajectory()

    while not rospy.is_shutdown():
        trajectory.update()
