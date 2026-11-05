# Webcam Moving-Object Detection by Frame Differencing

**Project ID:** 052 · **Entry point:** [mod1.py](mod1.py)

## Objective
Detect motion in a webcam stream by comparing each frame with an initial grayscale background frame.

## Pipeline
Open webcam → resize frame to width 500 → grayscale → Gaussian blur (21×21) → absolute difference from initial frame → binary threshold at 25 → dilation (2 iterations) → external contour extraction → draw rectangles for contours with area at least 500 pixels → display status.

## Technologies
Python, OpenCV, NumPy and imutils.

## Run
Install `opencv-python`, `numpy` and `imutils`, then run `python mod1.py`. Press `q` to exit. A webcam and desktop display are required.

## Implementation limitations
- The first successfully read frame becomes the permanent background; lighting or camera movement can cause widespread false detections.
- The capture return flag is ignored before resizing, so camera failure can cause an exception.
- Status text is set to MOVING once a contour passes the area threshold and is never reset to NORMAL when motion stops.
- No background adaptation, shadows handling, object classification, tracking IDs, persistence or evaluation exists.
- The frame-difference approach detects change, not semantic object identity.

## Verification
Static source review only; webcam behaviour was not executed or measured.
