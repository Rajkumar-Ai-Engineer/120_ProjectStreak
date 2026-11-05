# NLP Domain — Source-Based Implementation Audit

**Repository:** Rajkumar-Ai-Engineer/120_ProjectStreak  
**Path:** nlp/  
**Audit date:** 2026-11-05  
**Method:** Recursive Git tree inspection and static review of available Python files, notebooks and dependency manifests.

## 1. Executive summary

The NLP directory contains **15 source-bearing project folders** and **4 image-only reference assets**. The repository's existing PROJECT_INVENTORY.md did not include this directory. Two projects carry explicit catalogue labels in their folder names (067 and 068); the remaining folders are not assigned canonical IDs by this audit. IDs are not fabricated or inferred for unnumbered folders.

Project-specific README files have been created for all 15 source-bearing folders. The two large notebooks in TextClassifyusingnb and textClustering could not be retrieved in full through the GitHub file-content endpoint; their algorithms and results are explicitly marked unverified.

## 2. Project coverage

| Folder / project | Source evidence | Actual task / architecture | Key finding |
|---|---|---|---|
| 067 — Multilingual Sentiment Analysis with Gradio | Python script | Hugging Face nlptown multilingual BERT sentiment pipeline + Gradio | Model predicts 1–5 star ratings; notebook magic in .py; share/debug enabled |
| 068 — Text Generation using GPT-Neo 7B | Python script | Transformers causal generation using EleutherAI/gpt-neo-2.7B | Title says 7B but checkpoint is 2.7B; CUDA hard-coded; notebook magic |
| COVID19Researcher | main.py, helper.py, requirements | Streamlit + Phidata + Groq gemma2-9b-it + Google Search | Misleading API-key variable; no visible source citations |
| QuestionAnswering | Python script | BERT SQuAD extractive QA + Gradio | Notebook magic prevents ordinary Python execution; no context-length/no-answer handling |
| Sequence Classification on IMDB using LSTM | Notebook | TensorFlow/Keras embedding + LSTM binary classifier | return_sequences=True causes sequence output against one label per review |
| TextClassifyusingnb | Large notebook | Exact pipeline not independently confirmed | Full notebook unavailable from file-content endpoint; algorithm unverified |
| TopicModelling | Python script | NLTK preprocessing + Gensim LDA on five hard-coded documents | Misspelled unused token-filter variable; notebook shell commands in .py |
| finetuning_emotion_xberta | Notebook | XLM-RoBERTa + GoEmotions + Hugging Face Trainer | Dataset import/install mismatch; training data reused for evaluation; save API mismatch |
| resume_parser | main.py, helper.py | Tesseract OCR + Gemini 2.0 Flash + Gradio | Public share/debug enabled; PII privacy and hiring-bias concerns |
| sentiment_analysis_bert | train.py | spaCy en_core_web_trf text processing | Folder name says BERT sentiment, but code is spaCy pipeline and does not output sentiment |
| speechtotext | Notebook | LibriSpeech + TensorFlow + Whisper fine-tuning/transcription | Dependency typo, checkpoint mismatch, silent-audio division by zero, padding/loss concerns |
| summarizersciencepaper | main.py, helper.py | Phidata/Groq agent + DuckDuckGo search for paper summaries | No DOI/arXiv metadata verification or citations |
| textClustering | Large notebook | Exact clustering method not independently confirmed | Full notebook unavailable from file-content endpoint; algorithm unverified |
| textsummarization | summarize.py | T5-base summarization inference | Empty input and incorrect tokenizer/generate argument names |
| voice_assistant | Notebook | sounddevice + Whisper + Gemini + pyttsx3 | Recorded waveform is not passed into transcription path; fixed silence threshold |

## 3. Image-only assets (not counted as runnable projects)

