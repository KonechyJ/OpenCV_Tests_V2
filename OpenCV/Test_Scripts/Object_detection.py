import numpy as np
import cv2

#creates the base image and the template -- loads them as grayscale
img = cv2.resize(cv2.imread('assets/soccer_practice.png', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/ball.png', 0), (0, 0), fx=0.8, fy=0.8)

#sets height and width to the templates shape
h, w = template.shape


#preset methods used to do template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


#runs through all the method in methods above
for method in methods:
    img2 = img.copy()

    #assigns an array of the sections that match the image that we are checking against
    result = cv2.matchTemplate(img2, template, method)

    #returns all the values below.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #checks gives the min or max based on the location
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc


    #draws a rectangle on the matching locations from results
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()