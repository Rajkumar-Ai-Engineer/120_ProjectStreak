import os
import cv2 as cv
import face_recognition
import pickle

folder = "images"
images_path = os.listdir(folder)


img_list = []
IMG_LABELS = []

for img in images_path:
    img_list.append(cv.imread(os.path.join(folder,img)))
    IMG_LABELS.append(os.path.splitext(img)[0])


def find_encodings(img_list):
    encode = []
    
    for imgs in img_list:
        formatted = cv.cvtColor(imgs,cv.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(formatted)[0]
        encode.append(encodes)
    return encode
    
    
print("Encoding_start")
ENCODINGS_LIST = find_encodings(img_list)
print("finished")

   
data = [ENCODINGS_LIST,IMG_LABELS]

file = open("data.p",'wb')
pickle.dump(data,file)
    
