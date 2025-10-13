import os
import cv2 as cv
import matplotlib.pyplot as plt

cascade_file_path = "haarcascade_frontalface_default.xml"

datasets = "dataset"

sub_data = input("Enter a person Name to store the image in that folder:")
# sub_data = "Raju"

path = os.path.join(datasets,sub_data)

if not os.path.isdir(path):
    os.makedirs(path)
    

(width,height) = (130,100)


face_cascaded_file = cv.CascadeClassifier(cascade_file_path)


cam = cv.VideoCapture(0)

count = int(input("Enter the number to take as much as images for that person:"))

initial = 1

while initial < count:
    
    _,frame = cam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    faces = face_cascaded_file.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=4)
    
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
        face = gray[y:y+h,x:x+w]        
        face_resize = cv.resize(face,(width,height))
        cv.imwrite('%s/%s.png' %(path,initial),face_resize)
        
        initial +=1      
        
    # img = plt.imshow(cv.cvtColor(frame,cv.COLOR_BGR2RGB))
    # plt.axis("off")
    # plt.show()
        
    cv.imshow("Collecting the data...",frame)
    if cv.waitKey(1) & 0xff == ord("r"):
        break
    
cam.release()
cv.destroyAllWindows()