import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE




data = pd.read_csv('updated.csv')
print(data.info())

data = data.drop(columns=['Unnamed: 5','isFlaggedFraud'])

X = data.iloc[:5000,:-1].values
y = data.iloc[:5000,-1].values

scaler = StandardScaler()
resamp = SMOTE()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

X_train_res,y_train_res = resamp.fit_resample(X_train,y_train)

X_train = scaler.fit_transform(X_train_res)
X_test = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train,y_train_res)

pred_y = model.predict(X_test)

acc = accuracy_score(y_test,pred_y)
print(acc*100)
cl_r = classification_report(y_test,pred_y)
print(cl_r)

with open('model.pkl',mode='wb') as model_file:
    pickle.dump(model,model_file)

with open('scaler.pkl',mode='wb') as scaler_file:
    pickle.dump(scaler,scaler_file)
    
print('success')
    