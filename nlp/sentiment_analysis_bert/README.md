# Sentiment Analysis BERT — Source/Folder Mismatch

**Domain:** NLP. **Source:** train.py.

## What the code actually does
Despite the folder name, the script loads spaCy's en_core_web_trf pipeline, reads text from the terminal, processes it and prints a spaCy Doc. It does not load a BERT sentiment classifier or produce sentiment labels/scores. Depending on enabled spaCy pipeline components, this performs general NLP tasks such as named-entity recognition.

## Findings
- Folder name and implementation do not match.
- Gradio is imported but unused.
- No training loop, sentiment label, evaluation dataset, fine-tuning or formatted inference output exists.
- The transformer pipeline can require substantial memory and model download time.

## Next steps
Rename/reclassify the folder to match spaCy text processing/NER, or implement a genuine sentiment workflow with labelled data, classifier, evaluation and inference UI. Do not describe the current source as BERT sentiment analysis. Static inspection only.
