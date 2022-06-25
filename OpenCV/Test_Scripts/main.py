import cv2
import random
import numpy as np

#sets the image
img = cv2.imread("assets/logo.png")
#resize image
img = cv2.resize(img, (1100, 1100))
#roatate image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

#  -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of the image will be neglected. it is the default
#   0, cv2.IMREAD_GRAYSCALE : Loads a image in grayscale mode
#   1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

#shows the image
cv2.imshow('Image', img)

#store a new image
cv2.imwrite("new_img.jpg", img)


#makes the prgrom wait for a command indefintiely
cv2.waitKey(0)

#closes down
cv2.destroyAllWindows()

#=================================================================================================
#=================================================================================================
#=================================================================================================

#shows an array of image values for specific points
print(img)

#prints the height, width, and channels of the object
# ex) (995, 1000, 3)
print(img.shape)

#look at the first row of an image
print(img[0])

#loop through the firsr 100 rows on image pixels

for i in range(266):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255) ]

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#copeies a part of the img from the specified bounds
tag = img[500:700, 600:900]

#assigned the cut out image to the assigned place
img[100:300, 650:950] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#=================================================================================================
#=================================================================================================
#=================================================================================================

