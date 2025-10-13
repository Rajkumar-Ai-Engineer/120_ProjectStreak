from keras.models import load_model
import joblib
import pandas as pd
import numpy as np

model = load_model(filepath='model.h5')


data = pd.read_csv("scaled.csv")

x = data.drop('Label',axis=1)
# print(x)
input_data = x.values.reshape(x.shape[0],1,x.shape[1])
# Predict
prediction = model.predict(input_data[4:5])

prediction = np.argmax(prediction,axis=1)




print("Predicted Output:", "benign" if prediction[0] == 0 else "ddos")

