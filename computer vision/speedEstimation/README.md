# Vehicle Speed Estimation from Video

**Project ID:** 062 · **Source:** [traffic.py](traffic.py)

## Objective
Estimate the speed of detected objects in a video using YOLO object detection, ByteTrack IDs, polygon-zone filtering and a perspective transform.

## Observed architecture
- Load a YOLO model (default argument `yolov8x.pt`).
- Read video metadata with Supervision.
- Initialize ByteTrack at the source video's frame rate.
- Detect objects at image size 1280 and confidence threshold 0.3.
- Filter detections by class and polygon zone; apply NMS at IoU 0.5.
- Track objects, transform bottom-centre anchor points into a top-down target plane, keep recent y-coordinates per tracker ID and calculate a rate of change.
- Annotate frames with boxes, traces and labels; write to `result.mp4`.

## Technologies
Ultralytics YOLO, Supervision, OpenCV, NumPy, collections and tqdm.

## Important correctness issues
- `sv.get_video_frames_generator(self.Source)` is passed the polygon coordinates rather than `self.video_path`; this is a blocking input error.
- Speed is computed from transformed pixel displacement and converted to km/h by multiplying by 3.6, but the target plane is defined in arbitrary pixel units (25×250). No real-world distance calibration is present, so the km/h label is not physically justified.
- The source polygon coordinates and perspective transform are hard-coded for one camera view and resolution.
- `detections.class_id != 0` removes class 0 (commonly person in COCO); document the intended vehicle classes and filter explicitly.
- The `Roboflow` import is capitalized and unused; the required package/dependency list is not defined.
- No CLI/main invocation is shown in the inspected source, and no source video or model weights are included.

## Status
**Prototype with at least one blocking video-generator argument defect and uncalibrated speed units.** Treat output speed values as unvalidated until corrected and calibrated against measured distances.

## Verification
Static inspection only; no video processing or speed measurement was run.
