import numpy as np
import cv2
import paho.mqtt.client as mqtt

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
client = mqtt.Client()

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:
        print("detected.....")
        image = cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imwrite('face.png', image)
        rc, png = cv2.imencode('.png', gray)
        msg = png.tobytes()

        client.connect("localhost",1883,60)
        client.publish("facetopic", payload=msg, qos=0)
        client.disconnect()

        break;

cap.release()
cv2.destroyAllWindows()

