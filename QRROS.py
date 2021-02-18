import rospy
import cv2
import numpy
import qrcode
import std_msgs.msg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Reader():
    def __init__(self):
        self.image_sub = rospy.Subscriber("/bebop/camera1/image_raw", Image,self.camera_callback)
        self.bridge = CvBridge()
        self.detector = cv2.QRCodeDetector()
        return

    def camera_callback(self,data):
        #print "here"
        global i
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

    	except CvBridgeError as e:
    		print(e)
    	(row,cols,channels) = cv_image.shape

    	img = cv_image
        self.detector = cv2.QRCodeDetector()
        data, bbox, _ = self.detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            #for i in range(len(bbox)):
                # draw all lines
                #cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

            if data:
                print("[+] QR Code detected, data:", data)
                print("[+] QR Code detected, data:", bbox)
                print rospy.Time.now()

        # display the result
        cv2.imshow("img", img)

        cv2.waitKey(100)


if __name__ == '__main__':
    rospy.init_node('QR_node', anonymous=False)
    rospy.loginfo('ProgramSTarted_QR_node')
    try:
        reader = Reader()
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")
    cv2.destroyAllWindows()
