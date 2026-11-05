# AG News Text Classification with LSTM

**Project ID in current inventory:** 050 · **Current folder:** `computer vision/Document_Classifcation`

> **Domain correction:** Despite its current folder location and inventory label, this notebook performs text/news classification, not computer vision.

## Objective and dataset
Classify AG News articles into the dataset's four news categories using text tokenization, padded sequences and a recurrent neural network.

## Observed pipeline
1. Install TensorFlow, NLTK, Hugging Face `datasets` and NumPy.
2. Load the `ag_news` dataset with train and test splits.
3. Extract article text and labels.
4. Fit a Keras Tokenizer on training text with a 20,000-word vocabulary and OOV token.
5. Convert text to integer sequences and pad to a maximum sequence length of 100.
6. Build an embedding/LSTM/dense classification network and train/evaluate it (see notebook cells for exact layer configuration).

## Technologies
Python, Hugging Face Datasets, TensorFlow/Keras, NLTK and NumPy.

## Reproducibility
The notebook downloads the dataset and NLTK tokenizer data at runtime. No requirements file, saved model, test report or pinned versions are included.

## Audit notes
- This is NLP / text classification. Reconcile its domain placement and project number against the original catalogue before moving or renumbering it.
- Confirm that test data is used only for final evaluation and not model selection.
- Add class-name mapping, confusion matrix, per-class precision/recall/F1, seed control and a saved inference pipeline.
- Validate tokenizer and padding configuration at inference time.

## Verification
Notebook cells were inspected but not executed. No accuracy score is independently asserted.
