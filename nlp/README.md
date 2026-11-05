# NLP — Natural Language Processing Project Collection

This directory contains source projects, notebooks and a small number of image-only reference assets. This is a source-derived index, not a claim that every notebook has been executed or every model result reproduced.

## Executable/source-bearing projects

| Project | Main task / implementation | Documentation |
|---|---|---|
| COVID19Researcher | Groq/Phidata search-assisted COVID research agent | [README](COVID19Researcher/README.md) |
| QuestionAnswering | Extractive BERT SQuAD question answering with Gradio | [README](QuestionAnswering/README.md) |
| IMDB LSTM | TensorFlow/Keras review sentiment classification | [README](Sequence%20Classification%20on%20IMDB%20using%20LSTM/README.md) |
| TextClassifyusingnb | Large text-classification notebook; exact method needs notebook verification | [README](TextClassifyusingnb/README.md) |
| TopicModelling | Gensim LDA topic modelling | [README](TopicModelling/README.md) |
| Emotion XLM-R | GoEmotions fine-tuning experiment with XLM-RoBERTa | [README](finetuning_emotion_xberta/README.md) |
| Resume Parser | Tesseract OCR + Gemini extraction + Gradio | [README](resume_parser/README.md) |
| sentiment_analysis_bert | Actual source is spaCy transformer NLP, not BERT sentiment | [README](sentiment_analysis_bert/README.md) |
| Speech-to-Text | TensorFlow/Hugging Face Whisper fine-tuning experiment | [README](speechtotext/README.md) |
| Science Paper Summarizer | Phidata/Groq agent with web search | [README](summarizersciencepaper/README.md) |
| Text Clustering | Large notebook; exact algorithm needs notebook verification | [README](textClustering/README.md) |
| Text Summarization | T5-base inference prototype | [README](textsummarization/README.md) |
| Voice Assistant | Microphone + Whisper + Gemini + pyttsx3 | [README](voice_assistant/README.md) |
| Project 067 — Multilingual Sentiment | Hugging Face multilingual 1–5 star model + Gradio | [README](67%20%E2%80%94%20Multilingual%20Sentiment%20Analysis%20with%20Gradio%20App/README.md) |
| Project 068 — GPT-Neo Text Generation | GPT-Neo 2.7B causal language generation | [README](-%2068%20%E2%80%94%20Text%20Generation%20using%20GPT-Neo%207B/README.md) |

## Image-only reference assets

- Project 063 — Named Entity Recognition using spaCy: PNG only; no executable implementation found in this folder.
- Project 071 — Question Generation using LLaMA-8B: PNG only; no executable implementation found.
- Project 073 — Document Similarity Search using BERT Embeddings + FAISS: PNG only; no executable implementation found.
- Text Generation using Falcon Model: PNG only; no executable implementation found.

These assets are not counted as runnable projects and do not prove that model code, weights or results are present.

## Audit summary
- 15 source-bearing project folders documented.
- 4 image-only assets identified separately.
- 13 READMEs added in the first pass; the remaining two numbered project READMEs are linked above.
- Two large notebooks could not be fully retrieved through the GitHub file-content endpoint, so their algorithm details are explicitly marked unverified.
- No training, inference, audio recording, OCR, web search or model API call was executed.

See [NLP implementation audit](../NLP_AUDIT.md) for defects, coverage and remediation priorities.
