import cv2
import copy
import numpy as np


#======================================================
# maybe delete the cropped fucntion and replace it
# with a command to expand the bounding box on command?
#======================================================



image = cv2.imread('assets/shapes.png')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


ROI_number = 0
counts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
counts = counts[0] if len(counts) == 2 else counts[1]
for c in counts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)



cv2.imshow('image', image)
cv2.waitKey()



#https://stackoverflow.com/questions/47580887/adjust-size-and-position-of-bounding-boxes-while-keeping-it-somewhat-centered
#expand bounding box using ROI in opencv: https://stackoverflow.com/questions/54249517/python-file-write-all-the-bounding-box-coordinates-using-opencv