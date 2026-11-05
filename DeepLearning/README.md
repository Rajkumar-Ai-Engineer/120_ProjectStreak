# Deep Learning Projects

This directory contains **19 project-like top-level directories**. The repository's current `PROJECT_INVENTORY.md` formally indexes 10 DeepLearning project boundaries (IDs 001–010). Nine additional directories have now been given project-specific documentation but remain **unindexed candidates** pending the overall project reconciliation. They have deliberately not been assigned invented project IDs.

## Indexed projects (IDs 001–010)

| ID | Project | Documentation |
|---:|---|---|
| 001 | AI Cyber — LSTM-based network intrusion/DDoS classification | [README](AI_cyber/README.md) |
| 002 | Brain Tumour — VGG19 transfer-learning experiment | [README](Brain_tumour/README.md) |
| 003 | Human Pose — OpenPose with OpenCV DNN | [README](Human_pose/README.md) |
| 004 | Seq Seq — English-to-Hindi MarianMT translation | [README](SEQ_SEQ/README.md) |
| 005 | YOLO — YOLOv4 video object detection | [README](Yolo/README.md) |
| 006 | Face Mask Detector — SSD + MobileNet | [README](maskdetector/25-%20Face%20Mask%20detector/README.md) |
| 007 | Recurrent sentiment models — SimpleRNN/LSTM/GRU | [README](preditive/README.md) |
| 008 | Speech command recognition — 1D CNN | [README](speech/README.md) |
| 009 | Style Transfer — CycleGAN horse↔zebra | [README](style_transfer/README.md) |
| 010 | U-Net image segmentation architecture | [README](unet_image_segmentation/README.md) |

## Additional documented directories — IDs not yet assigned

These directories were present in GitHub but absent from the current formal project inventory. They may represent additional projects, alternate experiments, duplicates, or historical artifacts. Keep them separate until source reconciliation determines their canonical project identity and number.

| Directory | README |
|---|---|
| `DC-GAN` | [README](DC-GAN/README.md) |
| `DeepFake` | [README](DeepFake/README.md) |
| `GPT-2` | [README](GPT-2/README.md) |
| `ImageCaption` | [README](ImageCaption/README.md) |
| `Path-hole` | [README](Path-hole/README.md) |
| `bert_for_emotion` | [README](bert_for_emotion/README.md) |
| `cycle-GAN` | [README](cycle-GAN/README.md) |
| `tactron` | [README](tactron/README.md) |
| `- 34 — Super-Resolution for Image Reconstruction using GANs` | [README](< - 34 — Super-Resolution for Image Reconstruction using GANs/README.md>) |

## Audit notes

- The `cycle-GAN` and `style_transfer` folders may be duplicate or alternate CycleGAN experiments; compare their notebook contents before counting them separately.
- The YOLOv4 demo and the separate YOLOv11 pothole-detection notebook are distinct model/use-case artifacts unless later evidence establishes otherwise.
- The root file `40 — License Plate Detection using YOLOv9.png` is an image asset only; it is not counted as an implemented project from this evidence.
- Static inspection only. Notebooks were not rerun during documentation. Historical outputs are not independently reproduced.
- Some README files intentionally record incomplete or unresolved implementation details rather than claiming a complete runnable application.
