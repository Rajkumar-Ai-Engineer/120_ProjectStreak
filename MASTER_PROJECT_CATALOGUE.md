# 120 Project Streak — Master Project Catalogue

> **Audit snapshot: 5 November 2026.** This catalogue consolidates the six domain indexes, numbered project records, supplemental source-bearing folders, image references and PDF references found in the repository. It deliberately distinguishes implemented/source-bearing folders from visual or document-only references.

## Repository status at a glance

| Evidence class | Count | Interpretation |
|---|---:|---|
| Canonical numbered projects | 62 | IDs 001–062 in the verified project register |
| Deep Learning supplemental source folders | 9 | Additional source-bearing candidates; IDs not assigned |
| Computer Vision supplemental source folders | 3 | Additional source-bearing candidates; IDs not assigned |
| NLP source-bearing folders | 15 | Includes explicitly labelled 067 and 068; 13 unnumbered |
| Data Analytics screenshot references | 16 | Visual references; no executable project source found in `da/` |
| Data Analytics PDF references | 5 | Source documents; page-level review required |
| Other image-only references | 12 | DL 1, GenAI 4, CV 3, NLP 4; not runnable projects by themselves |

**Important:** The repository name and target refer to 120 projects, but the current evidence does **not** establish 120 unique, numbered, implemented projects. The 62 numbered entries are the only currently consolidated canonical register. Supplemental entries must be reconciled against the original project catalogue before assigning IDs or claiming a final total of 120. A screenshot or PDF is a project lead, not proof of an implementation.

## Six domain indexes

| Domain | Current indexed evidence | Main index |
|---|---|---|
| Deep Learning | 10 canonical projects (001–010), 9 additional source-bearing folders, 1 image-only reference | [DeepLearning/README.md](DeepLearning/README.md) |
| Generative AI | 19 canonical projects (011–029), 4 image references associated with Project 081 / LLM Debug Lab | [GenerativeAI/README.md](GenerativeAI/README.md) |
| Machine Learning | 19 canonical projects (030–048) | [Machine_Learning/README.md](Machine_Learning/README.md) |
| Computer Vision | 14 canonical projects (049–062), 3 additional source-bearing folders, 3 image-only references | [computer vision/README.md](computer%20vision/README.md) |
| NLP | 15 source-bearing folders (including labelled 067/068), 4 image-only references | [nlp/README.md](nlp/README.md) |
| Data Analytics | 16 screenshot references and 5 PDF sources; no executable project source identified in `da/` | [da/README.md](da/README.md) |

## Canonical numbered register

The complete 62-row numbered register, including project names, domains, technologies, paths and individual README links, is maintained in [PROJECT_INVENTORY.md](PROJECT_INVENTORY.md). The IDs currently run from 001 to 062. Domain-level descriptions and source notes are maintained in each index linked above.

### Canonical ranges

| IDs | Domain | Count |
|---|---|---:|
| 001–010 | Deep Learning | 10 |
| 011–029 | Generative AI | 19 |
| 030–048 | Machine Learning | 19 |
| 049–062 | Computer Vision | 14 |
| **Total** | | **62** |

NLP and Data Analytics contain additional evidence, but their source-derived folders and references are not fully reconciled to unique canonical IDs.

## Supplemental source-bearing projects

These are separate source-bearing folders discovered in the repository. They are indexed here without inventing IDs.

### Deep Learning — 9 candidates

| Project / folder | Source index |
|---|---|
| DC-GAN | [Project README](DeepLearning/DC-GAN/README.md) |
| DeepFake | [Project README](DeepLearning/DeepFake/README.md) |
| GPT-2 | [Project README](DeepLearning/GPT-2/README.md) |
| ImageCaption | [Project README](DeepLearning/ImageCaption/README.md) |
| Path-hole / YOLOv11 pothole detection | [Project README](DeepLearning/Path-hole/README.md) |
| BERT for emotion | [Project README](DeepLearning/bert_for_emotion/README.md) |
| cycle-GAN | [Project README](DeepLearning/cycle-GAN/README.md) |
| Tacotron | [Project README](DeepLearning/tactron/README.md) |
| ESRGAN super-resolution | [Project README](DeepLearning/-%2034%20%E2%80%94%20Super-Resolution%20for%20Image%20Reconstruction%20using%20GANs/README.md) |

### Computer Vision — 3 candidates

| Project / folder | Source index |
|---|---|
| Video Summarization using OpenAI Whisper | [Project README](computervision/-%2057%20%E2%80%94%20Video%20Summarization%20using%20OpenAI%20Whisper/README.md) |
| AI Image Captioning for Social Media | [Project README](computervision/58_—_ai_image_captioning_for_social_media_content_using_gemini/README.md) |
| Detectron2 Instance Segmentation | [Project README](computervision/Instance-Segmentation/README.md) |

### NLP — 15 source-bearing folders

See the full source-derived list and implementation caveats in [nlp/README.md](nlp/README.md). It includes COVID19Researcher, QuestionAnswering, IMDB LSTM, TextClassifyusingnb, TopicModelling, Emotion XLM-R, Resume Parser, sentiment_analysis_bert, Speech-to-Text, Science Paper Summarizer, Text Clustering, Text Summarization, Voice Assistant, Project 067 Multilingual Sentiment Analysis and Project 068 Text Generation using GPT-Neo. The two numbered folder labels are preserved; the remaining 13 have no canonical IDs assigned in the current register.

## Image-only project references

The images below are retained as project evidence and are explicitly **not** counted as source implementations. Open each domain index for the embedded images and additional detail.

