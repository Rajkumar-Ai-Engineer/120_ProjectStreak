# QuestionAnswering — Extractive BERT Question Answering

**Domain:** NLP. **Entry point:** question_answering.py.

## Purpose and architecture
A Gradio interface accepts a question and context passage, then extracts an answer span using Transformers pipeline with bert-large-uncased-whole-word-masking-finetuned-squad. The answer_question function returns the pipeline answer field.

## Run
Install transformers and gradio, then run the script after removing the notebook-only !pip install line (or execute that line in a notebook environment).

## Findings
- This is extractive, context-dependent QA, not open-domain QA; answers must be grounded in the supplied passage.
- No maximum context handling, confidence display, no-answer threshold or input validation is configured.
- interface.launch uses share=True and debug=True; disable public sharing/debug outside controlled development.
- No requirements file or tests are present.

## Verification
Static inspection only; model weights were not downloaded and inference was not run.

## Next steps
Pin dependencies, validate context length, expose confidence/no-answer behavior, disable public sharing by default and add context-grounded tests.
