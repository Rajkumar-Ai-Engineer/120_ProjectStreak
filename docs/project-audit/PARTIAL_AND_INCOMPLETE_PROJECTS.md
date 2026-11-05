# Partial and Incomplete Projects

## Scope

This report combines static code-review findings already documented in the repository. It does not claim runtime verification. No scripts, notebooks, model training, inference, servers, external APIs, OCR or audio workflows were executed during this audit snapshot.

## Deep Learning — known issues

- AI Cyber: feature-selection leakage and inference feature-mapping concerns are noted in DOCUMENTATION_COVERAGE.md.
- Brain Tumour: dataset path assumptions and test-set validation concerns require review.
- Seq Seq: test split is used during training; restore a proper train/validation/test separation.
- YOLO: video frame handling and confidence/label interpretation need verification.
- Face Mask Detector: nested project path and end-to-end execution remain incompletely verified.
- Preditive (RNN/LSTM/GRU): test-set validation and swapped metric labels are noted.
- Speech Commands: checkpoint monitor mismatch requires correction.
- Style Transfer: preprocessing function uses an incorrect variable.
- U-Net: dataset loaders and output/mask setup remain unresolved.
- Additional candidate findings: DC-GAN discriminator output/loss mismatch and GPU-only pin; ImageCaption caption parsing/cleaning concerns; GPT-2 notebook mixes GPT-2 loading with a separate DistilBERT QA result; BERT emotion uses test data as evaluation during training and hard-codes CUDA; CycleGAN duplicate status unresolved.

## Generative AI — known issues

- Visual Flow LLM Backend: client-supplied API key and wildcard CORS are high-priority security concerns.
- Langflow JSON Loader API: missing route decorator noted.
- WebAutoGPT and DocQuery: URL/filename safety issues require hardening.
- MCQ Generator: placeholder Flask secret and heuristic quiz scoring need replacement.
- Multiple projects have environment-variable assignment defects.
- LangAudit relies on weak keyword-only evaluation.
- RAG applications should add source metadata, citations, retrieval evaluation, tenant/user index isolation and groundedness checks.
- Agent tools should use least privilege, sandbox generated code, and require confirmation before destructive operations.

## Machine Learning — verification state

The 19 canonical Machine_Learning entries have project-specific READMEs in the formal inventory. A separate consolidated Machine Learning audit report was not present at the inspected repository root. Do not infer that all models are correct or reproducible from README presence. Run the individual notebooks in clean environments and record held-out metrics, data leakage checks and dependency versions.

## Computer Vision — known issues

- Detectron2 instance-segmentation source contains an exposed Roboflow API credential; rotate the credential immediately and remove it from repository history if it was valid.
- Vehicle speed-estimation video generation is broken and the reported km/h values are not calibrated.
- SimCLR contains shape/tape/loss defects that block reliable training.
- Image Colorization is missing Caffe model weights.
- AG News text classification is filed under Computer Vision despite being an NLP/text task.
- Bar Reader is import-only; it does not load an image, invoke decoding or return a result.
- Several projects rely on hard-coded Colab/machine paths or missing model/data assets.

## NLP — known issues

- IMDB LSTM output shape is inconsistent with one binary label per review.
- XLM-RoBERTa multi-label training/evaluation configuration needs correction.
- T5 summarization has input and Transformers argument-name defects.
- Whisper speech workflow has dependency, checkpoint, padding/loss and preprocessing concerns.
- Voice Assistant captures audio but does not pass the captured waveform into the transcription call.
- Resume Parser processes personal data and enables public Gradio sharing; add consent, access controls, data minimization and deletion.
- sentiment_analysis_bert is a folder-name/source mismatch: inspected code is a spaCy pipeline and does not output sentiment.
- COVID and research agents need dated sources and visible citations.
- TextClassifyusingnb and textClustering notebook internals could not be fully retrieved through the GitHub file-content endpoint.

## Data Analytics — evidence gaps

- da/ contains 5 PDFs and 16 screenshots, but no Python, SQL, notebook, dashboard project source or dependency files were identified in that directory.
- 15 screenshots have substantive visual notes; one screenshot remains retrieval-pending.
- PDF page-level content extraction remains pending for all 5 PDFs.
- Dashboard values are transcribed as visible only; they have not been checked against raw data, formulas or source datasets.

## Cross-project remediation priorities

1. Rotate and remove exposed credentials; use secret managers and least-privilege tokens.
2. Fix data leakage and train/validation/test separation.
3. Add pinned dependencies, clean setup instructions and smoke tests.
4. Add task-appropriate evaluation: macro-F1, precision/recall, mAP, WER/CER, ROUGE/BERTScore, retrieval recall/precision and groundedness as appropriate.
5. Add dataset/model provenance, licenses, input/output examples and reproducible commands.
6. Add privacy controls for resumes, voice and other personal data.
7. Reconcile project aliases, duplicate candidates and conflicting numeric labels against the original catalogue.

## Verification boundary

Findings are static-review observations from repository source and existing audit documentation. Notebook outputs are historical artifacts, not independently reproduced results. See the individual project README files and domain audit reports for file-level details.