# Graffiti Removal with OpenCV Inpainting

**Project ID:** 056 · **Entry point:** [test.py](test.py)

## Objective
Demonstrate removal of marked graffiti from an image using two classical OpenCV inpainting algorithms.

## Pipeline
1. Load `original.png`.
2. Draw synthetic graffiti/text and save a working image.
3. Let the user mark graffiti pixels with a mouse to create a binary mask (left-drag to mark, `r` to reset, `d` to finish).
4. Apply OpenCV `INPAINT_TELEA` and `INPAINT_NS` with radius 3.
5. Display original, mask and both inpainted results; save the outputs.

## Technologies
Python, OpenCV, NumPy and Matplotlib.

## Included evidence
The directory contains `original.png`, `graffiti_image.jpg`, `result_telea.jpg` and `result_ns.jpg`. These are stored example artefacts, not independently reproduced quality measurements.

## Run
Install OpenCV, NumPy and Matplotlib. Run `python test.py` from this directory in a desktop environment. The script expects `original.png` in the working directory.

## Limitations
- Inpainting reconstructs small masked regions from surrounding pixels; it does not understand scene semantics or guarantee recovery of hidden content.
- The mask is manually drawn; no automatic graffiti segmentation is implemented.
- Results depend heavily on mask accuracy, image resolution and inpainting radius.
- No quantitative image-restoration metric or user study is provided.

## Verification
Static inspection only; saved outputs were not regenerated.
