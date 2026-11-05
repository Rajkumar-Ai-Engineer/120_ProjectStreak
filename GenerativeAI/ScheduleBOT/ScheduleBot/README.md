# ScheduleBot — Google Calendar Scheduling Agent

**Project ID:** 023 · **Domain:** Generative AI  
**Flask UI:** `app.py` · **Agent:** `main.py` · **Google API client:** `GoogleClient.py`

## Purpose
A conversational scheduling prototype using a Phidata Agent with a Groq model and Google Calendar tools. The agent description instructs it to use India Standard Time (IST).

## Implemented workflow
- Flask receives a user request through the `/submit` route.
- `ScheduleBotAgent` creates a Phidata Agent using Groq model ID `openai/gpt-oss-120b`.
- The registered tools create calendar events, list upcoming events and delete an event.
- `GoogleAPIClient` authenticates through Google OAuth using `credentials.json`, caches credentials in `token.pickle`, and builds Calendar and Sheets API clients.
- The client class also contains methods for creating, reading, writing and appending spreadsheet values, but these methods are not registered as tools on the active agent.

## Setup and configuration
Provide a Google OAuth client-secret file named `credentials.json`, configure `GROQ_API_KEY`, install `ScheduleBot/requirements.txt`, and run the Flask app. OAuth scopes include Calendar and Spreadsheets. Naive event datetimes are assigned the `Asia/Kolkata` timezone.

## Security and correctness findings
- Flask is started with `debug=True`; do not expose the development server publicly.
- OAuth tokens are serialized with pickle. Protect the token file and never load it from an untrusted source.
- The agent can delete calendar events; there is no explicit user confirmation step in the tool wrapper.
- Calendar and spreadsheet scopes are broad; request only the access required.
- `calendar_tools.py`, parent `helper.py` and `docker_manager.py` are additional/alternate utilities; the active agent imports `ScheduleBot/tools.py` and `GoogleClient.py`.
- No automated tests, deployment configuration or calendar-operation audit log is included.

## Verification
Static inspection only; no Google OAuth flow, calendar write or deletion was performed.

## Next steps
Require confirmation before destructive actions, use least-privilege OAuth scopes, secure token storage, validate timezone-aware intervals, add API authentication and tests, and expose Sheets tools only if intentionally supported.
