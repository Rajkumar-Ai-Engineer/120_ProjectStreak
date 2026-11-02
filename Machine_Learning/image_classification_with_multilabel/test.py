import numpy as np
import json
from keras.models import model_from_json
from PIL import Image

# Load the model architecture from JSON file
with open("model.json", 'r') as file:
    model_file = file.read()

# Load the model
model = model_from_json(model_file)

# Load weights into the model
model.load_weights("models.h5")

# Define your class labels
labels = ["burgers", "cookies", "donuts", "french_fries"]

def classify(img_path: str):
    # Open and resize the image
    img = Image.open(img_path)
    img_resize = img.resize((224, 224))
    
    # Convert image to numpy array and expand dimensions to fit the model input shape
    img_array = np.array(img_resize)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict with the model
    predict = model.predict(img_array)
    
    # Get the index with the highest probability
    predicted_class_index = np.argmax(predict)
    
    # Get the predicted label from labels list
    predicted_label = labels[predicted_class_index]
    
    # Print the predicted label
    print("Predicted Label:", predicted_label)

# Example usage
img_path = r'dataset\Train\french_fries\fries_21.jpg'
classify(img_path)
