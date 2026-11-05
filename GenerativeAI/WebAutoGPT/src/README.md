# WebAutoGPT — Search, Web Extraction and LLM Research Prototype

**Project ID:** 026 · **Domain:** Generative AI  
**Flask UI:** `app.py` · **Research pipeline:** `helper.py`

## Purpose
A two-input Flask application that searches for web pages related to a user query, extracts page text, builds a LlamaIndex vector index and answers a second question over the collected documents.

## Implemented flow
1. The UI accepts a search/research query and a follow-up question.
2. `Reader` uses Zyte SERP when configured; otherwise it scrapes Google search HTML with Requests and BeautifulSoup.
3. `WebReader` uses Zyte web extraction when configured, otherwise `DirectScrape` fetches up to three URLs and extracts up to 2,000 characters of page text per URL.
4. The extracted documents are indexed with LlamaIndex.
5. The query engine uses the configured OpenAI LLM (GPT-4o) to answer the follow-up question.
6. Flask renders the returned answer in the page template.

## Configuration
Configure `OPENAI_API_KEY` and `zyteserp_api_key` (if using Zyte). The requirements file lists Flask, LlamaIndex, OpenAI, Playwright and related packages. The app also expects `templates/index.html`, which is not present in the inspected tree.

## Findings and risks
- Google search HTML scraping is brittle and may break as markup changes; the Requests call has no timeout.
- User-supplied URLs are fetched directly. Add strict URL validation, private-network blocking and redirect checks to reduce SSRF risk.
- The main helper uses up to three pages and truncates each to 2,000 characters; coverage is intentionally limited.
- The separate `reference.py` contains a literal placeholder OpenAI key and runs an example research task at import time; it is not the Flask app's active path and should be refactored before reuse.
- The Flask server uses `debug=True`; do not expose it in production.
- No citation rendering, prompt-injection isolation, source quality scoring, tests or research evaluation is implemented.

## Verification
Static inspection only; no web search, scraping or LLM request was run.

## Next steps
Use a supported search API, validate URLs and content, preserve source URLs and timestamps, defend against instructions embedded in retrieved pages, and add timeouts, tests and citations.
