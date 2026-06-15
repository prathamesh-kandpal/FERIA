"""
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
"""
