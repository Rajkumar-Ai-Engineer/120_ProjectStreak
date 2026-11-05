# Computer Vision — Consolidated Project Index

**Canonical inventory:** Projects 049–062 · **Total:** 14 numbered folders  
**Supplemental directory:** [computervision/](../computervision/README.md) · **Audit:** [COMPUTER_VISION_AUDIT.md](../COMPUTER_VISION_AUDIT.md) · [Master catalogue](../README.md)

The repository has two separate Computer Vision-related directories. This is the consolidated domain index. Supplemental folders and image-only references are retained separately and do not silently override canonical project IDs.

## Canonical projects (IDs 049–062)

| ID | Project | Project documentation |
|---:|---|---|
| 049 | AR-Based Virtual Makeup | [README](AR_based_virtual_makeup/README.md) |
| 050 | Document Classification (AG News text classifier; domain mismatch) | [README](Document_Classifcation/README.md) |
| 051 | Image Colorization | [README](Image_Colorization/README.md) |
| 052 | Moving Object Detection | [README](MovingObjectDetection/README.md) |
| 053 | OCR | [README](OCR/README.md) |
| 054 | Pencil Sketch Conversion | [README](PencilSketchConversion/README.md) |
| 055 | Aerial Image Classification | [README](aerial_img/README.md) |
| 056 | AI Graffiti Removal | [README](ai_graffiti_removal/README.md) |
| 057 | Bar Reader (stub) | [README](bar_reader/README.md) |
| 058 | Bird Species Detection | [README](birds_species/README.md) |
| 059 | Face Recognition | [README](face_recognition/README.md) |
| 060 | Object Tracker | [README](object_tracker/README.md) |
| 061 | SimCLR | [README](simclr/README.md) |
| 062 | Vehicle Speed Estimation | [README](speedEstimation/README.md) |

## Additional source-bearing projects — IDs pending reconciliation

| Project label | Evidence / documentation |
|---|---|
| 57 — Video Summarization using OpenAI Whisper | [README](../computervision/-%2057%20%E2%80%94%20Video%20Summarization%20using%20OpenAI%20Whisper/README.md) — Whisper transcription + Transformers summarization |
| 58 — AI Image Captioning for Social Media | [README](../computervision/58_—_ai_image_captioning_for_social_media_content_using_gemini/README.md) — GIT captioning + Gemini social copy |
| Instance Segmentation | [README](../computervision/Instance-Segmentation/README.md) — Detectron2 Mask R-CNN tutorial |

## Image-only reference folders — implementation not verified

| Label | Evidence / documentation |
|---|---|
| 44 — YOLOv8 + ByteTrack | [README](../computervision/44%20%E2%80%94%20Object%20Detection%20and%20Tracking%20using%20YOLOv8%20and%20ByteTrack%20Supervision/README.md) — image only |
| 52 — Virtual Calculator | [README](../computervision/-%2052%20%E2%80%94%20Virtual%20Calculator/README.md) — image only |
| 54 — AI-Powered Drowsiness Detection | [README](../computervision/-%2054%20%E2%80%94%20AI-Powered%20Drowsiness%20Detection%20System/README.md) — image only |

## Reconciliation warnings
- Project 050 is stored in the CV folder but the inspected implementation is AG News text classification; retain its path and flag the domain mismatch.
- Supplemental labels 057 and 058 collide with canonical IDs 057 Bar Reader and 058 Bird Species. Keep both source records pending original-catalogue verification.
- Supplemental image-only 052 Virtual Calculator must not be confused with canonical 052 Moving Object Detection.
- Static inspection does not certify runtime. See [COMPUTER_VISION_AUDIT.md](../COMPUTER_VISION_AUDIT.md) for implementation and security findings.
