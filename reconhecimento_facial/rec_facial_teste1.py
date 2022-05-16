from ast import While
from outcome import capture
import cv2
xml_classificador = 'haarcascade_frontalface_alt2.xml'
faceClassificador = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#iniciar_camera
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while not cv2. waitKey(20) & 0XFF == ord("q"):
    ret, frame_color=capture.read()
    gray=cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    
    faces  = faceClassificador.detectMultiScale(gray)
    for x, y, w,h, in faces:
        cv2.rectangle(frame_color, (x, y), (x+w,y+h), (0,0,255),2)
    cv2.imshow('color', frame_color)
    
    #cv2.imshow('color', frame_color)
    #cv2.imshow('gray', gray)