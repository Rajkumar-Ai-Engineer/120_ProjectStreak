from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model and scaler
with open('model.pkl', mode='rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', mode='rb') as scaler_file:
    scaler = pickle.load(scaler_file)

app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API! Use /docs for Swagger UI or /predict/ to make predictions."}

# Input data model
class TransactionData(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    CASH_IN: int
    CASH_OUT: int
    DEBIT: int
    PAYMENT: int
    TRANSFER: int

@app.post("/predict/")
def predict(transaction: TransactionData):
    # Create numpy array
    data = np.array([
        transaction.amount,
        transaction.oldbalanceOrg,
        transaction.newbalanceOrig,
        transaction.oldbalanceDest,
        transaction.newbalanceDest,
        transaction.CASH_IN,
        transaction.CASH_OUT,
        transaction.DEBIT,
        transaction.PAYMENT,
        transaction.TRANSFER,
    ])

    # Scale the data (ensure correct shape)
    scaled_data = scaler.transform([data])  # Reshape to 2D

    # Predict fraud and probabilities
    prediction = model.predict(scaled_data)
    proba = model.predict_proba(scaled_data)

    return {
        "fraud": int(prediction[0]),  # Convert to int for JSON
        "probability": proba[0].tolist(),  # Convert to list for JSON
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
