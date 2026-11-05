# Pencil Sketch Conversion GUI

**Project ID:** 054 · **Entry point:** [pencil.py](pencil.py)

## Objective
Convert a user-selected image into a pencil-sketch-style grayscale image and display the original and transformed result in a Tkinter desktop window.

## Algorithm
The script reads an image with OpenCV, converts it to grayscale, inverts it, applies a 21×21 Gaussian blur, inverts the blur and divides the grayscale image by the blurred inverted image (scale 256). This is a common dodge/blend pencil-sketch approximation.

## GUI features
- Select an input image using a file dialog.
- Display original and sketch side by side.
- Save the generated sketch as PNG.

## Technologies
Python, OpenCV, NumPy, Pillow and Tkinter.

## Run
Install `opencv-python`, `numpy` and `Pillow`, then run `python pencil.py`. Tkinter and a desktop display are required.

## Defects and limitations
- `save_sketch()` calls `filedialog.askopenfilename` rather than `asksaveasfilename`; this is the wrong dialog for choosing a new output path.
- No validation is performed if OpenCV fails to read the selected image.
- No image-size limits, exception handling or automated tests are present.
- `trail.py` is a separate tiny file and is not part of the main GUI flow.

## Verification
Static inspection only; GUI interaction and image quality were not tested.
