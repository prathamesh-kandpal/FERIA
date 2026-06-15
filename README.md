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
