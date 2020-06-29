# importing required packages

from imutils.video import VideoStream
import numpy as np
import time
import cv2

# let's capture the background before had for acquisition
# creating an object for videoStream

print("[INFO] Creating object for VideoStream...")
vs = VideoStream(src=0).start()
time.sleep(2)

# capturing background 
# initializing background as None / 0
background = 0

# initializing webCam for background capture
#vs.start()
print("[INFO] Capturing background frames...")
for i in range(30):
    background = vs.read()
#vs.stop()
print("[INFO] Background Captured...")

# laterally inverting / flipping the image
background = np.flip(background, axis=1)

# let's detect the required color on the cloth to make it invisible
print("[INFO] We are going Live...")
#vs.start()
#time.sleep(2)
while True:

    frame = vs.read()
    frame = np.flip(frame, axis=1)

    # converting BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # the range for lower red

    lowerRed = np.array([0, 120, 70])
    upperRed = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lowerRed, upperRed)

    # range for upper red
    lowerRed = np.array([170, 120, 70])
    upperRed = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lowerRed, upperRed)

    # generating final mask to detect red color
    mask = mask1 + mask2

    # let's begin segmenting the cloth from the frames

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # creating an inverted mask to segment out the cloth from the frame
    mask_invert = cv2.bitwise_not(mask)

    # segmenting the cloth out of frame
    res_frame = cv2.bitwise_and(frame, frame, mask=mask_invert)

    # computing resulted image
    res_frame2 = cv2.bitwise_and(background, background, mask=mask)
    final_frame = cv2.addWeighted(res_frame, 1, res_frame2, 1, 0)

    # displaying the frame

    cv2.imshow("Invisibility:", final_frame)
    key = cv2.waitKey(1) & 0xFF

    # quit if user interrupts with 'q'
    if key == 'q':
        break

print("[INFO] Good_Bye...")
# cleanUp
cv2.destroyAllWindows()
vs.stop()

