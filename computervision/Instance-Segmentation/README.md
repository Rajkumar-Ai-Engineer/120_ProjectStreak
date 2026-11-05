# Instance Segmentation with Detectron2 on a Custom COCO Dataset

**Source:** [train_detectron2_segmentation_on_custom_data.py](train_detectron2_segmentation_on_custom_data.py)

## Purpose
A Colab-exported training tutorial showing how to run a pretrained Detectron2 Mask R-CNN model, register a COCO-format dataset, train on custom instance-segmentation data, and run inference on a validation split.

## Observed workflow
1. Check GPU/CUDA availability.
2. Install Detectron2 from its Git repository.
3. Load a pretrained COCO Mask R-CNN R-50-FPN 3x model and run a sample inference.
4. Download a Roboflow dataset in COCO segmentation format.
5. Register train, test and validation splits with Detectron2.
6. Configure `mask_rcnn_R_101_FPN_3x`, 3 classes, 2,000 iterations and base learning rate 0.001.
7. Train with `DefaultTrainer`.
8. Load `model_final.pth` and visualize predictions on validation images.

## Main technologies
Python, PyTorch, Detectron2, OpenCV, COCO annotations, Roboflow and CUDA.

## Critical security action
The source file contains a hard-coded Roboflow API key. It must be considered compromised because it is committed to the repository. Revoke/rotate it in Roboflow, remove it from the source and Git history as appropriate, and load a replacement from an environment variable or secret manager. Do not reproduce the value in docs.

## Code and reproducibility concerns
- The notebook downloads a dataset and assumes Colab/GPU/CUDA tooling.
- The source registers a test split but assigns `cfg.DATASETS.TEST` to it; the final manual visualization uses the validation split. Clarify the intended evaluation protocol.
- `NUM_CLASSES = 3` must match the dataset's foreground class count exactly.
- The final inference step assumes `model_final.pth` exists after training.
- Detectron2 installation is CUDA/PyTorch-version sensitive.
- Dataset version, annotation integrity, training logs and final checkpoint are not included in this directory.
- No reproducible environment lock or automated test is present.

## Execution boundary
This is a Colab tutorial script containing notebook magics and downloads. It was inspected statically, not executed. Do not interpret the presence of training code as evidence that a trained custom model or measured validation score is committed.

## Recommended next steps
Move credentials to secrets, parameterize dataset/model settings, pin compatible CUDA/PyTorch/Detectron2 versions, add dataset checks, save evaluation metrics and checkpoint metadata, and document class mapping and validation results.
