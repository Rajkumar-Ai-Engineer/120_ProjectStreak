import os 
import numpy as np 
import cv2 as cv 

haarfile = "haarcascade_frontalface_default.xml"

face_cascade = cv.CascadeClassifier(haarfile)

datasets = "dataset"

print("Training")

(images,labels,names,id) = ([],[],{},0)

for (root_dir,dirs,files) in os.walk(datasets):
    
    
    for sub_dir in dirs:
        names[id] = sub_dir
        
        full_path_folder = os.path.join(datasets,sub_dir)
        
        for filename in os.listdir(full_path_folder):
            path = full_path_folder + "/" + filename
            label = id
            images.append(cv.imread(path,0))
            labels.append(int(label))
        id +=1 

(images,labels) = [np.array(lis) for lis in [images,labels]]

(width,height) = (130,100)


model = cv.face.LBPHFaceRecognizer_create()

model.train(images,labels)

cam = cv.VideoCapture(0)

cnt = 0

while True:
    
    _,frame = cam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        face = gray[y:y+h,x:x+w]
        
        face_resize = cv.resize(face,(width,height))
        
        prediction = model.predict(face_resize)
        
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        if prediction[1]<400:
            cv.putText(frame,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv.FONT_HERSHEY_PLAIN,2,(255, 0, 0),2)
            print (names[prediction[0]])
            cnt=0
        else:
            cnt+=1
            cv.putText(frame,'Unknown',(x-10, y-10), cv.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            if(cnt>100):
                print("Unknown Person")
                cv.imwrite("unKnown.jpg",frame)
                cnt=0
    cv.imshow('FaceRecognition', frame)
    key = cv.waitKey(10)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()