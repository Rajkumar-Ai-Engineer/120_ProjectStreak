# IMDB Sequence Classification Using LSTM

**Domain:** NLP. **Notebook:** Sequence_Classification_on_IMDB_using_LSTM_.ipynb.

## Purpose and workflow
A TensorFlow/Keras binary sentiment classification exercise using the built-in IMDB movie-review dataset. It caps the vocabulary at 10,000 tokens, pads sequences to 200, uses a 128-dimensional embedding, an LSTM with 128 units, dropout 0.2 and a sigmoid Dense output. It compiles with Adam and binary cross-entropy, trains for 10 epochs and evaluates on the test split.

## Critical shape issue
The LSTM uses return_sequences=True, so it emits one hidden state per time step. The Dense layer therefore produces a sequence of predictions, while IMDB labels are one binary value per review. The output/loss shapes are inconsistent for the intended sequence-level classification. Use return_sequences=False or an explicit pooling layer before the classifier.

## Dependencies and verification
TensorFlow/Keras are required. Notebook source was inspected; training/evaluation were not run and no accuracy is claimed.

## Next steps
Fix output shape, add validation and reproducible seeds, report precision/recall/F1 and confusion matrix, and save model plus vocabulary/tokenization configuration.
