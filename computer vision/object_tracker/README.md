# Interactive Object Tracking with OpenCV Trackers

**Project ID:** 060 · **Entry point:** [opencvtrackers_test.py](opencvtrackers_test.py)

## Objective
Allow a user to select an object in the first video frame and track its bounding box through subsequent frames using one of OpenCV's legacy tracking algorithms.

## Implemented trackers
- BOOSTING
- MIL
- KCF

The script asks the user to choose a tracker, then accepts a video path (empty input selects webcam), reads the first frame, opens `selectROI`, initializes the tracker and updates/draws the bounding box on each subsequent frame. Press ESC to exit.

## Technologies
Python and OpenCV. The selected legacy tracker APIs may require an OpenCV contrib build and version-specific `cv.legacy` support.

## Run
Install a compatible `opencv-contrib-python` package and run `python opencvtrackers_test.py` in a desktop environment.

## Limitations
- Tracker selection uses an unchecked integer index; invalid input raises an exception.
- The first frame read is not checked before `selectROI`.
- No detector is used: the user must manually select the initial object.
- Tracking failure is displayed but there is no re-detection/reinitialization.
- No FPS, drift, robustness or benchmark comparison is recorded.
- No video output is saved.

## Verification
Static inspection only; tracker compatibility and live/video behaviour were not tested.
