import numpy as np
import cv2


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

#Capture an image from your camera
cam = cv2.VideoCapture(0)

#import Face Cascades (Prebuilt identification of faces)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Face detection settings
    faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Color sampling point points (Takes the face identification X and Y and adds additional pixels for sampling what shirt color you're wearing
        firstShirtSamplePointX = x + 40
        firstShirtSamplePointY = (y+h) + 125

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

        cv2.rectangle(frame, (firstShirtSamplePointX, firstShirtSamplePointY), (firstShirtSamplePointX + 5, firstShirtSamplePointY + 5),
                  (0, 240, 255), 1)
        cv2.rectangle(frame, (secondShirtSamplePointX, secondShirtSamplePointY), (secondShirtSamplePointX + 5, secondShirtSamplePointY + 5),
                  (0, 240, 255), 1)
        cv2.rectangle(frame, (thirdShirtSamplePointX, thirdShirtSamplePointY), (thirdShirtSamplePointX + 5, thirdShirtSamplePointY + 5),
                  (0, 240, 255), 1)

        h = (h1 + h2 + h3)/3
        s = (s1 + s2 + s3)/3
        v = (v1 + v2 + v3)/3

        print("HSV values = ", h, s/255, v/255)
        generalName = getColorName(h, s, v)
        print("Generalized Color Name = ", generalName)


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
