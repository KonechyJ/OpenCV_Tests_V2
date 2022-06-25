import numpy as np
import cv2

img = cv2.imread('assets/logo.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)


for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 2, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = [int(x) for x in np.random.randint(0, 255, size=3)]
        cv2.line(img, corner1, corner2, (), 1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()