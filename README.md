# 120 Project Streak — Master Project Catalogue

A consolidated navigation hub for all six project domains and their implementation/reference documentation.

> **Important inventory status:** the existing canonical register currently verifies **62 numbered project entries (001–062)**. Additional project folders, image references and PDF sources exist beyond those 62. They are included below as candidates or source-only references, not silently counted as verified implementations. The repository's 120-project target is not yet evidence-backed as 120 unique runnable projects.

## Six domain indexes

| Domain | Current evidence | Main README |
|---|---|---|
| Deep Learning | 10 canonical projects (001–010), 9 additional source-bearing folders, image references including labels 034 and 040 | [DeepLearning/README.md](DeepLearning/README.md) |
| Generative AI | 19 canonical projects (011–029), four reference images associated with Project 081 | [GenerativeAI/README.md](GenerativeAI/README.md) |
| Machine Learning | 19 canonical projects (030–048) | [Machine_Learning/README.md](Machine_Learning/README.md) |
| Computer Vision | 14 canonical projects (049–062), 3 additional source-bearing folders, 3 image-only folders | [computer vision/README.md](computer%20vision/README.md) |
| NLP | 15 source-bearing folders (including labelled 067/068), 4 image-only references | [nlp/README.md](nlp/README.md) |
| Data Analytics | 16 screenshot references and 5 PDF sources; no executable project source found in da/ | [da/README.md](da/README.md) |

## Canonical project register — IDs 001–062

The following table preserves every entry currently in the repository's canonical project index. Each link points to the project-specific README. Implementation completeness and runtime verification are separate; see each project page.

