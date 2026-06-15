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
