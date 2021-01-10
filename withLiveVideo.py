import numpy as np
import cv2
import pandas as pd

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
                generalColor = "red"
            elif "blue" in cname:
                generalColor = "blue"
            elif "bleu" in cname:
                generalColor = "blue"
            elif "green" in cname:
                generalColor = "green"
            elif "yellow" in cname:
                 generalColor = "yellow"
            elif "turquoise" in cname:
                 generalColor = "turquoise"
            elif "grey" in cname:
                generalColor = "grey"
            elif "rosy" in cname:
                generalColor = "pink"
            elif "black" in cname:
                generalColor = "black"
            else:
                 generalColor = "other color named " + cname
    return generalColor, cname

#Capture an image from your camera
cam = cv2.VideoCapture(0)

#import Face Cascades (Prebuilt identification of faces)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Face detection settings
    faces = face_cascade.detectMultiScale(
        imgGray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #Color sampling point (Takes the face identification X and Y and adds additional pixels for sampling what shirt color you're wearing
    shirtSamplePointX = x + 40
    shirtSamplePointY = y + 135

    b, g, r = frame[shirtSamplePointX, shirtSamplePointY]

    cv2.rectangle(frame, (shirtSamplePointX, shirtSamplePointY), (shirtSamplePointX + 5, shirtSamplePointY + 5),
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

    jsonFile = open("index.html", "w")
    jsonFile.write(
        "{\"generalColor\": \"" + generalName + "\", \"" + cnamePost + "\": \"cnamePost\", \"BGR\": \"" + bgr + "\"}")
    jsonFile.close()




    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break



