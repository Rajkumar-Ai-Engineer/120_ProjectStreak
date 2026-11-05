# Autofixer — LLM-Assisted Code Error Repair

**Project ID:** 012 · **Domain:** Generative AI  
**Entry point:** `main.py`

## Purpose
A Streamlit interface that accepts a Python code snippet and its error message, asks a Groq-hosted chat model to propose a correction, and displays the returned text as Python code.

## Architecture and workflow
1. User enters source code and an error message in Streamlit text fields.
2. A LangChain `PromptTemplate` inserts both values into a code-repair instruction.
3. `ChatGroq` is configured with model `deepseek-r1-distill-llama-70b`.
4. The prompt and model are composed with the LangChain pipe operator.
5. `fix_code` invokes the chain, removes `<think>...</think>` blocks and remaining HTML-like tags, then returns the cleaned text.
6. Streamlit displays the proposed repair using `st.code`.

## Dependencies and configuration
The requirements file lists SuperAGI client, python-dotenv, LangChain, LangChain Groq, OpenAI and Google GenAI SDK. The main source also imports Streamlit, which is missing from the checked-in requirements. Configure `GROQ_API_KEY` in the environment.

## Findings and limitations
- `helper.py` creates a SuperAGI client with an empty API key; it is not used by the active Streamlit repair flow.
- The main file imports Google GenAI and reads `GROQ_API_KEY`, but the Google client and local variable are unused.
- The model response is shown to the user but is not parsed, syntax-checked, tested, diffed or applied to a file.
- Removing tags with a broad regular expression may also remove legitimate code text.
- There is no backup, patch review, test execution, rollback or safe execution sandbox.
- LLM-generated repairs can introduce new defects or unsafe code; review changes before use.

## Run
Install the listed dependencies plus Streamlit in a virtual environment, set `GROQ_API_KEY`, then run `streamlit run main.py`.

## Next steps
Return a unified diff, run syntax checks and isolated tests, show confidence/uncertainty, preserve the original file, add repair test cases, and remove or configure the unused SuperAGI client.