| No. | Project | Domain | Primary language | Detected technologies | Documentation |
|---:|---|---|---|---|---|
| 001 | [Ai Cyber](DeepLearning/AI_cyber/README.md) | DeepLearning | Python | joblib, keras, keras.callbacks, keras.layers, keras.models |
| 002 | [Brain Tumour](DeepLearning/Brain_tumour/README.md) | DeepLearning | Python | keras.applications.vgg19, keras.callbacks, keras.layers, keras.models, keras.preprocessing.image |
| 003 | [Human Pose](DeepLearning/Human_pose/README.md) | DeepLearning | Python | cv2, matplotlib.pyplot, numpy |
| 004 | [Seq Seq](DeepLearning/SEQ_SEQ/README.md) | DeepLearning | Python | datasets, transformers |
| 005 | [Yolo](DeepLearning/Yolo/README.md) | DeepLearning | Python | cv2, imutils, numpy, os |
| 006 | [25 Face Mask Detector](DeepLearning/maskdetector/25- Face Mask detector/README.md) | DeepLearning | Python | cv2, imutils, keras, keras.applications.mobilenet, keras.callbacks |
| 007 | [Preditive](DeepLearning/preditive/README.md) | DeepLearning | Python | keras.callbacks, keras.layers, keras.models, keras.preprocessing.sequence, matplotlib.pyplot |
| 008 | [Speech](DeepLearning/speech/README.md) | DeepLearning | Python | IPython.display, keras, keras.callbacks, keras.layers, keras.models |
| 009 | [Style Transfer](DeepLearning/style_transfer/README.md) | DeepLearning | Python | IPython.display, matplotlib.pyplot, os, tensorflow, tensorflow_datasets |
| 010 | [Unet Image Segmentation](DeepLearning/unet_image_segmentation/README.md) | DeepLearning | Python | keras, keras.layers, tensorflow |
| 011 | [Agentaudit](GenerativeAI/AgentAuditAI/AgentAudit/README.md) | GenerativeAI | Python | autogen, dotenv, langsmith, logging, logs |
| 012 | [Autofixer](GenerativeAI/Autofixer/README.md) | GenerativeAI | Python | google, langchain, langchain_groq, os, re |
| 013 | [Contextartitext](GenerativeAI/ContextArchitect/ContextArtitext/README.md) | GenerativeAI | Python | dotenv, helper, llama_index, logging, logs |
| 014 | [Decisionsim](GenerativeAI/DecisionSim/README.md) | GenerativeAI | Python | IPython, autogen, crewai, dotenv, helper |
| 015 | [Finsightai](GenerativeAI/FinSightAI/README.md) | GenerativeAI | Python | autogen, chromadb, dotenv, gradio, helper |
| 016 | [Insightserve](GenerativeAI/InsightServe/README.md) | GenerativeAI | Python | requests, streamlit |
| 017 | [Llmstudiopro](GenerativeAI/LLMStudioPro/README.md) | GenerativeAI | Python | dotenv, helper, json, langchain, langchain_community |
| 018 | [Langaudit](GenerativeAI/LangAudit/README.md) | GenerativeAI | Python | csv, datetime, dotenv, hashlib, json |
| 019 | [Mcq Generator](GenerativeAI/MCQ_GENERATOR/README.md) | GenerativeAI | Python | MCQ, dotenv, flask, json, langchain |
| 020 | [Medicalsage](GenerativeAI/MedicalSage/README.md) | GenerativeAI | Python | dotenv, llama_index, main, os, pinecone |
| 021 | [Projectpilot](GenerativeAI/ProjectPilot/ProjectPilot/README.md) | GenerativeAI | Python | crewai, crewai_tools, dotenv, langgraph, logging |
| 022 | [Reportgenx](GenerativeAI/ReportGenx/README.md) | GenerativeAI | Python | dotenv, langchain, langchain_groq, matplotlib, numpy |
| 023 | [Schedulebot](GenerativeAI/ScheduleBOT/ScheduleBot/README.md) | GenerativeAI | Python | GoogleClient, datetime, dotenv, flask, google |
| 024 | [Statechatai](GenerativeAI/StateChatAI/README.md) | GenerativeAI | Python | IPython, autogen, dotenv, langgraph, os |
| 025 | [Taskmanager](GenerativeAI/TaskManager/README.md) | GenerativeAI | Python | agents_config, autogen, autogenagents, crewai, crewaiagents |
| 026 | [Src](GenerativeAI/WebAutoGPT/src/README.md) | GenerativeAI | Python | bs4, dotenv, flask, helper, llama_index |
| 027 | [Docquery](GenerativeAI/docquery/README.md) | GenerativeAI | Not specified | Not specified |
| 028 | [Backend](GenerativeAI/genai_1/backend/README.md) | GenerativeAI | Python | fastapi, json, langchain |
| 029 | [Temp](GenerativeAI/genai_1/temp/README.md) | GenerativeAI | Python | fastapi, langflow |
| 030 | [Disease](Machine_Learning/Disease/README.md) | Machine_Learning | Python | cv2, keras, numpy, tkinter |
| 031 | [Email Spam](Machine_Learning/Email_spam/README.md) | Machine_Learning | Python | matplotlib.pyplot, nltk.corpus, numpy, pandas, pickle |
| 032 | [Handgesture](Machine_Learning/HandGesture/README.md) | Machine_Learning | Python | collections, cv2, keras.applications.resnet_v2, keras.layers, keras.models |
| 033 | [Handwritten Digit Classification](Machine_Learning/Handwritten_digit_classification/README.md) | Machine_Learning | Python | keras, keras.datasets, keras.models, matplotlib.pyplot, numpy |
| 034 | [Recommentation System](Machine_Learning/Recommentation_system/README.md) | Machine_Learning | Python | numpy, pandas |
| 035 | [Sales Forecasting](Machine_Learning/Sales_forecasting/README.md) | Machine_Learning | Python | matplotlib.pyplot, numpy, pandas, plotly.graph_objects, seaborn |
| 036 | [Bert Text](Machine_Learning/bert_text/README.md) | Machine_Learning | Python | datasets, torch, torch.utils.data, transformers |
| 037 | [Customersegmentation](Machine_Learning/customersegmentation/README.md) | Machine_Learning | Python | matplotlib.pyplot, pandas, sklearn.cluster, sklearn.metrics, sklearn.preprocessing |
| 038 | [Facial Recognition](Machine_Learning/facial_recognition/README.md) | Machine_Learning | Python | cv2, face_recognition, numpy, os, pickle |
| 039 | [Frauddetection](Machine_Learning/frauddetection/README.md) | Machine_Learning | Python | fastapi, imblearn, joblib, matplotlib, numpy |
| 040 | [Image Classification With Multilabel](Machine_Learning/image_classification_with_multilabel/README.md) | Machine_Learning | Python | PIL, json, keras, keras.layers, keras.models |
| 041 | [Image Classify](Machine_Learning/image_classify/README.md) | Machine_Learning | Python | keras.callbacks, keras.layers, keras.models, keras.preprocessing.image, matplotlib.pyplot |
| 042 | [Loan Prediction](Machine_Learning/loan_prediction/README.md) | Machine_Learning | Python | matplotlib.pyplot, numpy, os, pandas, plotly.express |
| 043 | [Predictive Analysis Health Care](Machine_Learning/predictive_analysis_health_care/README.md) | Machine_Learning | Python | category_encoders, imblearn.over_sampling, kagglehub, matplotlib.pyplot, numpy |
| 044 | [Predictive Maintenance System](Machine_Learning/predictive_maintenance_system/README.md) | Machine_Learning | html | imblearn.over_sampling, matplotlib.pyplot, numpy, pandas, sklearn.metrics |
| 045 | [Sentiment Analysis](Machine_Learning/sentiment_Analysis/README.md) | Machine_Learning | Python | keras.callbacks, keras.datasets, keras.layers, keras.models, keras.preprocessing.sequence |
| 046 | [Stock Price](Machine_Learning/stock_price/README.md) | Machine_Learning | Python | matplotlib.pyplot, numpy, pandas, sklearn.linear_model, sklearn.metrics |
| 047 | [Timeseries](Machine_Learning/timeseries/README.md) | Machine_Learning | Python | matplotlib.pyplot, numpy, pandas, plotly.express, seaborn |
| 048 | [Traffic Prediction](Machine_Learning/traffic_prediction/README.md) | Machine_Learning | Python | keras.callbacks, keras.layers, keras.models, matplotlib.pyplot, numpy |
| 049 | [Ar Based Virtual Makeup](computer vision/AR_based_virtual_makeup/README.md) | computer vision | Python | cv2, mediapipe, numpy |
| 050 | [Document Classifcation](computer vision/Document_Classifcation/README.md) | computer vision | Python | datasets, keras.layers, keras.preprocessing.sequence, keras.preprocessing.text, nltk |
| 051 | [Image Colorization](computer vision/Image_Colorization/README.md) | computer vision | Python | PIL, cv2, matplotlib, numpy, streamlit |
| 052 | [Movingobjectdetection](computer vision/MovingObjectDetection/README.md) | computer vision | Python | cv2, imutils, numpy |
| 053 | [Ocr](computer vision/OCR/README.md) | computer vision | Python | cv2, pytesseract |
| 054 | [Pencilsketchconversion](computer vision/PencilSketchConversion/README.md) | computer vision | Python | PIL, cv2, numpy, tkinter |
| 055 | [Aerial Img](computer vision/aerial_img/README.md) | computer vision | Python | keras, numpy, tensorflow |
| 056 | [Ai Graffiti Removal](computer vision/ai_graffiti_removal/README.md) | computer vision | Python | cv2, matplotlib, numpy, os, random |
| 057 | [Bar Reader](computer vision/bar_reader/README.md) | computer vision | Python | pyzbar |
| 058 | [Birds Species](computer vision/birds_species/README.md) | computer vision | Python | cv2, torch, ultralytics |
| 059 | [Face Recognition](computer vision/face_recognition/README.md) | computer vision | Python | cv2, matplotlib, numpy, os |
| 060 | [Object Tracker](computer vision/object_tracker/README.md) | computer vision | Python | cv2, sys |
| 061 | [Simclr](computer vision/simclr/README.md) | computer vision | Python | numpy, tensorflow, tensorflow_datasets |
| 062 | [Speedestimation](computer vision/speedEstimation/README.md) | computer vision | Python | Roboflow, collections, cv2, numpy, os |