- Project 063 — Named Entity Recognition using spaCy.png
- Project 071 — Question Generation using LLaMA-8B.png
- Project 073 — Document Similarity Search using BERT Embeddings + FAISS.png
- Text Generation using Falcon Model.png

These files are images only in the inspected tree. They do not establish that source code, model weights, datasets or reproducible results exist. The corresponding source projects should be located before assigning implementation status.

## 4. Cross-cutting issues

### 4.1 Reproducibility and packaging
Several project scripts contain notebook-only shell commands such as !pip install, which are invalid in ordinary .py execution. Multiple project folders lack a dedicated requirements file or pinned versions. Add a consistent Python version, dependency lock/requirements file and clean setup instructions.

### 4.2 Model/task alignment
- The multilingual sentiment model is a 1–5 star rating model; do not silently describe it as a three-class polarity model.
- The folder sentiment_analysis_bert does not implement BERT sentiment classification.
- GoEmotions is multi-label and requires explicit label encoding, problem type and suitable metrics.
- The IMDB LSTM currently emits sequence-level predictions due to return_sequences=True, incompatible with one binary label per review.

### 4.3 Evaluation gaps
No reliable cross-project benchmark was found. Recommended task-specific evaluation:
- Sentiment: macro/micro F1, per-language results, confusion matrix.
- Extractive QA: Exact Match and token-level F1.
- Text classification: precision, recall, macro-F1 and class balance.
- Topic modelling: coherence, stability and human interpretation.
- Clustering: silhouette where appropriate, cluster-size analysis and human review.
- Summarization: ROUGE/BERTScore plus factuality review.
- Speech recognition: WER and CER on held-out audio.
- Generation: human review for relevance, coherence and factuality; avoid relying on a single automatic score.

### 4.4 Privacy and security
- Resume Parser handles personal data and sends OCR text to Gemini. Add consent, access control, data minimization and deletion; do not use LLM suitability output as an automated hiring decision.
- Gradio public sharing is enabled in the inspected sentiment and resume apps. Disable by default for personal or sensitive inputs.
- Voice assistant captures microphone audio and sends transcript text to an external model; disclose and control that processing.
- COVID and research-paper agents need dated sources and visible citations, not unsupported claims of original research.

### 4.5 Speech pipeline correctness
The Whisper notebook has preprocessing/checkpoint inconsistencies and needs padding-mask review. The voice assistant's captured recording is not used by the transcription call. These need code corrections and held-out WER/CER or end-to-end tests before claiming working speech systems.

## 5. Documentation created

- [NLP project index](nlp/README.md)
- 15 project-specific README files under nlp/
- [Repository documentation coverage](DOCUMENTATION_COVERAGE.md)

## 6. Verification boundaries

- Static inspection only; no notebook cells or Python scripts were executed.
- No model weights were downloaded; no training, inference, OCR, microphone capture, speech playback, Gradio/Streamlit server, search request or external API call was performed.
- TextClassifyusingnb and textClustering notebooks were too large for the available GitHub file-content retrieval path; their detailed internals remain unverified.
- Image-only reference assets are not treated as executable projects.
- Existing canonical project IDs were not renumbered; unnumbered NLP folders remain unassigned pending reconciliation with the original catalogue.

## 7. Recommended remediation order

1. Correct the IMDB LSTM output shape and XLM-RoBERTa multi-label training/evaluation setup.
2. Fix T5 summarization input and Transformers argument names.
3. Fix Whisper dependencies, checkpoint consistency, audio normalization and label masking.
4. Connect the voice assistant's recorded audio directly to transcription and load Whisper once.
5. Correct folder/project naming mismatches and the GPT-Neo checkpoint/title discrepancy.
6. Disable public Gradio sharing by default and add privacy controls to Resume Parser.
7. Add citations and authoritative source verification to research agents.
8. Inspect the two large notebooks in a notebook-capable environment and document the actual classification/clustering algorithms.
9. Add pinned dependencies, tests and task-specific evaluation to all runnable projects.
