# Speech-to-Text — Whisper Fine-Tuning Experiment

**Domain:** NLP / Speech. **Notebook:** main.ipynb.

## Purpose and workflow
A TensorFlow and Hugging Face Whisper experiment. It loads LibriSpeech via TensorFlow Datasets, targets 16 kHz audio, resamples with librosa, extracts features with WhisperProcessor, defines a TensorFlow Whisper conditional-generation training step and provides a transcription helper using a local checkpoint.

## Findings
- The install cell misspells tensorflow-datasets as tensrflow-datasets.
- Normalization divides by maximum absolute audio amplitude without handling silence (division by zero).
- Preprocessing uses openai/whisper-small while the model factory loads openai/whisper; checkpoint consistency needs resolution.
- tf.py_function output shapes are not explicitly set.
- Padded label tokens need masking in the loss.
- Transcription expects local whisper_tf_epoch3 checkpoint, which is not guaranteed to exist.
- No WER/CER evaluation is provided.

## Next steps
Fix dependencies/checkpoint names, mask padding, set TensorFlow shapes, handle silence, validate data splits and report WER/CER on held-out audio. Static inspection only; no training or transcription executed.
