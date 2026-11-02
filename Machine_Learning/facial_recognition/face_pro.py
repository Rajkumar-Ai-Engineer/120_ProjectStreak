import pickle
import os
import cv2 as cv
import face_recognition
import numpy as np


file = open("data.p",'rb')
data = pickle.load(file)
ENCODINGS_LIST,IMG_LABELS = data
img = cv.imread("images\samaltman.jpg")
# res =  cv.resize(img,(500,500))
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)


face_locations = face_recognition.face_locations(img_rgb)
face_encodings = face_recognition.face_encodings(img_rgb,face_locations)

for face_loc,face_enc in zip(face_locations,face_encodings):
    
    matches = face_recognition.compare_faces(ENCODINGS_LIST,face_enc)
    face_dis = face_recognition.face_distance(ENCODINGS_LIST,face_enc)
   
    
    index = np.argmin(face_dis)
    if matches:
        
        top,right,bottom,left = face_loc
        
        img = cv.rectangle(img,(left,top),(right,bottom),(0,0,255),2)
        
        cv.putText(img,str(IMG_LABELS[index]),(left+6,top-6),cv.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
        
        
        cv.imshow("img",img)
        
        cv.waitKey(0)
            
        
    else:
        print("not found")

    
