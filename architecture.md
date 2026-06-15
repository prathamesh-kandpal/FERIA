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
