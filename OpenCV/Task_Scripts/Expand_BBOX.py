import cv2
import numpy as np

path = r'C:\Users\C21941\PycharmProjects\Open_CV_Tests3\assets\cats.jpg'
img = cv2.imread(path)
canvas = img.copy()

## set and crop the ROI
x,y,w,h = bbox = (200, 300, 200, 200)

#            (Image, Start Point, End point, color, line thickness)
cv2.rectangle(canvas, (x,y), (x+w,y+h), (0,0,255), 2)
cropped = img[y:y+h, x:x+w]
cv2.imshow("cropped", cropped)

## get the center and the radius
cx = x+w//2
cy = y+h//2
cr = max(w,h)//2

## set offset, repeat enlarger ROI
dr = 10
for i in range(0,4):
    r = cr+i*dr
    cv2.rectangle(canvas, (cx-r, cy-r), (cx+r, cy+r), (0,255,0), 1)

cv2.imshow("source", canvas)
cv2.waitKey()
cv2.destroyAllWindows()

