# Grayscale Image Colorization

**Project ID:** 051 · **Primary app candidate:** [app (1).py](<app%20(1).py>) · **Additional script:** [train.py](train.py)

## Objective
Predict chrominance channels for a grayscale image using a pretrained Caffe colourization network, then combine them with the original luminance channel to produce a colour image.

## Implementation
Both Python files convert an image to grayscale, convert it to RGB/Lab, resize the L channel to 224×224, subtract 50, run a Caffe DNN forward pass, resize predicted a/b channels to the source dimensions, concatenate with the original L channel and convert Lab back to RGB. The app wraps this flow in a Streamlit image uploader; `train.py` loads `1.jpg` and displays before/after images with Matplotlib.

## Technologies and assets
OpenCV DNN, NumPy, Pillow, Matplotlib and Streamlit. The folder contains a network prototxt and `pts_in_hull.npy`.

## Blocking issue
The required pretrained Caffe weights file (`colorization_release_v2.caffemodel`) is referenced by the scripts but is not present in the inspected folder. The app and script also contain absolute Windows paths that point to different local machines. The app's expected prototxt filename differs from the checked-in name.

## Setup and operation
Install the imports used by the chosen entry point, obtain the correct model weights from a trusted source, verify the model/points files, and replace hard-coded paths with configuration. Run the Streamlit file with `streamlit run "app (1).py"` only after resolving those paths.

## Review findings
- `train.py` is inference/demo code; it does not train the colourization network.
- The Streamlit app converts a PIL-derived RGB array using a BGR-to-gray conversion constant; validate channel handling to avoid colour-channel errors.
- No tests, quality metrics, model provenance/license record or reproducible model download instructions are present.

## Verification
Static inspection only; no inference was run and no output quality claim is made.
