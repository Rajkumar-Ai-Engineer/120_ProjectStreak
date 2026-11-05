# Master Project Inventory — 120 Project Streak

Audit snapshot: 2026-11-05. Repository: https://github.com/Rajkumar-Ai-Engineer/120_ProjectStreak

## Scope and interpretation

This is a consolidated inventory of project boundaries visible in the repository. It distinguishes the existing canonical register from additional source-bearing folders. The user-provided task specification describes how an external catalogue should be compared, but no separate authoritative 120-project catalogue or external reference files were attached in this task. Therefore this file is not a claim that all intended projects have been identified.

## Existing canonical register — 62 projects

The 62 rows below are the entries in the checked-in documentation_inventory.json and PROJECT_INVENTORY.md. Project IDs and paths are preserved.

| ID | Project | Domain | Repository path | Entry points | Detected imports (sample) | Documentation |
|---:|---|---|---|---|---|---|
| 001 | Ai Cyber | DeepLearning | DeepLearning/AI_cyber | test.py, train.ipynb | joblib, keras, keras.callbacks, keras.layers, keras.models, matplotlib.pyplot | README present |
| 002 | Brain Tumour | DeepLearning | DeepLearning/Brain_tumour | train.ipynb | keras.applications.vgg19, keras.callbacks, keras.layers, keras.models, keras.preprocessing.image, matplotlib.pyplot | README present |
| 003 | Human Pose | DeepLearning | DeepLearning/Human_pose | 1.ipynb | cv2, matplotlib.pyplot, numpy | README present |
| 004 | Seq Seq | DeepLearning | DeepLearning/SEQ_SEQ | transformer.ipynb | datasets, transformers | README present |
| 005 | Yolo | DeepLearning | DeepLearning/Yolo | train.ipynb | cv2, imutils, numpy, os | README present |
| 006 | 25 Face Mask Detector | DeepLearning | DeepLearning/maskdetector/25- Face Mask detector | test.py, train.ipynb | cv2, imutils, keras, keras.applications.mobilenet, keras.callbacks, keras.layers | README present |
| 007 | Preditive | DeepLearning | DeepLearning/preditive | gru1.ipynb | keras.callbacks, keras.layers, keras.models, keras.preprocessing.sequence, matplotlib.pyplot, tensorflow | README present |
| 008 | Speech | DeepLearning | DeepLearning/speech | train.ipynb | IPython.display, keras, keras.callbacks, keras.layers, keras.models, keras.utils | README present |
| 009 | Style Transfer | DeepLearning | DeepLearning/style_transfer | cycle_gan.ipynb | IPython.display, matplotlib.pyplot, os, tensorflow, tensorflow_datasets, tensorflow_examples.models.pix2pix | README present |
| 010 | Unet Image Segmentation | DeepLearning | DeepLearning/unet_image_segmentation | unet_is.ipynb | keras, keras.layers, tensorflow | README present |
| 011 | Agentaudit | GenerativeAI | GenerativeAI/AgentAuditAI/AgentAudit | main.py | autogen, dotenv, langsmith, logging, logs, os | README present |
| 012 | Autofixer | GenerativeAI | GenerativeAI/Autofixer | main.py | google, langchain, langchain_groq, os, re, streamlit | README present |
| 013 | Contextartitext | GenerativeAI | GenerativeAI/ContextArchitect/ContextArtitext | app.py, main.py | dotenv, helper, llama_index, logging, logs, os | README present |
| 014 | Decisionsim | GenerativeAI | GenerativeAI/DecisionSim | app.py, test.py | IPython, autogen, crewai, dotenv, helper, io | README present |
| 015 | Finsightai | GenerativeAI | GenerativeAI/FinSightAI | app.py, main.py | autogen, chromadb, dotenv, gradio, helper, langchain | README present |
| 016 | Insightserve | GenerativeAI | GenerativeAI/InsightServe | main.py | requests, streamlit | README present |
| 017 | Llmstudiopro | GenerativeAI | GenerativeAI/LLMStudioPro | app.py | dotenv, helper, json, langchain, langchain_community, langchain_groq | README present |
| 018 | Langaudit | GenerativeAI | GenerativeAI/LangAudit | helper.py | csv, datetime, dotenv, hashlib, json, langchain | README present |
| 019 | Mcq Generator | GenerativeAI | GenerativeAI/MCQ_GENERATOR | app.py, main.py | MCQ, dotenv, flask, json, langchain, langchain_groq | README present |
| 020 | Medicalsage | GenerativeAI | GenerativeAI/MedicalSage | app.py, main.py | dotenv, llama_index, main, os, pinecone, streamlit | README present |
| 021 | Projectpilot | GenerativeAI | GenerativeAI/ProjectPilot/ProjectPilot | main.py | crewai, crewai_tools, dotenv, langgraph, logging, logging_File | README present |
| 022 | Reportgenx | GenerativeAI | GenerativeAI/ReportGenx | main.py | dotenv, langchain, langchain_groq, matplotlib, numpy, os | README present |
| 023 | Schedulebot | GenerativeAI | GenerativeAI/ScheduleBOT/ScheduleBot | app.py, main.py | GoogleClient, datetime, dotenv, flask, google, google_auth_oauthlib | README present |
| 024 | Statechatai | GenerativeAI | GenerativeAI/StateChatAI | main.py | IPython, autogen, dotenv, langgraph, os, typing | README present |
| 025 | Taskmanager | GenerativeAI | GenerativeAI/TaskManager | main.py | agents_config, autogen, autogenagents, crewai, crewaiagents, dotenv | README present |
| 026 | Src | GenerativeAI | GenerativeAI/WebAutoGPT/src | app.py, main.py | bs4, dotenv, flask, helper, llama_index, os | README present |
| 027 | Docquery | GenerativeAI | GenerativeAI/docquery | Not identified |  | README present |
| 028 | Backend | GenerativeAI | GenerativeAI/genai_1/backend | main.py | fastapi, json, langchain | README present |
| 029 | Temp | GenerativeAI | GenerativeAI/genai_1/temp | main.py | fastapi, langflow | README present |
| 030 | Disease | Machine_Learning | Machine_Learning/Disease | CNN_Test.py | cv2, keras, numpy, tkinter | README present |
| 031 | Email Spam | Machine_Learning | Machine_Learning/Email_spam | train.ipynb | matplotlib.pyplot, nltk.corpus, numpy, pandas, pickle, regex | README present |
| 032 | Handgesture | Machine_Learning | Machine_Learning/HandGesture | train.ipynb | collections, cv2, keras.applications.resnet_v2, keras.layers, keras.models, matplotlib.pyplot | README present |
| 033 | Handwritten Digit Classification | Machine_Learning | Machine_Learning/Handwritten_digit_classification | train.ipynb | keras, keras.datasets, keras.models, matplotlib.pyplot, numpy, tensorflow | README present |
| 034 | Recommentation System | Machine_Learning | Machine_Learning/Recommentation_system | train.ipynb | numpy, pandas | README present |
| 035 | Sales Forecasting | Machine_Learning | Machine_Learning/Sales_forecasting | train.ipynb | matplotlib.pyplot, numpy, pandas, plotly.graph_objects, seaborn, sklearn.metrics | README present |
| 036 | Bert Text | Machine_Learning | Machine_Learning/bert_text | text_classify_bert.ipynb | datasets, torch, torch.utils.data, transformers | README present |
| 037 | Customersegmentation | Machine_Learning | Machine_Learning/customersegmentation | k_means.ipynb | matplotlib.pyplot, pandas, sklearn.cluster, sklearn.metrics, sklearn.preprocessing | README present |
| 038 | Facial Recognition | Machine_Learning | Machine_Learning/facial_recognition | en.py | cv2, face_recognition, numpy, os, pickle | README present |
| 039 | Frauddetection | Machine_Learning | Machine_Learning/frauddetection | main.py | fastapi, imblearn, joblib, matplotlib, numpy, pandas | README present |
| 040 | Image Classification With Multilabel | Machine_Learning | Machine_Learning/image_classification_with_multilabel | test.py, train.ipynb | PIL, json, keras, keras.layers, keras.models, keras.preprocessing.image | README present |
| 041 | Image Classify | Machine_Learning | Machine_Learning/image_classify | train.ipynb | keras.callbacks, keras.layers, keras.models, keras.preprocessing.image, matplotlib.pyplot, numpy | README present |
| 042 | Loan Prediction | Machine_Learning | Machine_Learning/loan_prediction | train.ipynb | matplotlib.pyplot, numpy, os, pandas, plotly.express, plotly.graph_objects | README present |
| 043 | Predictive Analysis Health Care | Machine_Learning | Machine_Learning/predictive_analysis_health_care | train.ipynb | category_encoders, imblearn.over_sampling, kagglehub, matplotlib.pyplot, numpy, pandas | README present |
| 044 | Predictive Maintenance System | Machine_Learning | Machine_Learning/predictive_maintenance_system | train.ipynb | imblearn.over_sampling, matplotlib.pyplot, numpy, pandas, sklearn.metrics, sklearn.model_selection | README present |
| 045 | Sentiment Analysis | Machine_Learning | Machine_Learning/sentiment_Analysis | train.ipynb | keras.callbacks, keras.datasets, keras.layers, keras.models, keras.preprocessing.sequence, keras.preprocessing.text | README present |
| 046 | Stock Price | Machine_Learning | Machine_Learning/stock_price | train.ipynb | matplotlib.pyplot, numpy, pandas, sklearn.linear_model, sklearn.metrics, sklearn.model_selection | README present |
| 047 | Timeseries | Machine_Learning | Machine_Learning/timeseries | train.ipynb | matplotlib.pyplot, numpy, pandas, plotly.express, seaborn, statsmodels.tsa.arima.model | README present |
| 048 | Traffic Prediction | Machine_Learning | Machine_Learning/traffic_prediction | train.ipynb | keras.callbacks, keras.layers, keras.models, matplotlib.pyplot, numpy, pandas | README present |
| 049 | Ar Based Virtual Makeup | computer vision | computer vision/AR_based_virtual_makeup | fm.ipynb | cv2, mediapipe, numpy | README present |
| 050 | Document Classifcation | computer vision | computer vision/Document_Classifcation | train.ipynb | datasets, keras.layers, keras.preprocessing.sequence, keras.preprocessing.text, nltk, numpy | README present |
| 051 | Image Colorization | computer vision | computer vision/Image_Colorization | train.py | PIL, cv2, matplotlib, numpy, streamlit | README present |
| 052 | Movingobjectdetection | computer vision | computer vision/MovingObjectDetection | mod1.py | cv2, imutils, numpy | README present |
| 053 | Ocr | computer vision | computer vision/OCR | test.py | cv2, pytesseract | README present |
| 054 | Pencilsketchconversion | computer vision | computer vision/PencilSketchConversion | pencil.py | PIL, cv2, numpy, tkinter | README present |
| 055 | Aerial Img | computer vision | computer vision/aerial_img | test.py | keras, numpy, tensorflow | README present |
| 056 | Ai Graffiti Removal | computer vision | computer vision/ai_graffiti_removal | test.py | cv2, matplotlib, numpy, os, random | README present |
| 057 | Bar Reader | computer vision | computer vision/bar_reader | bartest.py | pyzbar | README present |
| 058 | Birds Species | computer vision | computer vision/birds_species | test.ipynb | cv2, torch, ultralytics | README present |
| 059 | Face Recognition | computer vision | computer vision/face_recognition | collect_data.py | cv2, matplotlib, numpy, os | README present |
| 060 | Object Tracker | computer vision | computer vision/object_tracker | opencvtrackers_test.py | cv2, sys | README present |
| 061 | Simclr | computer vision | computer vision/simclr | main.py | numpy, tensorflow, tensorflow_datasets | README present |
| 062 | Speedestimation | computer vision | computer vision/speedEstimation | traffic.py | Roboflow, collections, cv2, numpy, os, supervision | README present |

