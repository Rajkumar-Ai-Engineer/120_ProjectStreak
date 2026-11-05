# Computer Vision Domain Audit

**Repository:** [Rajkumar-Ai-Engineer/120_ProjectStreak](https://github.com/Rajkumar-Ai-Engineer/120_ProjectStreak)  
**Branch inspected:** `master`  
**Audit date:** 2026-11-05  
**Scope:** Both `computer vision/` and `computervision/` directories  
**Method:** Recursive Git tree inspection plus static review of project READMEs, Python files, notebook cells, model/configuration artifacts and saved run outputs.

## 1. Executive summary

The repository has two distinct Computer Vision-named directories. The original `computer vision/` directory contains **14 numbered project folders (049–062)**. The separate `computervision/` directory contains **3 code-bearing project folders** and **3 image-only folders**. The image-only folders are not counted as implemented projects.

| Measure | Finding |
|---|---:|
| Numbered project folders in `computer vision/` | 14 |
| Additional code-bearing folders in `computervision/` | 3 |
| Image-only folders in `computervision/` | 3 |
| Code-bearing folders inspected | 17 |
| Project-specific README files rewritten/created | 20 |
| Domain index files created | 2 |
| Training/inference executed during this audit | 0 |

These are folder-level findings, **not a final count of unique intended catalogue projects**. The original source catalogue is not available in this repository inspection context. Duplicate identity and official numbering therefore remain subject to cross-source reconciliation.

## 2. Scope and directory structure

### 2.1 Numbered collection: `computer vision/`

| ID | Project | Path | Static status |
|---:|---|---|---|
| 049 | AR-Based Virtual Makeup | `AR_based_virtual_makeup` | Notebook implementation |
| 050 | Document Classification | `Document_Classifcation` | Implemented text classifier; domain mismatch |
| 051 | Image Colorization | `Image_Colorization` | App/script present; model weights missing |
| 052 | Moving Object Detection | `MovingObjectDetection` | Webcam motion-detection script |
| 053 | OCR | `OCR` | Single-image Tesseract script |
| 054 | Pencil Sketch Conversion | `PencilSketchConversion` | Tkinter GUI script |
| 055 | Aerial Image | `aerial_img` | ImageNet ResNet50 demo |
| 056 | AI Graffiti Removal | `ai_graffiti_removal` | Interactive OpenCV inpainting demo |
| 057 | Bar Reader | `bar_reader` | Import-only stub |
| 058 | Birds Species | `birds_species` | YOLO training artifacts + checkpoint loader |
| 059 | Face Recognition | `face_recognition` | Haar + LBPH webcam workflow |
| 060 | Object Tracker | `object_tracker` | OpenCV manual-initialization tracker |
| 061 | SimCLR | `simclr` | Training code has blocking defects |
| 062 | Speed Estimation | `speedEstimation` | YOLO + ByteTrack prototype; speed calibration invalid |

### 2.2 Additional collection: `computervision/`

| Folder label | Evidence found | Classification |
|---|---|---|
| 44 — Object Detection and Tracking using YOLOv8 and ByteTrack Supervision | One PNG image only | Image/reference artefact; no implementation |
| 52 — Virtual Calculator | One PNG image only | Image/reference artefact; domain and implementation unverified |
| 54 — AI-Powered Drowsiness Detection System | One PNG image only | Image/reference artefact; no implementation |
| 57 — Video Summarization using OpenAI Whisper | Python/Colab-exported script | Code-bearing; vision-adjacent video/audio NLP |
| 58 — AI Image Captioning for Social Media Content using Gemini | Python/Colab-exported script | Code-bearing; image captioning + LLM content generation |
| Instance-Segmentation | Detectron2 training script | Code-bearing; custom COCO instance-segmentation tutorial |

## 3. Important findings and remediation priority

### Critical — exposed API credential

The Detectron2 training script contains a literal Roboflow API credential. It is committed in the repository and must be treated as compromised.

**Required action:** Revoke/rotate the credential in Roboflow, replace it with environment/secret-manager access, and review Git history for removal. The credential value is intentionally not copied into this report. Documentation updates do not remediate the exposed secret.

### High — incorrect speed units and video source

In `computer vision/speedEstimation/traffic.py`:
- The video-frame generator is initialized with the polygon coordinate array instead of `self.video_path`, a blocking argument error.
- Pixel displacement in a perspective-transformed 25×250 target plane is multiplied by 3.6 and labelled km/h without a real-world distance calibration. This does not establish physical speed.
- The source polygon is camera-specific and hard-coded.
- Class ID 0 is excluded; the intended class mapping should be made explicit.

### High — SimCLR objective and runtime defects

In `computer vision/simclr/main.py`:
- ResNet input shape omits the RGB channel dimension.
- `tf.GradientTape` is used without calling its constructor.
- Contrastive labels point each embedding to its own diagonal similarity rather than the paired augmented view, so the loss is not a correct SimCLR NT-Xent objective.
- The loaded test split is unused.

The current source does not establish successful SimCLR training.

### High — missing colourization weights and absolute paths

In `computer vision/Image_Colorization/`:
- The required `colorization_release_v2.caffemodel` is referenced but absent.
- Scripts contain machine-specific absolute Windows paths.
- The Streamlit app's prototxt filename does not match the checked-in filename.
- The app receives a PIL RGB array but uses a BGR-to-grayscale conversion constant; channel handling should be corrected and tested.

### Medium — project domain and inventory discrepancies

- Project 050 loads AG News and implements an LSTM text classifier. It belongs to NLP/text classification, not Computer Vision.
- Project 055 uses ImageNet-pretrained ResNet50 for generic top-three classification. No aerial-specific dataset/model is present.
- Project 057 (Bar Reader) only imports `pyzbar.decode`; it does not decode an image.
- Project IDs 057 and 058 in the additional `computervision/` folder collide with existing IDs 057 (Bar Reader) and 058 (Bird Species) in the numbered folder. Do not renumber until the original source catalogue is checked.
- Project 44 and 54 additional folders contain images only; they must not be represented as implemented projects.
- Project 57's Whisper summarization and Project 58's image captioning are not strictly conventional computer-vision-only workloads; their placement should be validated against the domain taxonomy.

### Other code-level observations

- Project 052's motion status is never reset to NORMAL after motion stops, and failed camera reads are not handled.
- Project 054 uses `askopenfilename` for saving; it should use a save dialog.
- Project 058's notebook loads a saved YOLO checkpoint but has no meaningful inference workflow in the inspected cells. The recorded training CSV reports final-epoch precision 0.96081, recall 0.96842, mAP50 0.98361 and mAP50–95 0.83109; these are historical artifacts, not independently reproduced metrics.
- Project 059 uses a hard-coded LBPH distance threshold, has no held-out evaluation and processes biometric face images. Consent, access control and retention controls are required before real-world use.
- Project 060 has unchecked tracker selection and first-frame handling; tracking is manually initialized and no detector/re-identification exists.
- Project 049's makeup effects use fixed landmark polygons and colours; there is no visual-quality or robustness evaluation.
- Project 056 uses manually drawn masks and classical inpainting; it does not implement automatic graffiti segmentation.

## 4. Per-project documentation

Each code-bearing project now has a project-specific README describing actual source behaviour, dependencies, known defects, verification boundaries and next steps.

- [049 — AR-Based Virtual Makeup](computer%20vision/AR_based_virtual_makeup/README.md)
- [050 — AG News Text Classification](computer%20vision/Document_Classifcation/README.md)
- [051 — Image Colorization](computer%20vision/Image_Colorization/README.md)
- [052 — Moving Object Detection](computer%20vision/MovingObjectDetection/README.md)
- [053 — OCR](computer%20vision/OCR/README.md)
- [054 — Pencil Sketch Conversion](computer%20vision/PencilSketchConversion/README.md)
- [055 — ImageNet Classification Demo](computer%20vision/aerial_img/README.md)
- [056 — Graffiti Removal](computer%20vision/ai_graffiti_removal/README.md)
- [057 — Barcode Reader Stub](computer%20vision/bar_reader/README.md)
- [058 — Bird Species Detection](computer%20vision/birds_species/README.md)
- [059 — Face Recognition](computer%20vision/face_recognition/README.md)
- [060 — Object Tracker](computer%20vision/object_tracker/README.md)
- [061 — SimCLR](computer%20vision/simclr/README.md)
- [062 — Speed Estimation](computer%20vision/speedEstimation/README.md)
- [Additional — YOLOv8 + ByteTrack image-only placeholder](computervision/44 — Object Detection and Tracking using YOLOv8 and ByteTrack Supervision/README.md)
- [Additional — Drowsiness Detection image-only placeholder](computervision/- 54 — AI-Powered Drowsiness Detection System/README.md)
- [Additional — Whisper Video Summarization](computervision/- 57 — Video Summarization using OpenAI Whisper/README.md)
- [Additional — Gemini Social Image Captioning](computervision/58_—_ai_image_captioning_for_social_media_content_using_gemini/README.md)
- [Additional — Virtual Calculator image-only placeholder](computervision/- 52 — Virtual Calculator/README.md)
- [Additional — Detectron2 Instance Segmentation](computervision/Instance-Segmentation/README.md)

## 5. Verification boundaries

- The audit used recursive Git trees and static source/notebook/configuration inspection.
- No Python script, notebook, model, webcam, video, GPU training run or external API was executed.
- Notebook outputs and CSV metrics are reported only as committed historical artifacts.
- No project is certified as production-ready.
- No implementation files were intentionally changed in this documentation pass.
- The source catalogue for the full 120-project target was not part of this scoped Computer Vision pass; this report does not declare any project globally missing.

## 6. Recommended next actions

1. Rotate the exposed Roboflow credential immediately.
2. Fix and test the speed-estimation frame generator and perform physical calibration before displaying km/h.
3. Correct the SimCLR model input, gradient-tape context and NT-Xent positive-pair/masking logic.
4. Add or document the missing Caffe weights and remove absolute paths from Image Colorization.
5. Implement Barcode Reader or mark it explicitly as a stub in the project catalogue.
6. Reconcile the additional folder's IDs 44/52/54/57/58 with the authoritative source list.
7. Move Project 050 into the correct NLP domain only after preserving catalogue numbering and links.
8. Add dependency manifests, tests and reproducible evaluation for each project.
