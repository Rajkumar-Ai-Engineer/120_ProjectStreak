# Deep Learning — Project Index

**Canonical inventory:** Projects 001–010 · **Canonical total:** 10  
**Additional source-bearing folders:** 9 candidates · **Image-only reference:** 1  
**Master catalogue:** [Repository README](../README.md) · [Documentation coverage](../DOCUMENTATION_COVERAGE.md)

This index separates the ten entries in the canonical project inventory from additional folders and image references discovered during the audit. The extra folders are not assigned IDs until reconciled against the original 120-project catalogue.

## Canonical projects (IDs 001–010)

| ID | Project | Implementation focus | Documentation |
|---:|---|---|---|
| 001 | AI Cyber | LSTM-based network intrusion/DDoS classification | [README](AI_cyber/README.md) |
| 002 | Brain Tumour | VGG19 transfer-learning experiment | [README](Brain_tumour/README.md) |
| 003 | Human Pose | OpenPose with OpenCV DNN | [README](Human_pose/README.md) |
| 004 | Seq Seq | English-to-Hindi MarianMT translation | [README](SEQ_SEQ/README.md) |
| 005 | YOLO | YOLOv4 video object detection | [README](Yolo/README.md) |
| 006 | Face Mask Detector | SSD + MobileNet | [README](maskdetector/25-%20Face%20Mask%20detector/README.md) |
| 007 | Recurrent sentiment models | SimpleRNN/LSTM/GRU | [README](preditive/README.md) |
| 008 | Speech command recognition | 1D CNN | [README](speech/README.md) |
| 009 | Style Transfer | CycleGAN horse↔zebra | [README](style_transfer/README.md) |
| 010 | U-Net Image Segmentation | U-Net encoder-decoder | [README](unet_image_segmentation/README.md) |

## Additional source-bearing folders — IDs pending reconciliation

| Folder | Observed focus | Documentation |
|---|---|---|
| DC-GAN | CIFAR-10 DCGAN experiment | [README](DC-GAN/README.md) |
| DeepFake | Deepfake image/video detection notebook | [README](DeepFake/README.md) |
| GPT-2 | GPT-2 loading demo and separate DistilBERT QA component | [README](GPT-2/README.md) |
| ImageCaption | VGG16 + LSTM image captioning | [README](ImageCaption/README.md) |
| Path-hole | YOLOv11 Nano pothole detection | [README](Path-hole/README.md) |
| bert_for_emotion | BERT emotion classification | [README](bert_for_emotion/README.md) |
| cycle-GAN | Separate CycleGAN notebook; possible alternate/duplicate of style_transfer | [README](cycle-GAN/README.md) |
| tactron | Tacotron2 + HiFi-GAN text-to-speech inference | [README](tactron/README.md) |
| ESRGAN super-resolution | Pretrained ESRGAN TensorFlow Hub inference | [README](-%2034%20%E2%80%94%20Super-Resolution%20for%20Image%20Reconstruction%20using%20GANs/README.md) |

## Image-only project reference — label 040

The repository contains an image labelled **40 — License Plate Detection using YOLOv9**. It is retained as a project reference; a matching source implementation has not been established from the image alone.

![Project 040 — License Plate Detection using YOLOv9](40%20%E2%80%94%20License%20Plate%20Detection%20using%20YOLOv9.png)

## Reconciliation notes
- The ESRGAN folder label includes **034**, which conflicts with canonical Machine Learning Project 034 (Recommendation System). Do not silently assign or reuse that ID.
- cycle-GAN and style_transfer may be duplicate/alternate experiments; compare notebook contents before counting separately.
- YOLOv4 object detection and YOLOv11 pothole detection are distinct observed use cases unless source comparison proves otherwise.
- Image-only references are not executable implementations.

## Verification boundary
Static source/notebook inspection only. Notebooks were not rerun; saved outputs are not reproduced results. See [Documentation Coverage](../DOCUMENTATION_COVERAGE.md).
