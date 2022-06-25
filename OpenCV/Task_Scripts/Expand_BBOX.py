import cv2
import copy
import numpy as np



#======================================================
# maybe delete the cropped fucntion and replace it
# with a command to expand the bounding box on command?
#======================================================




## Read and copy
img = cv2.imread("assets/cat.jpg")
canvas = copy.copy(img)

## set and crop the ROI
x,y,w,h = bbox = (180, 100, 50, 100)
cv2.rectangle(canvas, (x,y), (x+w,y+h), (0,0,255), 2)
croped = img[y:y+h, x:x+w]
cv2.imshow("cropped", croped)

## get the center and the radius
cx = x+w//2
cy = y+h//2
cr  = max(w,h)//2

## set offset, repeat enlarger ROI
dr = 10
for i in range(0,4):
    r = cr+i*dr
    cv2.rectangle(canvas, (cx-r, cy-r), (cx+r, cy+r), (0,255,0), 1)
    croped = img[cy-r:cy+r, cx-r:cx+r]
    cv2.imshow("cropped{}".format(i), croped)

## display
cv2.imshow("source", canvas)
cv2.waitKey()
cv2.destroyAllWindows()

#https://stackoverflow.com/questions/47580887/adjust-size-and-position-of-bounding-boxes-while-keeping-it-somewhat-centered