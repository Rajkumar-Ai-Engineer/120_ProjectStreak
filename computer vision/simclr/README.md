# SimCLR-Style Self-Supervised Learning Experiment

**Project ID:** 061 · **Entry point:** [main.py](main.py)

## Objective
Explore contrastive representation learning on CIFAR-10 using two augmented views of each image, a ResNet50 encoder and a projection head.

## Intended pipeline
Load CIFAR-10 → normalize images → create two random augmented views → encode/project both views → compute a temperature-scaled contrastive objective → update trainable weights with Adam.

## Technologies and configuration
TensorFlow/Keras, TensorFlow Datasets and NumPy. The source sets image size 32, batch size 256, projection dimension 128, temperature 0.5, 20 epochs and Adam learning rate 0.001.

## Critical implementation defects
- `input_shape=(IMG_SIZE, IMG_SIZE)` is missing the RGB channel dimension; expected shape is three-dimensional (for example, 32×32×3).
- `with tf.GradientTape as tape:` is missing the call parentheses; it should instantiate the tape context manager.
- The loss labels are `tf.range(batch_size_of_concatenated_features)`, which makes each embedding's own diagonal similarity the target. SimCLR requires paired-view positive indices and masking self-similarity; this implementation does not encode that objective correctly.
- `test_ds` is loaded but never used.
- The augmentation pipeline is declared, but the training step and model execution require correction before meaningful training.
- No projection/encoder checkpoint, downstream linear evaluation, retrieval evaluation or training metrics file is saved.

## Status
**Experimental code with blocking defects; successful SimCLR training is not established by the repository.**

## Verification
Static source inspection only; the training script was not executed. Do not report a model quality score.
