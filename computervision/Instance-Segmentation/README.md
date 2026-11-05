# Detectron2 Instance Segmentation on Custom COCO Data

**Source:** [train_detectron2_segmentation_on_custom_data.py](train_detectron2_segmentation_on_custom_data.py)

## Purpose
Colab-exported tutorial for pretrained Mask R-CNN inference, COCO dataset registration, custom instance-segmentation training and validation-image visualization with Detectron2.

## Observed pipeline
1. Check GPU/CUDA availability and install Detectron2.
2. Run pretrained `COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml` inference.
3. Download a Roboflow dataset in COCO segmentation format.
4. Register train, test and validation splits.
5. Configure `mask_rcnn_R_101_FPN_3x`, 3 classes, 2,000 iterations and learning rate 0.001.
6. Train with `DefaultTrainer`.
7. Load `model_final.pth` and visualize predictions on validation images.

## Main technologies
Python, PyTorch, Detectron2, OpenCV, COCO annotations, Roboflow and CUDA.

## Security — action required
The committed source contains a literal Roboflow API credential. Treat it as exposed: revoke/rotate it, remove the literal from source and review Git history. Load replacement credentials from an environment variable or secret manager. The credential is intentionally not reproduced here.

## Reproducibility and code-review findings
- Colab, GPU, CUDA and notebook download assumptions are embedded in the script.
- Detectron2 installation depends on compatible PyTorch/CUDA versions.
- `NUM_CLASSES = 3` must match the dataset's foreground class count.
- The test split is assigned to `cfg.DATASETS.TEST`, while the final manual visualization iterates over the validation split; define one explicit evaluation protocol.
- The final inference stage assumes training created `model_final.pth`.
- Dataset version, class mapping, training output, checkpoint and measured evaluation report are not committed in this directory.
- Notebook magics and shell commands mean this exported file is not a clean portable Python module.

## Verification
Static code inspection only. No training, dataset download or inference was run. The presence of a training script is not proof that a custom trained model or validated score is available.

## Next steps
Rotate the credential, pin a compatible environment, parameterize dataset/model configuration, validate annotation/class mappings, save metrics and checkpoint metadata, and add a reproducible evaluation script.
