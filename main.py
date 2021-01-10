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

#Capture an image from your camera
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
img_name = "openCVImage.png"
cv2.imwrite(img_name, frame)
img = cv2.imread('openCVImage.png')
imgResize = cv2.resize(img, (250, 200))
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = imgGray[y:y+h, x:x+w]
    roi_color = imgResize[y:y+h, x:x+w]

    shirtSamplePointX = x + 20
    shirtSamplePointY = y + 100

    b,g,r = imgResize[shirtSamplePointX, shirtSamplePointY]

    cv2.rectangle(imgResize, (shirtSamplePointX, shirtSamplePointY), (shirtSamplePointX+5, shirtSamplePointY+5), (0, 0, 255), 1)
    b = int(b)
    g = int(g)
    r = int(r)
    print("RGB values = ", r, g, b)
    generalName = getColorName(r, g, b)[0]
    cnamePost = getColorName(r, g, b)[1]
    print("Generalized Color Name = ", generalName )
    print("CNAME is " + cnamePost)

    bgr = str(r) + "," + str(g) + "," + str(b)

    jsonFile = open("index.html", "w")
    jsonFile.write("{\"generalColor\": \""+generalName+"\", \""+cnamePost+"\": \"cnamePost\", \"BGR\": \""+bgr+"\"}")
    jsonFile.close()