## Additional source-bearing candidates — 27 folders

These have source code or notebooks and project-specific documentation, but they are not included in the 62-entry canonical register. They may be additional intended projects, alternate implementations, duplicates, or historical experiments. No canonical IDs are assigned except the explicit 067 and 068 labels.

| Candidate ID / source label | Project label | Repository path | Evidence summary | Reconciliation state |
|---|---|---|---|---|
| DL-C01 | Super-Resolution for Image Reconstruction using GANs | DeepLearning/- 34 — Super-Resolution for Image Reconstruction using GANs | Image/model inference notebook; candidate ID collision with existing ID 034 | Candidate; not reconciled to source catalogue |
| DL-C02 | DC-GAN | DeepLearning/DC-GAN | CIFAR-10 DCGAN notebook and script; discriminator output/loss mismatch noted | Candidate; not reconciled to source catalogue |
| DL-C03 | DeepFake Detection | DeepLearning/DeepFake | Deepfake image/video detection notebook; full pipeline not verified | Candidate; not reconciled to source catalogue |
| DL-C04 | GPT-2 and Transformer QA Demo | DeepLearning/GPT-2 | GPT-2 loading plus separate DistilBERT QA demo | Candidate; not reconciled to source catalogue |
| DL-C05 | Image Caption Generation | DeepLearning/ImageCaption | VGG16 plus LSTM Flickr8k captioning notebook | Candidate; not reconciled to source catalogue |
| DL-C06 | Pothole Detection with YOLOv11 Nano | DeepLearning/Path-hole | YOLOv11/Roboflow notebook; training not reproduced | Candidate; not reconciled to source catalogue |
| DL-C07 | BERT Emotion Classification | DeepLearning/bert_for_emotion | Six-label BERT emotion notebook; test split used for evaluation during training | Candidate; not reconciled to source catalogue |
| DL-C08 | CycleGAN Experiment | DeepLearning/cycle-GAN | Separate CycleGAN notebook; possible duplicate/alternate to ID 009 | Candidate; not reconciled to source catalogue |
| DL-C09 | Tacotron2 and HiFi-GAN TTS | DeepLearning/tactron | Pretrained speech synthesis inference notebook | Candidate; not reconciled to source catalogue |
| NLP-01 | COVID19Researcher | nlp/COVID19Researcher | Groq/Phidata research agent | Candidate; not reconciled to source catalogue |
| NLP-02 | QuestionAnswering | nlp/QuestionAnswering | BERT SQuAD extractive QA with Gradio | Candidate; not reconciled to source catalogue |
| NLP-03 | IMDB LSTM | nlp/Sequence Classification on IMDB using LSTM | TensorFlow/Keras review classifier | Candidate; not reconciled to source catalogue |
| NLP-04 | TextClassifyusingnb | nlp/TextClassifyusingnb | Large notebook; algorithm not fully verified | Candidate; not reconciled to source catalogue |
| NLP-05 | TopicModelling | nlp/TopicModelling | Gensim LDA topic modelling | Candidate; not reconciled to source catalogue |
| NLP-06 | Emotion XLM-R | nlp/finetuning_emotion_xberta | XLM-RoBERTa/GoEmotions fine-tuning | Candidate; not reconciled to source catalogue |
| NLP-07 | Resume Parser | nlp/resume_parser | Tesseract OCR, Gemini extraction, Gradio | Candidate; not reconciled to source catalogue |
| NLP-08 | sentiment_analysis_bert | nlp/sentiment_analysis_bert | Actual inspected code is spaCy transformer processing, not BERT sentiment | Candidate; not reconciled to source catalogue |
| NLP-09 | Speech-to-Text | nlp/speechtotext | Whisper/TensorFlow speech experiment | Candidate; not reconciled to source catalogue |
| NLP-10 | Science Paper Summarizer | nlp/summarizersciencepaper | Phidata/Groq search-assisted summarizer | Candidate; not reconciled to source catalogue |
| NLP-11 | Text Clustering | nlp/textClustering | Large notebook; algorithm not fully verified | Candidate; not reconciled to source catalogue |
| NLP-12 | Text Summarization | nlp/textsummarization | T5-base inference prototype | Candidate; not reconciled to source catalogue |
| NLP-13 | Voice Assistant | nlp/voice_assistant | Microphone, Whisper, Gemini, pyttsx3 | Candidate; not reconciled to source catalogue |
| 067 | Multilingual Sentiment Analysis with Gradio | nlp/67 — Multilingual Sentiment Analysis with Gradio App | Hugging Face multilingual 1–5 star model | Candidate; not reconciled to source catalogue |
| 068 | Text Generation using GPT-Neo 7B | nlp/- 68 — Text Generation using GPT-Neo 7B | Notebook actually references GPT-Neo 2.7B checkpoint | Candidate; not reconciled to source catalogue |
| CV-C01 | Video Summarization using OpenAI Whisper | computervision/- 57 — Video Summarization using OpenAI Whisper | Whisper transcription plus Transformers summarization | Candidate; not reconciled to source catalogue |
| CV-C02 | AI Image Captioning for Social Media | computervision/58_—_ai_image_captioning_for_social_media_content_using_gemini | GIT image captioning plus Gemini copy generation | Candidate; not reconciled to source catalogue |
| CV-C03 | Instance Segmentation | computervision/Instance-Segmentation | Detectron2 Mask R-CNN custom COCO training tutorial | Candidate; not reconciled to source catalogue |

