import numpy as np
import cv2
import os
import time
from subprocess import Popen, PIPE

directory = os.getcwd()

def getColorName(H,S,V):
        S = S/255
        V = V/255
        if(V <= .15):
                generalColor = "Black"
        elif(.16 <= S <= 70 and V <= .60 and 70 >= H <= 40):
                generalColor = "Grey"
        elif(S <= .15 and V >= .6):
                generalColor = "White"
        elif(1 <= H <= 20):
                generalColor = "Red"
        elif(21 <= H <= 25):
                generalColor = "Orange"
        elif(26 <= H <= 32):
                generalColor = "Yellow"
        elif(33 <= H <= 89):
                generalColor = "Green"
        elif(90 <= H  <= 126):
                generalColor = "Blue"
        elif(127 <= H <= 148):
                generalColor = "Purple"
        elif(149 <= H <= 165):
                generalColor = "Pink"
        elif(166 <= H <= 180):
                generalColor = "Red"
        else:
                generalColor = "Other"
        return generalColor

#Capture an image from your camera then save as an image to reuse later and single frame processing (save resources)
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cv2.imwrite("openCVImage.png", frame)
img = cv2.imread("openCVImage.png")
cam.release
#import Face Cascades (Prebuilt identification of faces)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Convert to grayscale and HSV (HSV is used to identify Hue for color)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Face detection settings
faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

#If faces are empty 
if faces == ():
        jsonFile = open("/var/www/html/index.html", "w")
        jsonFile.write("{\"generalColor\": \"" + "Empty"  + "\", \"HSV\": \"" + "0,0,0" + "\"}")
        jsonFile.close()


for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #Three shirt sampling points
        firstShirtSamplePointX = x + 40
        firstShirtSamplePointY = (y + h) + 100

        secondShirtSamplePointX = firstShirtSamplePointX - 10
        secondShirtSamplePointY = firstShirtSamplePointY + 5

        thirdShirtSamplePointX = firstShirtSamplePointX + 10
        thirdShirtSamplePointY = firstShirtSamplePointY - 5


        h, s, v = imgHSV[firstShirtSamplePointX, firstShirtSamplePointY]
        h1 = int(h)
        s1 = int(s)
        v1 = int(v)

        h, s, v = imgHSV[secondShirtSamplePointX, secondShirtSamplePointY]
        h2 = int(h)
        s2 = int(s)
        v2 = int(v)

        h, s, v = imgHSV[thirdShirtSamplePointX, thirdShirtSamplePointY]
        h3 = int(h)
        s3 = int(s)
        v3 = int(v)

        cv2.rectangle(img, (firstShirtSamplePointX, firstShirtSamplePointY), (firstShirtSamplePointX + 5, firstShirtSamplePointY + 5),
                  (0, 0, 255), 1)
        cv2.rectangle(img, (secondShirtSamplePointX, secondShirtSamplePointY), (secondShirtSamplePointX + 5, secondShirtSamplePointY + 5),
                  (0, 0, 255), 1)
        cv2.rectangle(img, (thirdShirtSamplePointX, thirdShirtSamplePointY), (thirdShirtSamplePointX + 5, thirdShirtSamplePointY + 5),
                  (0, 0, 255), 1)

        h = (h1 + h2 + h3)/3
        s = (s1 + s2 + s3)/3
        v = (v1 + v2 + v3)/3

        generalName = getColorName(h, s, v)
        print("HSV values = ", h, s/255, v/255, " and Generalize Color Name = ", generalName)

        hsv = str(h) + "," + str(s/255) + "," + str(v/255)
        cv2.imwrite("openCVImage.png", img)
        jsonFile = open("/var/www/html/index.html", "w")
        jsonFile.write(
            "{\"generalColor\": \"" + generalName + "\", \"HSV\": \"" + hsv + "\"}")
        jsonFile.close()
