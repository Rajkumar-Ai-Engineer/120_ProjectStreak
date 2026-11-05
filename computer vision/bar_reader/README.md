# Barcode Reader — Implementation Stub

**Project ID in current inventory:** 057 · **Source:** [bartest.py](bartest.py)

## Current implementation
The entire Python source currently contains only:

```python
from pyzbar.pyzbar import decode
```

It imports the Pyzbar `decode` function but never loads an image/frame, invokes the function, or displays/stores decoded data.

## Status
**Source stub / incomplete implementation.** The directory should not be described as a working barcode reader yet.

## Missing pieces
- Image or webcam input.
- Invocation of `decode(image)`.
- Handling for multiple/empty detections.
- Display of barcode type, decoded value and bounding polygon.
- Error handling for unsupported formats and missing native ZBar library.
- Sample test image and tests.

## Dependencies
Pyzbar and its native ZBar dependency, plus an image input library such as OpenCV if added.

## Completion suggestion
Implement a small function that accepts an image, calls `decode`, returns type/value/bounds, and test it with known QR/barcode fixtures. Do not claim supported formats until tested.
