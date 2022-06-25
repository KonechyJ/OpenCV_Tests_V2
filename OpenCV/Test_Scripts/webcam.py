import cv2
import random
import numpy as np



#creates a capture device and assigns it the first webcam available
cap = cv2.VideoCapture(0)

#keeps the camera open while we run this loop
while True:

    #creates the frame
    ret, frame = cap.read()

    #get width and height of video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

    #create an array and fills it with zeros
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    #setting the new smaller image to the smaller cut out
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame



    #shows the feed
    cv2.imshow("frame", image)

    #checks for a key press to break the loop
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()