## Additional project folders and reference sources

### Deep Learning
- Nine additional documented source-bearing directories: DC-GAN, DeepFake, GPT-2, ImageCaption, Path-hole, bert_for_emotion, cycle-GAN, tactron and ESRGAN super-resolution. See [DeepLearning index](DeepLearning/README.md).
- [Project 040 — License Plate Detection using YOLOv9](DeepLearning/40%20%E2%80%94%20License%20Plate%20Detection%20using%20YOLOv9.png) is an image-only reference.
- The ESRGAN folder label includes 034, which conflicts with canonical ML Project 034 (Recommendation System).

### Generative AI
- Four PNGs in [genai/](genai/README.md): three files labelled 81 and one unnumbered LLM Debug Lab image. They are one possible Project 081 reference set, not four separate implementations.

### Computer Vision
- Additional source-bearing folders: Video Summarization using Whisper, AI Image Captioning for Social Media and Detectron2 Instance Segmentation.
- Image-only references: 044 YOLOv8 + ByteTrack, 052 Virtual Calculator and 054 AI-Powered Drowsiness Detection.
- Supplemental labels 057/058 conflict with canonical CV labels 057 Bar Reader and 058 Bird Species. See [supplemental index](computervision/README.md).

### NLP
- 15 source-bearing folders are indexed in [nlp/README.md](nlp/README.md); labels 067 and 068 are preserved.
- Image-only references: [063 NER using spaCy](nlp/63%20%E2%80%94%20Named%20Entity%20Recognition%20using%20SpaCy.png), [071 Question Generation using LLaMA-8B](nlp/-%2071%20%E2%80%94%20Question%20Generation%20using%20LLaMA-8B.png), [073 Document Similarity using BERT + FAISS](nlp/-%2073%20%E2%80%94%20Document%20Similarity%20Search%20using%20BERT%20Embeddings%20%2B%20FAISS.png), and Text Generation using Falcon.