## Non-code reference evidence

### Data Analytics folder

- 5 PDFs are present: 118-world wildlife.pdf, 120-job.pdf, churn-analysis.pdf, geospatial-coffee-sales.pdf, retail-sales.pdf.
- 16 screenshot assets are present. 15 have substantive screenshot-based notes; Screenshot 2026-11-03 183235.png remains retrieval-pending.
- 15 visible screenshot-based project topics are documented in da/projects/. They are visual evidence only and do not establish runnable code, source datasets, formulas, or reproducibility.
- PDF page-level content extraction was not completed in the existing DA audit. Project details and numbering in the PDFs must not be inferred from filenames alone.

### Image-only placeholders

- NLP: 4 image-only references, including labels 063, 071 and 073 plus a Falcon text-generation image.
- Computer Vision: 3 image-only folders with labels 044, 052 and 054. Their labels collide with other uses of those IDs in the repository.
- DeepLearning: a YOLOv9 license-plate-detection PNG exists outside a corresponding project folder.
- Root genai/: 4 PNG reference assets only.

## Current domain counts

| Domain / evidence group | Canonical register | Additional source-bearing candidates | Notes |
|---|---:|---:|---|
| DeepLearning | 10 | 9 | 19 project-like top-level directories; 9 are not canonically indexed |
| GenerativeAI | 19 | 0 | Separate root genai/ contains 4 image-only assets |
| Machine_Learning | 19 | 0 | 19 canonical entries |
| Computer Vision | 14 | 3 | Separate computervision/ path contains 3 code-bearing candidates and 3 image-only placeholders |
| NLP | 0 | 15 | 2 explicitly labelled 067/068; 13 unnumbered |
| Data Analytics | 0 | 15 screenshot topics | 5 PDFs also require page-level extraction; not counted as runnable projects |

## Counting rules

1. Count a project boundary, not every file, dataset, model, notebook, nested package, or build directory.
2. Keep exact canonical IDs and paths unchanged.
3. Treat a similar name as a candidate relationship, not proof of a duplicate or match.
4. Treat screenshots and PDFs as source evidence, not implementation evidence.
5. Do not assign IDs to unnumbered folders until the original catalogue is available.
6. Do not infer that IDs absent from the current repository are missing projects; the authoritative reference list is not present.

## Provenance

- Repository default branch: master.
- Repository tree inspected recursively through the GitHub Git Data API.
- Existing documentation_inventory.json, PROJECT_INVENTORY.md, README.md, domain indexes and audit reports were used as repository evidence.
- Static source/documentation review only; no project was executed as part of this repository-wide reconciliation snapshot.