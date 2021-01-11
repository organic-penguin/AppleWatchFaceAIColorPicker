import numpy as np
import cv2
import pandas as pd
import os
import time

colorIndex=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('include/colors.csv', names=colorIndex, header=None)

def getColorName(H,S,V):
	S = S/255
	V = V/255
	if(V < .15):
		generalColor = "Black"
	elif(V < .30):
		generalColor = "Grey"
	elif(S < .1):
		generalColor = "White"
	elif(0 < H < 20):
                generalColor = "Red"
	elif(21 < H < 50):
		generalColor = "Orange"
	elif(51 < H < 65):
		generalColor = "Yellow"
	elif(66 < H < 160):
		generalColor = "Green"
	elif(161 < H  < 256):
		generalColor = "Blue"
	elif(257 < H < 295):
		generalColor = "Purple"
	elif(296 < H < 342):
		generalColor = "Pink"
	elif(295 < H):
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

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Color sampling point (Takes the face identification X and Y and adds additional pixels for sampling what shirt color you're wearing
    shirtSamplePointX = x + 40
    shirtSamplePointY = y + 130

    h, s, v = imgHSV[shirtSamplePointX, shirtSamplePointY]

    cv2.rectangle(img, (shirtSamplePointX, shirtSamplePointY), (shirtSamplePointX + 5, shirtSamplePointY + 5),
                  (0, 150, 255), 1)
    h = int(h)
    s = int(s)
    v = int(v)
    print("HSV values = ", h, s/255, v/255)
    generalName = getColorName(h, s, v)
    #cnamePost = getColorName(h, s, v)[1]
    print("Generalized Color Name = ", generalName)
    #print("CNAME is " + cnamePost)

    hsv = str(h) + "," + str(s) + "," + str(v)
    cv2.imwrite("openCVImage.png", img)
    jsonFile = open("index.html", "w")
    jsonFile.write(
        "{\"generalColor\": \"" + generalName + "\", \"BGR\": \"" + hsv + "\"}")
    jsonFile.close()
#    time.sleep(1)
  #  os.popen("git add index.html openCVImage.png --force")
 #   time.sleep(1)
   # os.popen("git commit -m \"Adding todays colors\"")
#    time.sleep(1)
 #   os.popen("git push origin main:myColorForToday")
  #  time.sleep(1)

