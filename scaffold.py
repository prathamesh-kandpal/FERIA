"""
FERIA — Financial Email Resolution & Inquiry Agent
by Nexus AI

Run this script from inside your feria/ folder:
    python scaffold.py

It will create all folders and files with placeholder comments.
Each team member picks a file and owns it end to end.
"""

import os

# ── Folder structure ──────────────────────────────────────────────────────────

FOLDERS = [
    "src",
    "static/css",
    "static/js",
    "data",
]

# ── File contents (comments/stubs only, no logic) ─────────────────────────────

FILES = {

    # ── Python files ──────────────────────────────────────────────────────────

    "src/app.py": """\
\"\"\"
app.py — Application bootstrap file

Responsibilities:
- Launch the FastAPI application
- Import app instance from src.main
- Serve as the project's execution entrypoint

Run:

    uvicorn app:app --reload
\"\"\"

from src.main import app
""",

    "src/main.py": """\
\"\"\"
main.py — FastAPI application entry point
Owner: [Team Member Name]

Responsibilities:
- Initialize the FastAPI app instance
- Mount the static/ folder for frontend serving
- Define API routes:
    POST /ingest-email   — receive raw email, trigger the FERIA crew
    GET  /health         — health check endpoint
    GET  /chat           — serve the chat UI
- Load environment variables via python-dotenv
- Wire up CORS middleware for frontend-backend communication
\"\"\"
""",

    "src/agents.py": """\
\"\"\"
agents.py — CrewAI agent and crew definitions
Owner: [Team Member Name]

Responsibilities:
- Define the FERIA crew with 3-4 specialized agents:

    1. Triage Agent
       - Reads the incoming email
       - Classifies intent (complaint, query, request, escalation)
       - Tags priority level

    2. PII Redaction Agent
       - Strips sensitive customer data before further processing
       - Replaces PII with safe placeholders (e.g. [ACCOUNT_NO], [NAME])

    3. RAG Retrieval Agent
       - Calls into rag.py to fetch relevant policy/product context
       - Passes retrieved context to the drafting agent

    4. Response Drafting Agent
       - Composes a professional, compliant email reply
       - Escalates to human queue if confidence is low

- Define tasks for each agent
- Assemble and return the Crew object
- Keep tool definitions minimal — heavy logic lives in rag.py
\"\"\"
""",

    "src/rag.py": """\
\"\"\"
rag.py — RAG pipeline and PII redaction utilities
Owner: [Team Member Name]

Responsibilities:
- Load and chunk documents from the data/ folder
- Generate embeddings (e.g. OpenAI, HuggingFace, or FastEmbed)
- Build and persist the vector store (FAISS or ChromaDB)
- Expose a retrieve(query: str) function that returns top-k chunks
- Implement redact_pii(text: str) function:
    - Use regex or a lightweight NER model
    - Replace account numbers, names, emails, phone numbers
- This module is imported by agents.py — keep it stateless and functional
\"\"\"
""",

    "src/schemas.py": """\
\"\"\"
schemas.py — Pydantic models for request/response validation
Owner: [Team Member Name]

Responsibilities:
- Define all data models used across the app:

    EmailIngestionRequest
        - sender: str
        - subject: str
        - body: str
        - received_at: datetime

    TriageResult
        - intent: str           (complaint | query | request | escalation)
        - priority: str         (low | medium | high)
        - redacted_body: str

    AgentResponse
        - draft_reply: str
        - retrieved_context: list[str]
        - escalate: bool
        - confidence_score: float

    HealthResponse
        - status: str
        - version: str

- All models extend pydantic.BaseModel
- Used by main.py for route validation and by agents.py for structured output
\"\"\"
""",
    "src/__init__.py": """\
\"\"\"src/ — Python package for FERIA backend and agents\"\"\"
""",
    # ── Static frontend ───────────────────────────────────────────────────────

    "static/index.html": """\
<!--
index.html — FERIA landing page
Owner: [Team Member Name]

Content:
- Hero section: FERIA name, tagline, brief product description
- Key features section (3 cards: Triage, RAG, Compliance)
- CTA button linking to login.html
- Navigation bar with Nexus AI branding

Style: link to static/css/style.css
Scripts: link to static/js/main.js
-->
""",

    "static/login.html": """\
<!--
login.html — Login page
Owner: [Team Member Name]

Content:
- FERIA logo / Nexus AI branding at top
- Login form: username, password, institution name (dropdown)
- Submit button → redirects to dashboard.html (mock auth, no backend needed for demo)
- Forgot password link (static, non-functional for demo)

Style: link to static/css/style.css
Scripts: link to static/js/main.js
-->
""",

    "static/dashboard.html": """\
<!--
dashboard.html — Agent operations dashboard
Owner: [Team Member Name]

Content:
- Summary cards: Emails Processed, Resolved, Escalated, Avg Response Time
- Recent email triage table (mock data for demo):
    Columns: Sender, Subject, Intent, Priority, Status
- Sidebar navigation: Dashboard | Chat | Settings | Logout
- Status indicators using colour-coded badges

Style: link to static/css/style.css
Scripts: link to static/js/dashboard.js
-->
""",

    "static/chat.html": """\
<!--
chat.html — Live email triage chat interface
Owner: [Team Member Name]

Content:
- Chat window showing agent conversation thread
- Input box: paste or type a raw customer email
- Send button → POST to /ingest-email
- Response panel: shows triage result, redacted email, draft reply
- Escalation banner if escalate: true in response

Style: link to static/css/style.css
Scripts: link to static/js/chat.js
-->
""",

    "static/css/style.css": """\
/*
style.css — Global stylesheet for FERIA frontend
Owner: [Team Member Name]

Sections to implement:
- CSS variables: brand colours, font stack, spacing scale
- Reset / base styles
- Navigation bar
- Button styles (primary, secondary, danger)
- Card components
- Form inputs
- Badge / status pill styles
- Responsive grid layout
- Table styles for dashboard
- Chat window and message bubble styles

Suggested colour palette:
- Primary:   #1B3A6B  (deep navy — BFSI trustworthy)
- Accent:    #0F9B8E  (teal — AI / fintech modern)
- Surface:   #F5F7FA
- Text:      #1A1A2E
*/
""",

    "static/js/main.js": """\
/*
main.js — Shared JavaScript utilities
Owner: [Team Member Name]

Responsibilities:
- Navigation active state management
- Mock login handler (redirect to dashboard.html on submit)
- Any shared utility functions used across pages
- No framework — vanilla JS only
*/
""",

    "static/js/dashboard.js": """\
/*
dashboard.js — Dashboard page interactions
Owner: [Team Member Name]

Responsibilities:
- Populate summary cards with mock data on page load
- Render the triage table with sample email entries
- Filter/sort table by intent or priority (optional for demo)
*/
""",

    "static/js/chat.js": """\
/*
chat.js — Chat page interactions and API integration
Owner: [Team Member Name]

Responsibilities:
- Capture email input from the form
- POST to /ingest-email with JSON payload
- Parse AgentResponse and render:
    - Draft reply in the chat window
    - Triage intent and priority as badges
    - Escalation warning banner if needed
- Handle loading states and basic error messages
*/
""",

    # ── Data folder placeholder ───────────────────────────────────────────────

    "data/README.txt": """\
data/ — RAG training corpus
Owner: [Team Member Name]

Place your source documents here. Suggested files:

- faq.pdf or faq.txt          : Common customer FAQs
- product_guide.pdf           : Bank product descriptions (loans, cards, accounts)
- email_samples.txt           : Example customer emails with ideal responses
- escalation_policy.txt       : Rules for when to escalate vs auto-resolve
- compliance_guidelines.txt   : Regulatory tone and disclosure requirements

rag.py will load, chunk, and embed everything in this folder.
Do not commit sensitive or real customer data here.
""",

    # ── Documentation ─────────────────────────────────────────────────────────

    "README.md": """\
# FERIA — Financial Email Resolution & Inquiry Agent
**by Nexus AI**

> An agentic AI product built to streamline customer email support for BFSI institutions.

---

## Overview

FERIA automatically triages incoming customer emails, redacts PII, retrieves relevant
policy context via RAG, and drafts compliant responses — escalating only when human
intervention is genuinely needed.

---

## Team

| Name | Role | File Owned |
|------|------|------------|
| [Name] | Backend & API | main.py |
| [Name] | Agents & Crew | agents.py |
| [Name] | RAG Pipeline | rag.py |
| [Name] | Schemas & Frontend | schemas.py + static/ |

---

## Tech Stack

- **Agentic Framework**: CrewAI
- **Backend**: FastAPI
- **RAG**: FAISS / ChromaDB + LangChain
- **LLM**: Claude (Anthropic) via API
- **Frontend**: Vanilla HTML / CSS / JS
- **PII Redaction**: Regex + optional NER

---

## Project Structure

```
feria/
├── app.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agents.py
│   ├── rag.py
│   └── schemas.py
│
├── static/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── chat.html
│   ├── css/style.css
│   └── js/
│       ├── main.js
│       ├── dashboard.js
│       └── chat.js
│
├── data/
│   └── README.txt
│
├── README.md
├── architecture.md
├── requirements.txt
└── .env.example
```

---

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000` in your browser.

---

## Demo Flow

1. Open `chat.html`
2. Paste a sample customer email
3. FERIA triages, redacts PII, retrieves context, and drafts a reply
4. Escalation banner appears if the query is high-risk or ambiguous
""",

    "architecture.md": """\
# FERIA — System Architecture
**by Nexus AI**

---

## High-Level Flow

```
Customer Email
      │
      ▼
[FastAPI /ingest-email]
      │
      ▼
[FERIA CrewAI Crew]
      │
      ├── Triage Agent         → Classifies intent and priority
      │
      ├── PII Redaction Agent  → Strips sensitive data
      │
      ├── RAG Retrieval Agent  → Fetches relevant policy context (via rag.py)
      │
      └── Response Drafting Agent → Drafts reply or flags for escalation
                │
                ▼
         [AgentResponse]
                │
                ▼
     [FastAPI returns JSON]
                │
                ▼
         [chat.html renders result]
```

---

## Agent Responsibilities

| Agent | Input | Output |
|-------|-------|--------|
| Triage Agent | Raw email body | Intent label, priority level |
| PII Redaction Agent | Raw email body | Redacted email text |
| RAG Retrieval Agent | Redacted email | Top-k relevant policy chunks |
| Response Drafting Agent | Triage + context | Draft reply, escalation flag |

---

## RAG Pipeline

```
data/ folder
    │
    ▼
Document Loader (LangChain)
    │
    ▼
Text Splitter (RecursiveCharacterTextSplitter)
    │
    ▼
Embedding Model
    │
    ▼
Vector Store (FAISS / ChromaDB)
    │
    ▼
Retriever → top-k chunks → RAG Retrieval Agent
```

---

## Tech Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| Agentic framework | CrewAI | Role-based agents, easy task chaining |
| Backend | FastAPI | Async, lightweight, auto docs |
| Vector store | FAISS | No external service needed for demo |
| LLM | Claude via Anthropic API | Compliance-safe, strong instruction following |
| Frontend | Vanilla JS | No build step, easy for all team members |

---

## Deployment (Demo Scope)

- Run locally via `uvicorn main:app --reload`
- Frontend served as static files by FastAPI
- No database — in-memory vector store for demo
- `.env` file for API keys (never commit to repo)
""",

    # ── Config ────────────────────────────────────────────────────────────────

    "requirements.txt": """\
# FERIA dependencies
# Owner: fill in versions once agreed by the team

fastapi
uvicorn[standard]
python-dotenv
pydantic

crewai
crewai-tools

langchain
langchain-community
langchain-anthropic

faiss-cpu
sentence-transformers

# Optional: swap faiss-cpu for chromadb if preferred
# chromadb
""",

    ".env.example": """\
# .env.example — copy this to .env and fill in your keys
# Never commit .env to the repo

ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here_if_needed
APP_ENV=development
""",

    ".gitignore": """\
.env
__pycache__/
*.pyc
*.pyo
.DS_Store
*.egg-info/
dist/
build/
.venv/
venv/
*.faiss
*.pkl
""",

}

# ── Scaffold runner ───────────────────────────────────────────────────────────

def scaffold():
    print("FERIA scaffold starting...")

    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        print(f"  Created folder: {folder}/")

    for filepath, content in FILES.items():
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created file:   {filepath}")

    print("\nDone. Your FERIA project is ready.")
    print("Next step: assign file ownership in README.md and start building.")

if __name__ == "__main__":
    scaffold()
