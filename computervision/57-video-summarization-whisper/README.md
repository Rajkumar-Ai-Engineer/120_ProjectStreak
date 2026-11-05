# Video Summarization using OpenAI Whisper

**Reference label:** 57 — Video Summarization using OpenAI Whisper  
**Source:** [_57_—_video_summarization_using_openai_whisper.py](_57_—_video_summarization_using_openai_whisper.py)

## Purpose
Transcribe speech from a video with Whisper, then summarize the transcript using a Hugging Face Transformers summarization pipeline.

## Observed pipeline
1. Install `transformers` and `openai-whisper` in a notebook/Colab environment.
2. Load the Whisper `base` model.
3. Transcribe the hard-coded video path `/content/videoplayback.mp4`.
4. Pass the transcript to `pipeline("summarization")`.
5. Print the transcript and generated summary.

## Dependencies
- `openai-whisper`
- `transformers`
- PyTorch (required by the model stack)

## Current limitations and defects
- The input path is fixed to a Google Colab path; there is no CLI or upload interface.
- The default summarization pipeline model is not pinned, so output and compatibility may vary.
- Long transcripts may exceed the summarizer model's input token limit; chunking and hierarchical summarization are absent.
- No timestamps, speaker diarization, language selection, transcript persistence, tests, or evaluation are implemented.
- The script contains notebook-style `!pip` syntax and is not directly valid as an ordinary Python script without removing/replacing that line.

## Run context
The file is a Colab-exported notebook script. Run in a compatible notebook after installing dependencies and changing the video path. This audit did not execute the model.

## Recommended next steps
Add configurable input/output paths, transcript chunking, pinned model IDs, error handling, language/timestamp options, tests, and summary-quality evaluation.