### Data Analytics
- 16 screenshot-based project references are listed in [da/README.md](da/README.md), including the Project 112 portfolio-analysis reference.
- Five PDFs are retained as sources: 118 World Wildlife, 120 Job, Churn Analysis, Geospatial Coffee Sales and Retail Sales. Page-level extraction is pending; titles are not inferred beyond filenames.

## Repository audit and machine-readable records
- [Canonical project inventory](PROJECT_INVENTORY.md)
- [Documentation coverage](DOCUMENTATION_COVERAGE.md)
- [Machine-readable documentation inventory](documentation_inventory.json)
- [Computer Vision audit](COMPUTER_VISION_AUDIT.md)
- [Data Analytics audit](DATA_ANALYTICS_AUDIT.md)
- [Generative AI audit](GENERATIVE_AI_AUDIT.md)
- [NLP audit](NLP_AUDIT.md)

## Counting and reconciliation rules
1. Canonical numbered entries remain 001–062 until the original catalogue resolves the additional labels.
2. Additional source-bearing folders are candidates until duplicates and aliases are checked.
3. Images and PDFs are project references, not proof of runnable source code.
4. Screenshot and PDF counts are not summed as unique projects because they may overlap.
5. Conflicting labels are retained and flagged; no project is silently renumbered.
6. The README does not claim that all 120 unique projects are implemented or verified.

**Author:** Rajkumar V. · [GitHub](https://github.com/Rajkumar-Ai-Engineer)
