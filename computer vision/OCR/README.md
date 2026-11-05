# OCR with OpenCV Preprocessing and Tesseract

**Project ID:** 053 · **Entry point:** [test.py](test.py)

## Objective
Extract text from a local image using Tesseract OCR after grayscale conversion and Otsu thresholding.

## Pipeline
Read `0.jpg` → convert BGR to grayscale → apply binary Otsu threshold → pass the thresholded image to `pytesseract.image_to_string` → print recognized text and display the processed image.

## Technologies
Python, OpenCV and pytesseract, plus the separately installed Tesseract OCR executable.

## Setup
Install the Python packages and Tesseract OCR engine. Update `pytesseract.pytesseract.tesseract_cmd` for the local operating system, and ensure `0.jpg` exists in the working directory. Run `python test.py`.

## Limitations and fixes
- The image read result is not checked before colour conversion.
- The Tesseract executable path is hard-coded to one Windows installation.
- Only one fixed thresholding method is used; skew correction, denoising, scaling and page segmentation configuration are absent.
- No OCR confidence, bounding boxes, language selection, structured output or benchmark is recorded.
- The code assumes a GUI display for `imshow`.

## Verification
Static inspection only; OCR accuracy was not independently measured.
