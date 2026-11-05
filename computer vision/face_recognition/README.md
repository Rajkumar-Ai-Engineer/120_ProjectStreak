# Face Recognition with Haar Cascades and LBPH

**Project ID:** 059 · **Scripts:** [collect_data.py](collect_data.py), [face_reco.py](face_reco.py)

## Objective
Collect face crops for named people using a webcam, train OpenCV's Local Binary Patterns Histograms (LBPH) face recognizer, and classify detected faces from a live camera stream.

## Data collection
`collect_data.py` asks for a person label and number of images, creates a corresponding `dataset/<person>/` folder, detects faces with `haarcascade_frontalface_default.xml`, resizes grayscale crops to 130×100 and saves numbered PNG files.

## Recognition pipeline
`face_reco.py` walks the dataset folders, assigns integer labels, loads grayscale face images, trains `cv.face.LBPHFaceRecognizer_create()`, detects faces in webcam frames, resizes crops to 130×100 and predicts a label. A distance threshold of 400 controls whether a face is displayed as a known label or `Unknown`.

## Technologies
OpenCV (including the contrib face module), NumPy and Haar cascade XML.

## Run assumptions
Install a compatible `opencv-contrib-python` build and NumPy. Run data collection for each label, then run recognition from this directory. The cascade XML and dataset paths are relative to the working directory.

## Important limitations
- The recognition threshold of 400 is hard-coded and not calibrated on a held-out set.
- Dataset labels and images are loaded without filtering unreadable files or checking empty data.
- The collection loop stops when `initial < count`, so it may collect one fewer image than requested.
- Webcam read failures and camera initialization are not handled.
- No train/test split, accuracy, FAR/FRR, confusion matrix, liveness detection or demographic evaluation exists.
- Face data is biometric personal data; obtain informed consent, restrict access, set retention/deletion rules and avoid deploying this demo for consequential decisions.

## Verification
Static source inspection only; no face-recognition experiment or performance evaluation was run.
