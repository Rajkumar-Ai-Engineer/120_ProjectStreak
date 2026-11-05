# Resume Parser — OCR and Gemini-Based Resume Extraction

**Domain:** NLP / Document AI. **Gradio entry point:** main.py.

## Pipeline
Gradio accepts a PIL image; Tesseract OCR extracts text using a hard-coded Windows executable path. The helper inserts OCR text into a prompt requesting name, email, phone, skills, education, experience and AI Engineer suitability. Google GenAI gemini-2.0-flash generates a text response displayed by Gradio.

## Configuration
Set GEMINI_API_KEY in .env. Install Google GenAI SDK, python-dotenv, Pillow, pytesseract and Gradio. Install Tesseract separately and configure its path for the host OS.

## Privacy and correctness findings
- The Tesseract path is hard-coded to one Windows installation.
- The prompt asks the model to judge candidate suitability; this can introduce bias and must not be used as an automated hiring decision.
- Resume images and extracted personal data are sent to an external LLM provider. Obtain authorization and disclose processing.
- No structured schema, PII redaction, retention policy, authentication or secure upload limits are implemented.
- Gradio launches with share=True and debug=True, unsafe for real resumes.
- API key and model ID are stored as one-element tuples because of trailing commas.

## Next steps
Use configurable OCR paths, private authenticated hosting, encrypted temporary storage and deletion, structured extraction, PII controls and human-reviewed job criteria. Static inspection only; OCR and Gemini were not run.
