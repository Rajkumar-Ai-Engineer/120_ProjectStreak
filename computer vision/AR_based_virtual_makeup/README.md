# AR-Based Virtual Makeup

**Project ID:** 049 · **Entry point:** [fm.ipynb](fm.ipynb)

## Objective
Apply makeup-like visual effects to a face in a webcam stream or a still image using facial landmarks.

## Implementation
The notebook initializes MediaPipe Face Mesh and OpenCV. It defines image-space landmark operations for lipstick, blush, eyeliner, contouring and Gaussian-blur skin smoothing. The webcam loop converts BGR frames to RGB for MediaPipe, obtains face landmarks, applies the effects and displays the result. A later cell repeats the effect pipeline on `1.jpg`. Additional cells visualize all or selected landmark coordinates.

## Technologies
Python, MediaPipe Face Mesh, OpenCV and NumPy.

## Key functions
- `apply_lipstick`: fills a polygon formed from upper/lower lip landmark indices.
- `apply_blush`: creates a cheek mask and blends its colour.
- `apply_eyeliner`: draws connected lines around eye landmarks.
- `apply_contouring`: blends a polygon mask based on face landmarks.
- `apply_skin_smooth`: Gaussian blur blended with the original frame.
- `change_hair_color`: defined, but not called in the main makeup pipeline.

## Run assumptions
Requires a working webcam for the live cells, MediaPipe and OpenCV GUI support. The still-image cell expects `1.jpg` in the notebook working directory. No dependency lock or setup file is included.

## Review findings
- Effects use fixed BGR colour constants and fixed landmark polygons; they are not user-configurable.
- Blush/contour masks are broad polygons and may colour unintended facial regions.
- The notebook has repeated webcam capture sections; run only the intended cell sequence and release the camera between sessions.
- No face tracking stability, frame-rate, visual-quality or demographic robustness evaluation is included.
- Webcam loop exit keys differ between cells (`r` and `q`).

## Verification
Static notebook inspection only; no webcam session or notebook execution was performed. No performance or quality score is claimed.
