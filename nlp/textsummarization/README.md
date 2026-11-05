# Text Summarization — T5 Base Inference Prototype

**Domain:** NLP. **Entry point:** summarize.py.

## Purpose
Loads pretrained t5-base, prepends the task prefix "summarize:" to text, generates token IDs and decodes a summary.

## Critical code defects
- Source text is an empty string, so no meaningful content is summarized.
- Tokenizer output is accessed as .inputids; Transformers uses input_ids.
- Generation uses model.generate(inputs=inputids); use input_ids=input_ids or positional input IDs.
- No input interface, long-document chunking, evaluation, citations or summary-quality checks exist.
- No dependency manifest is present.

## Next steps
Correct tokenization/generation calls, add CLI/UI input, implement long-document chunking, set deterministic generation options and evaluate with ROUGE/BERTScore or human review. Static inspection only; no inference run.
