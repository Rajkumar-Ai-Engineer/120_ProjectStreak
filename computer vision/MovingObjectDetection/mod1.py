import cv2 as cv 
import numpy as np 
import imutils

cam = cv.VideoCapture(0)

First_Instance = None
area = 500
text = "NORMAL"
while True:
    _,frame = cam.read()
    frame = imutils.resize(frame,width=500)
    gray_img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gaussian_img = cv.GaussianBlur(gray_img,(21,21),0)
    if First_Instance is None:
        First_Instance = gaussian_img 
    dif_img = cv.absdiff(First_Instance,gaussian_img)
    thresholded_img = cv.threshold(dif_img,25,255,cv.THRESH_BINARY)[1]
    dilate = cv.dilate(thresholded_img,None,iterations=2)
    contours = cv.findContours(dilate.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(contours)
    
    for c in cnts:
        if cv.contourArea(c) < area:
            continue 
        (x,y,w,h) = cv.boundingRect(c)
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        text = "MOVING OBJECT DETECTED"
    cv.putText(frame,text,(10,20),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv.destroyAllWindows()
    
    

