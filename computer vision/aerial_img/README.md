# ImageNet Image Classification Demo on Aerial Samples

**Project ID:** 055 · **Entry point:** [test.py](test.py)

## Objective
Run an ImageNet-pretrained ResNet50 classifier on a local image (the checked-in example path is `city.jpg`) and print its top-three ImageNet predictions.

## Pipeline
Load ResNet50 with ImageNet weights → load and resize image to 224×224 → convert to array and add batch dimension → apply ResNet preprocessing → predict → decode and print top-three labels and scores.

## Technologies
TensorFlow/Keras ResNet50 and NumPy.

## Included assets
`city.jpg` and `lake.jpg` are present. The script currently references only `city.jpg`.

## Important interpretation
This is a generic ImageNet classification demonstration, not evidence of an aerial/satellite-specific model. No aerial dataset, custom training, geospatial processing or domain-specific class taxonomy is included.

## Run
Install a compatible TensorFlow/Keras stack and NumPy, ensure the current working directory contains `city.jpg`, and run `python test.py`.

## Limitations
- Top-three ImageNet labels are not calibrated aerial-image predictions.
- No evaluation dataset, metrics, batch processing or model fine-tuning exists.
- Image read failures and unsupported formats are not handled.
- Reproducibility depends on compatible TensorFlow/Keras versions and pretrained-weight availability.

## Verification
Static source inspection only; predictions were not reproduced.
