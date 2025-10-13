from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import time
import cv2 as cv


conf = 0.5

cam = cv.VideoCapture(0)


def detect_model(frame,facenet,masknet):
    
    (H,W) = frame.shape[:2]
    blob = cv.dnn.blobFromImage(frame,1.0,(300,300),(104.0,177.0,123.0))
    facenet.setInput(blob)
    detections = facenet.forward()
    
    faces = []
    coordinates = []
    preds = []
    
    for i in range(0,detections.shape[2]):
        
        confidence = detections[0,0,i,2]
        
        if confidence > conf:
            
            box = detections[0,0,i,3:7] * np.array([W,H,W,H])
            
            (startX,startY,endX,endY) = box.astype("int")
            
            (startX,startY) = (max(0,startX),max(0,startY))
            (endX,endY)  = (min(W - 1,endX),min(H - 1,endY))
            
            face = frame[startY:endY,startX:endX]
            face = cv.cvtColor(face, cv.COLOR_BGR2RGB)
            face = cv.resize(face,(224,224))
            face = img_to_array(face)
            face = preprocess_input(face)
            
            faces.append(face)
            coordinates.append((startX,startY,endX,endY))
            
    if len(faces) > 0:
        
        faces = np.array(faces,dtype="float32")
        preds = masknet.predict(faces,batch_size=32)
        
    return (coordinates,preds)


prototype_file_path = "deploy.prototxt"
weights_path        = "res10_300x300_ssd_iter_140000.caffemodel"

trained_model = "model_mobilenet.h5"

facenet = cv.dnn.readNet(prototype_file_path,weights_path)

masknet = load_model(trained_model)


while True:
    
    _,frame = cam.read()
    
    frame = imutils.resize(frame,width=500)
    
    (cords,preds) = detect_model(frame,facenet,masknet)
    
    for (box,pred) in zip(cords,preds):
        
        (startX,startY,endX,endY) = box
        (withoutMask,mask) = pred
        
        label = "No Mask" if withoutMask > mask  else "Mask"
        color = (0,255,0) if label == "Mask" else (0,0,255)
        
        label = "{}: {:.2f}%".format(label,max(mask,withoutMask) * 100)
        
        cv.putText(frame,label,(startX,startY-10),cv.FONT_HERSHEY_COMPLEX,0.45,color)
        
        cv.rectangle(frame,(startX,startY),(endX,endY),color,2)
        
    cv.imshow("Frame",frame)
    if cv.waitKey(1) &  0xff == ord("q"):
        break

cam.release()
cv.destroyAllWindows()

        
        
        