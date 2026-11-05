# Video Summarization using OpenAI Whisper

**Source:** [_57_—_video_summarization_using_openai_whisper.py](_57_—_video_summarization_using_openai_whisper.py)

## Purpose
Transcribe speech from a video with Whisper and summarize the resulting transcript with a Hugging Face Transformers summarization pipeline.

## Observed flow
1. Load Whisper's `base` model.
2. Transcribe the hard-coded path `/content/videoplayback.mp4`.
3. Pass the transcript to `pipeline("summarization")`.
4. Print the transcript and summary.

## Dependencies
`openai-whisper`, `transformers`, and the model runtime (typically PyTorch).

## Limitations
- Colab-specific hard-coded input path; no CLI or upload flow.
- Summarization model is not pinned.
- No chunking for long transcripts, timestamps, speaker diarization, language controls, persistence, tests or quality evaluation.
- The exported source includes notebook-style `!pip` syntax, so it is not directly a standard Python script without adapting the install line.

## Verification
Static source inspection only; no model execution or summary-quality evaluation was performed.

## Next steps
Parameterize paths, pin model versions, implement chunked/hierarchical summarization, handle empty/failed transcription, add tests and record evaluation examples.
