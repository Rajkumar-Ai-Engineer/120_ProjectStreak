import pickle
import cv2 as cv
import face_recognition
import numpy as np

# Load the face encodings and labels
with open("data.p", 'rb') as file:
    data = pickle.load(file)
ENCODINGS_LIST, IMG_LABELS = data

# Initialize webcam
cam = cv.VideoCapture(0)
cam.set(3, 640)  # Set width
cam.set(4, 480)  # Set height

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Convert to RGB for face_recognition processing
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Detect faces and compute encodings
    face_locations = face_recognition.face_locations(img_rgb)
    face_encodings = face_recognition.face_encodings(img_rgb, face_locations)

    for face_loc, face_enc in zip(face_locations, face_encodings):
        # Compare faces
        matches = face_recognition.compare_faces(ENCODINGS_LIST, face_enc)
        face_dis = face_recognition.face_distance(ENCODINGS_LIST, face_enc)

        if len(matches) > 0 and any(matches):
            index = np.argmin(face_dis)

            if matches[index]:
                # Get coordinates
                top, right, bottom, left = face_loc

                # Draw rectangle and label
                cv.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                cv.putText(img, str(IMG_LABELS[index]), (left + 6, top - 6), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

    # Display the image
    cv.imshow("Face Recognition", img)

    # Break the loop on pressing 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv.destroyAllWindows()
