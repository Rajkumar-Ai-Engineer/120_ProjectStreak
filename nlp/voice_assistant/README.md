# Voice Assistant — Whisper, Gemini and Text-to-Speech

**Domain:** NLP / Speech. **Notebook:** test.ipynb.

## Purpose and pipeline
The notebook prototype captures microphone audio with sounddevice in 100 ms chunks until two seconds of low amplitude, transcribes with local OpenAI Whisper base (English), sends the transcript to Gemini gemini-2.0-flash and speaks the response using pyttsx3.

## Configuration
Set GEMINI_API_KEY in .env. Imports require soundfile, sounddevice, Whisper, pyttsx3, NumPy, python-dotenv and Google GenAI, plus microphone/audio-device support.

## Findings
- The main block records audio, then separately prompts for an audio path; the captured recording is not passed into the transcription function. This breaks the intended live microphone flow.
- Whisper model is loaded inside the transcription function, adding repeated load latency.
- Fixed amplitude silence detection can stop during quiet speech or fail in noisy environments.
- Transcription is forced to English.
- No wake word, conversation memory, interruption handling, streaming response, privacy controls or tests are included.

## Next steps
Pass captured waveform directly to Whisper, load the model once, use voice activity detection, support language selection, add audio-device error handling and disclose that transcripts are sent to Gemini. Static inspection only; no audio or model execution.
