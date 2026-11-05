# Bird Species Detection with Ultralytics YOLO

**Project ID:** 058 · **Notebook:** [test.ipynb](test.ipynb)

## Objective
The folder contains a YOLO-based object-detection training run and a notebook that loads its saved best checkpoint. The project is labelled Bird Species Detection; the exact class names and dataset definition are not committed in the inspected directory.

## Training evidence
The saved `runs/detect/train/args.yaml` records:
- Ultralytics task: detection
- Model: `yolo11n.pt`
- 20 epochs, batch size 16, image size 640
- CUDA device, pretrained weights, deterministic mode enabled
- Validation enabled

The run directory includes `best.pt`, `last.pt`, plots, confusion matrices, batch visualizations and `results.csv`.

## Recorded final-epoch metrics
The final row of the committed training CSV (epoch 20) records precision 0.96081, recall 0.96842, mAP50 0.98361 and mAP50–95 0.83109. These are historical run artefacts, not independently reproduced results. They are meaningful only with the original dataset split, class mapping and evaluation configuration.

## Notebook behaviour
The notebook imports Ultralytics YOLO and loads `runs/detect/train/weights/best.pt` using `torch.load(..., weights_only=False)`, then wraps it in `YOLO`. It contains no further inference cells in the inspected notebook.

## Limitations and risks
- Dataset YAML and original dataset are absent; training configuration points to a Colab path `/content/ALL-6/data.yaml`.
- Class names, dataset source/version and split integrity cannot be verified here.
- `weights_only=False` uses pickle-based loading; only load trusted checkpoints.
- No reproducible prediction script or sample input is included.
- Model weights and run artefacts are large; document provenance and consider Git LFS or external artifact storage.

## Verification
Static inspection of notebook, YAML, CSV and saved artifacts only; model loading and inference were not run.