| Domain | Reference | Repository asset / index |
|---|---|---|
| Deep Learning | 040 — License Plate Detection using YOLOv9 | [PNG](DeepLearning/40%20%E2%80%94%20License%20Plate%20Detection%20using%20YOLOv9.png) · [Index](DeepLearning/README.md) |
| Generative AI | Project 081 visual-flow / LLM Debug Lab reference set (3 numbered 81 assets + 1 unnumbered) | [Reference index](genai/README.md) |
| Computer Vision | 044 — YOLOv8 + ByteTrack | [Reference index](computervision/README.md) |
| Computer Vision | 052 — Virtual Calculator | [Reference index](computervision/README.md) |
| Computer Vision | 054 — AI-Powered Drowsiness Detection | [Reference index](computervision/README.md) |
| NLP | 063 — Named Entity Recognition using spaCy | [PNG](nlp/63%20%E2%80%94%20Named%20Entity%20Recognition%20using%20SpaCy.png) |
| NLP | 071 — Question Generation using LLaMA-8B | [PNG](nlp/-%2071%20%E2%80%94%20Question%20Generation%20using%20LLaMA-8B.png) |
| NLP | 073 — Document Similarity using BERT Embeddings + FAISS | [PNG](nlp/-%2073%20%E2%80%94%20Document%20Similarity%20Search%20using%20BERT%20Embeddings%20%2B%20FAISS.png) |
| NLP | Unnumbered — Text Generation using Falcon | [PNG](nlp/Text%20Generation%20using%20Falcon%20Model.png) |

### Data Analytics — screenshot references

All 16 screenshots and their individual evidence notes are linked from [da/README.md](da/README.md):

1. IPL Analysis 2025
2. House Price Analysis
3. Restaurant Food Sales
4. India Crime Analysis
5. COVID-19 Analysis
6. Healthcare Patient and Billing
7. Financial Portfolio Growth (Python reference)
8. Project 112 — Financial Portfolio Analysis
9. Reddit Sentiment Distribution
10. HR Attrition Dashboard
11. Employee Performance Dashboard
12. Movie Ratings Analysis
13. Product Sales 2010–2024
14. Sales Dashboard — City/Country
15. Online Retail Customer Segmentation
16. Unidentified screenshot (183235; classification pending)

### Data Analytics — PDF references

| Source label | PDF | Evidence note |
|---|---|---|
| 118 — World Wildlife | [PDF](da/118-world%20wildlife.pdf) | [Review note](da/source-pdfs/118-world-wildlife.md) |
| 120 — Job | [PDF](da/120-job.pdf) | [Review note](da/source-pdfs/120-job.md) |
| Unnumbered — Churn Analysis | [PDF](da/churn-analysis.pdf) | [Review note](da/source-pdfs/churn-analysis.md) |
| Unnumbered — Geospatial Coffee Sales | [PDF](da/geospatial-coffee-sales.pdf) | [Review note](da/source-pdfs/geospatial-coffee-sales.md) |
| Unnumbered — Retail Sales | [PDF](da/retail-sales.pdf) | [Review note](da/source-pdfs/retail-sales.md) |

PDF titles and screenshot labels are preserved as source labels. Do not assume that 118 or 120 represents a verified project number until the PDF contents and original catalogue are cross-checked.

## Numbering conflicts and unresolved matches

| Conflict / question | Safe handling |
|---|---|
| Deep Learning ESRGAN folder includes label 034; canonical ML 034 is Recommendation System | Keep both source records; do not reuse or silently reassign ID 034 |
| Supplemental CV labels 057 and 058 collide with canonical CV 057 Bar Reader and 058 Bird Species | Preserve both records pending source-catalogue validation |
| CV image-only 052 Virtual Calculator vs canonical CV 052 Moving Object Detection | Keep separate; image reference is not evidence of the canonical implementation |
| Deep Learning `cycle-GAN` vs `style_transfer` | Compare notebooks before counting as separate projects |
| Generative AI Project 081 image set | Four assets form one possible reference set, not four projects; source implementation not established |
| NLP labels 063, 071, 073 and unnumbered Falcon | Preserve as image-only references until matching source is found |
| Data Analytics labels 112, 118 and 120 | Preserve as source labels; verify against original catalogue and PDF contents |
| CV folder named Document Classification | Implementation evidence describes an AG News text classifier; flag domain mismatch rather than silently moving it |

## Audit and supporting records

- [PROJECT_INVENTORY.md](PROJECT_INVENTORY.md) — 62 canonical numbered projects.
- [DOCUMENTATION_COVERAGE.md](DOCUMENTATION_COVERAGE.md) — README and source documentation coverage.
- [documentation_inventory.json](documentation_inventory.json) — machine-readable static inventory.
- [COMPUTER_VISION_AUDIT.md](COMPUTER_VISION_AUDIT.md) — CV findings.
- [DATA_ANALYTICS_AUDIT.md](DATA_ANALYTICS_AUDIT.md) — Data Analytics evidence findings.
- [GENERATIVE_AI_AUDIT.md](GENERATIVE_AI_AUDIT.md) — GenAI findings.
- [NLP_AUDIT.md](NLP_AUDIT.md) — NLP findings.

## Counting rules

1. Count a project once when independent evidence supports one project boundary.
2. Do not count dataset images, model weights, output images, nested modules or duplicate experiments as separate projects.
3. Keep source-bearing folders, image-only references and PDF references in separate evidence classes.
4. Preserve original labels, even when they conflict; document the conflict.
5. Assign a canonical ID only after matching to the original 120-project source catalogue.
6. Do not describe a project as runnable, complete or verified solely because a README or screenshot exists.
7. The 120-project target remains a reconciliation goal, not a verified count in this snapshot.

**Maintainer:** Rajkumar V. · [GitHub profile](https://github.com/Rajkumar-Ai-Engineer) · [Repository](https://github.com/Rajkumar-Ai-Engineer/120_ProjectStreak)
