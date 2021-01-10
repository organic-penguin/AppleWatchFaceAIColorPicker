import numpy as np
import cv2
import pandas as pd
import os
import time

colorIndex=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('include/colors.csv', names=colorIndex, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i, "R"])) + abs(G- int(csv.loc[i, "G"]))+ abs(B- int(csv.loc[i, "B"]))
        if(d <= minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
            cname = cname.lower()
            if "red" in cname:
                generalColor = "Red"
            elif "blue" in cname:
                generalColor = "Blue"
            elif "bleu" in cname:
                generalColor = "Blue"
            elif "green" in cname:
                generalColor = "Green"
            elif "yellow" in cname:
                 generalColor = "Yellow"
            elif "turquoise" in cname:
                 generalColor = "Turquoise"
            elif "grey" in cname:
                generalColor = "Grey"
            elif "rosy" in cname:
                generalColor = "Pink"
            elif "black" in cname:
                generalColor = "Black"
            else:
                 generalColor = "Other"
    return generalColor, cname

#Capture an image from your camera then save as an image to reuse later and single frame processing (save resources)
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cv2.imwrite("openCVImage.png", frame)
img = cv2.imread("openCVImage.png")
cam.release
#import Face Cascades (Prebuilt identification of faces)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Face detection settings
faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Color sampling point (Takes the face identification X and Y and adds additional pixels for sampling what shirt color you're wearing
    shirtSamplePointX = x + 40
    shirtSamplePointY = y + 125

    b, g, r = img[shirtSamplePointX, shirtSamplePointY]

    cv2.rectangle(img, (shirtSamplePointX, shirtSamplePointY), (shirtSamplePointX + 5, shirtSamplePointY + 5),
                  (0, 0, 255), 1)
    b = int(b)
    g = int(g)
    r = int(r)
    print("RGB values = ", r, g, b)
    generalName = getColorName(r, g, b)[0]
    cnamePost = getColorName(r, g, b)[1]
    print("Generalized Color Name = ", generalName)
    print("CNAME is " + cnamePost)

    bgr = str(r) + "," + str(g) + "," + str(b)
    cv2.imwrite("openCVImage.png", img)
    jsonFile = open("index.html", "w")
    jsonFile.write(
        "{\"generalColor\": \"" + generalName + "\", \"" + cnamePost + "\": \"cnamePost\", \"BGR\": \"" + bgr + "\"}")
    jsonFile.close()
    time.sleep(1)
    os.popen("git add index.html openCVImage.png --force")
    time.sleep(1)
    os.popen("git commit -m \"Adding todays colors\"")
    time.sleep(1)
    os.popen("git push origin")
    time.sleep(1)

