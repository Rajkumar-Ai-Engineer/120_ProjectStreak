# Natural Language Processing — Project Index

**Master catalogue:** [MASTER_PROJECT_CATALOGUE.md](../MASTER_PROJECT_CATALOGUE.md) · [Repository home](../README.md)

**Source-bearing project folders:** 15 · **Explicitly numbered folders:** 067 and 068  
**Audit:** [NLP_AUDIT.md](../NLP_AUDIT.md) · **Master catalogue:** [Repository README](../README.md)

This is a source-derived index. Existing folder labels are preserved; no IDs are assigned to unnumbered folders. Image-only references are shown separately and are not counted as runnable implementations.

## Source-bearing projects

| Project / folder | Main task / observed implementation | Documentation |
|---|---|---|
| COVID19Researcher | Groq/Phidata search-assisted COVID research agent | [README](COVID19Researcher/README.md) |
| QuestionAnswering | Extractive BERT SQuAD QA with Gradio | [README](QuestionAnswering/README.md) |
| IMDB LSTM | TensorFlow/Keras review sentiment classification | [README](Sequence%20Classification%20on%20IMDB%20using%20LSTM/README.md) |
| TextClassifyusingnb | Large text-classification notebook; exact method unverified | [README](TextClassifyusingnb/README.md) |
| TopicModelling | Gensim LDA topic modelling | [README](TopicModelling/README.md) |
| Emotion XLM-R | GoEmotions fine-tuning with XLM-RoBERTa | [README](finetuning_emotion_xberta/README.md) |
| Resume Parser | Tesseract OCR + Gemini extraction + Gradio | [README](resume_parser/README.md) |
| sentiment_analysis_bert | Source is spaCy transformer NLP, not BERT sentiment | [README](sentiment_analysis_bert/README.md) |
| Speech-to-Text | TensorFlow/Hugging Face Whisper experiment | [README](speechtotext/README.md) |
| Science Paper Summarizer | Phidata/Groq agent with web search | [README](summarizersciencepaper/README.md) |
| Text Clustering | Large notebook; exact algorithm unverified | [README](textClustering/README.md) |
| Text Summarization | T5-base inference prototype | [README](textsummarization/README.md) |
| Voice Assistant | Microphone + Whisper + Gemini + pyttsx3 | [README](voice_assistant/README.md) |
| 067 — Multilingual Sentiment Analysis with Gradio | Hugging Face multilingual 1–5 star sentiment model | [README](67%20%E2%80%94%20Multilingual%20Sentiment%20Analysis%20with%20Gradio%20App/README.md) |
| 068 — Text Generation using GPT-Neo 7B (folder title) | Source loads GPT-Neo 2.7B; title/checkpoint discrepancy documented | [README](-%2068%20%E2%80%94%20Text%20Generation%20using%20GPT-Neo%207B/README.md) |

## Image-only project references — source implementation not located

### 063 — Named Entity Recognition using spaCy
![Project 063 reference](63%20%E2%80%94%20Named%20Entity%20Recognition%20using%20SpaCy.png)

### 071 — Question Generation using LLaMA-8B
![Project 071 reference](-%2071%20%E2%80%94%20Question%20Generation%20using%20LLaMA-8B.png)

### 073 — Document Similarity Search using BERT Embeddings + FAISS
![Project 073 reference](-%2073%20%E2%80%94%20Document%20Similarity%20Search%20using%20BERT%20Embeddings%20%2B%20FAISS.png)

### Unnumbered — Text Generation using Falcon Model
![Falcon text generation reference](Text%20Generation%20using%20Falcon%20Model.png)

These four image assets establish project references only. They do not establish source code, trained weights, datasets or reproducible results. Locate and inspect matching source before changing implementation status.

## Reconciliation and verification notes
- The 15 folders include the two explicitly numbered folders 067 and 068; the remaining 13 have no canonical IDs assigned in the current inventory.
- Two large notebooks (TextClassifyusingnb and textClustering) could not be fully inspected through the available GitHub file-content path; algorithm details remain unverified.
- The folder sentiment_analysis_bert is a naming/implementation mismatch: inspected source uses spaCy and does not produce sentiment output.
- Static review only; no training, inference, OCR, audio capture, speech playback, server or external API was executed.
