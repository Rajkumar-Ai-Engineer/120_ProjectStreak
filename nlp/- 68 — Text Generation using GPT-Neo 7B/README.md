# Project 068 — Text Generation Using GPT-Neo

**Domain:** NLP / Language Generation. **Source:** 68_—_text_generation_using_gpt_neo_7b.py.

## Implementation
Loads EleutherAI/gpt-neo-2.7B tokenizer and causal language model from Hugging Face Transformers, sets the pad token to EOS, reads a prompt from the terminal, tokenizes it and generates one continuation with max_length 100, temperature 0.9 and top_k 50. The script sends both model and inputs to CUDA.

## Findings
- The source includes a notebook-only !pip install line; remove it before running as a normal Python script.
- The docstring says GPT-Neo 7B, but the actual checkpoint is gpt-neo-2.7B.
- CUDA is hard-coded; CPU-only machines fail. Device selection should be automatic.
- No attention-mask argument, generation seed, input validation, output comparison or evaluation is included.
- The script loads a large model and requires substantial GPU memory; no quantization or CPU fallback is implemented.

## Run
Install compatible PyTorch and Transformers versions, ensure sufficient GPU memory, remove the notebook magic and run the Python file. Model download requires network/cache access.

## Verification
Static inspection only; no checkpoint download or text generation was run.

## Next steps
Correct the project title, support CPU/GPU device selection, pass attention masks, configure max_new_tokens and sampling controls, and add reproducible prompt/output examples.
