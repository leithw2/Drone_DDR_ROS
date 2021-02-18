import rospy
import cv2
import numpy
import std_msgs.msg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from ar_markers import detect_markers

class Reader():
    def __init__(self):
        self.image_sub = rospy.Subscriber("/bebop/camera1/image_raw", Image,self.camera_callback)
        self.bridge = CvBridge()
        return

    def camera_callback(self,data):
        #print "here"

        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

    	except CvBridgeError as e:
    		print(e)
    	(row,cols,channels) = cv_image.shape

    	im = cv_image

        markers = detect_markers(im)
        for marker in markers:
                marker.highlite_marker(im)
                print ("found")
                print rospy.Time.now()
        print (markers)

        # display the result
        cv2.imshow("img", im)

        cv2.waitKey(100)


if __name__ == '__main__':
    rospy.init_node('tag_node', anonymous=False)
    rospy.loginfo('ProgramSTarted_tag_node')
    try:
        reader = Reader()
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")
    cv2.destroyAllWindows()
