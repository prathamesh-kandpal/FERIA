"""
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
"""
