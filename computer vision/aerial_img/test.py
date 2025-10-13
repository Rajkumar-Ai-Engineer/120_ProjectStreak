import tensorflow as tf
from keras.applications.resnet import ResNet50,preprocess_input,decode_predictions
from keras.preprocessing.image import  img_to_array,load_img
import numpy as np 


model = ResNet50(weights='imagenet')

img_path = "city.jpg"

img = load_img(path=img_path)
img = img.resize((224,224))
img_arr = img_to_array(img)
img_arr = np.expand_dims(axis=0,a=img_arr)
img_arr = preprocess_input(x=img_arr)

predictions = model.predict(img_arr)

decode_pred = decode_predictions(preds=predictions,top=3)[0]


for i ,(image_id,label,score) in enumerate(decode_pred):
    
    print(f"{i+1}:{label} ({score:.2f})")