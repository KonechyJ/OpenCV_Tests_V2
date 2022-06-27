import numpy as np
import cv2
import random

class BoundingBox:
    def __init__(self, x, y, width, height, myArray):
        self.x = x
        self.age = y
        self.width = width
        self.height = height
        self.myArray = myArray


    def checkTarget(self, myArray):

        StephArray = [random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)]
        for x in myArray:
            if StephArray[0] != myArray[0]:
                break
        if myArray == StephArray:
            print("Match")
            print(StephArray)
            print(myArray)
        else:
            print("different")
            print(StephArray)
            print(myArray)




input_video_file = "../../assets/video_116.mp4"
cap = cv2.VideoCapture(input_video_file)

givenArray = []

for i in range(4):
    givenArray.append(i)

while True:
    ret, frame = cap.read()
    B1 = BoundingBox(10, 40, 20, 20, givenArray)
    B1.checkTarget(givenArray)
    print("_____________")

    # ======================================================
    # maybe create a condition that randomly sends an array.
    # ======================================================

#add values to tuples: https://datagy.io/python-append-to-tuple/#:~:text=While%20Python%20tuples%20don%E2%80%99t%20offer%20a%20dedicated%20method,operator%2C%20which%20allows%20us%20to%20combine%20two%20tuples.

