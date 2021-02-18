#!/usr/bin/env python
import cv2
import glob
import qrcode
# initialize the cv2 QRCode detector
#image = cv2.imread("testQRCode-1.png")
for filename in sorted(glob.glob("images/*")):

    print (filename)
    im = cv2.imread(filename)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

detector = cv2.QRCodeDetector()

# example data
data = "https://www.twitch.tv/indiegen_william.com"
# output file name
filename = "images/Twitch.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

while True:
    img = im

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)

    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # draw all lines
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

        if data:
            print("[+] QR Code detected, data:", data)

    # display the result
    cv2.imshow("img", img)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
