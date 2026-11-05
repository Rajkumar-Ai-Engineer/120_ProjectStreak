# Computer Vision Projects

This directory contains the repository's numbered computer-vision learning projects (049–062). Each project README is intended to describe the actual checked-in implementation, dependencies, execution assumptions, limitations and verification status.

## Project index

| ID | Project | Directory |
|---:|---|---|
| 049 | AR-Based Virtual Makeup | [AR_based_virtual_makeup](AR_based_virtual_makeup/README.md) |
| 050 | Document Classification (AG News text classifier; domain mismatch) | [Document_Classifcation](Document_Classifcation/README.md) |
| 051 | Image Colorization | [Image_Colorization](Image_Colorization/README.md) |
| 052 | Moving Object Detection | [MovingObjectDetection](MovingObjectDetection/README.md) |
| 053 | OCR | [OCR](OCR/README.md) |
| 054 | Pencil Sketch Conversion | [PencilSketchConversion](PencilSketchConversion/README.md) |
| 055 | Aerial Image Classification | [aerial_img](aerial_img/README.md) |
| 056 | AI Graffiti Removal | [ai_graffiti_removal](ai_graffiti_removal/README.md) |
| 057 | Bar Reader (stub) | [bar_reader](bar_reader/README.md) |
| 058 | Bird Species Detection | [birds_species](birds_species/README.md) |
| 059 | Face Recognition | [face_recognition](face_recognition/README.md) |
| 060 | Object Tracker | [object_tracker](object_tracker/README.md) |
| 061 | SimCLR | [simclr](simclr/README.md) |
| 062 | Vehicle Speed Estimation | [speedEstimation](speedEstimation/README.md) |

## Audit notes
- Project 050 uses the AG News text dataset and an LSTM text-classification pipeline; its current location under Computer Vision is semantically incorrect.
- Project 057 contains only an import of `pyzbar.decode`; no image loading, decoding call, or output path is implemented.
- Several experiments have hard-coded machine/Colab paths and missing model/data assets.
- See the repository-level [Computer Vision Audit](../COMPUTER_VISION_AUDIT.md) for findings across both Computer Vision folders.
