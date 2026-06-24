# FERIA — Financial Email Resolution & Inquiry Agent
### Problem Statement & Project Brief | Insurance Domain
*Prepared by Nexus AI*

---

## Background

Insurance companies manage one of the most complex and emotionally sensitive customer support landscapes in financial services. Policyholders reach out at critical moments — after an accident, during a medical emergency, after a loved one's death — expecting fast, accurate, and empathetic responses.

Yet the reality of insurance customer support today is largely manual. Agents handle a high volume of emails spanning multiple insurance lines — health, motor, life, travel, and home — each with its own policy wording, coverage terms, exclusion clauses, claim procedures, and regulatory requirements.

Support agents are expected to triage urgency, look up the correct policy document for the right product, draft accurate responses grounded in coverage terms, and escalate complex cases — all while managing volume, maintaining compliance with IRDAI guidelines, and meeting mandated turnaround times.

This is not scalable. And the cost of getting it wrong — a misquoted coverage limit, a delayed claim acknowledgement, an incorrect exclusion cited — is measured in customer trust, regulatory penalties, and potential litigation.

---

## The Problem

### 1. High Volume, High Variety — Fully Manual Today
An insurance company offering health, motor, life, travel, and home insurance receives emails spanning dozens of query types simultaneously — new claim intimations, claim status follow-ups, policy coverage clarifications, premium payment disputes, renewal reminders, nominee update requests, grievance filings, and more. Each query type requires different information, different policy documents, and different response protocols. Today all of this is handled manually, one email at a time.

### 2. Policy Documents Are Dense and Product-Specific
Insurance policy wordings are among the most complex documents in financial services. A health insurance policy alone may contain sub-limits for specific treatments, co-payment clauses, waiting period conditions for pre-existing diseases, room rent restrictions, and network hospital requirements. A motor policy has own-damage vs third-party liability distinctions, NCB (No Claim Bonus) conditions, and cashless vs reimbursement claim procedures. Agents cannot be expected to memorize all of this across five product lines. Manual lookup is slow and error-prone.

### 3. Claim Emails Are Time-Sensitive and High Stakes
A customer emailing about a hospitalisation claim or a motor accident is often in distress. Delayed or inaccurate responses at this moment have outsized consequences — both for customer trust and for regulatory compliance. IRDAI mandates specific turnaround times: claim acknowledgement within 3 working days, final claim decision within 30 days. Manual workflows struggle to consistently meet these timelines at scale.

### 4. Escalation Loses All Context
Complex cases — rejected claims being disputed, grievances against surveyors, third-party liability disagreements, death claim complications — are escalated to senior agents or grievance officers. But the escalation is often just a forwarded email thread. The receiving agent must reconstruct the full picture: what the customer is asking, what the policy says, what was previously communicated, and why the case is sensitive. This duplication of effort delays resolution at exactly the moment speed matters most.

### 5. Grievance and Compliance Risk
IRDAI's Integrated Grievance Management System (IGMS) requires insurers to log and resolve grievances within defined timelines. Untracked escalations, undocumented decisions, and inconsistent responses create compliance exposure. Without a structured audit trail, proving that a case was handled correctly and within regulatory timelines is difficult.

### 6. PII and Sensitive Health Data Exposure
Insurance emails frequently contain sensitive personal information — policy numbers, claim amounts, diagnosis details, hospitalization records, vehicle registration numbers, nominee details. Without structured redaction before processing, this data is unnecessarily exposed during handling, storage, and any AI-assisted processing.

---

## What We Are Building

**FERIA (Financial Email Resolution & Inquiry Agent)** is an agentic AI pipeline that automates and augments the end-to-end customer email support workflow for insurance companies.

FERIA handles emails across multiple insurance lines — health, motor, life, travel, and home — from a single unified pipeline. Each stage is handled by a specialized AI agent. Routine queries are auto-resolved with policy-grounded, citation-backed responses. Complex, high-risk, or emotionally sensitive cases are escalated to human agents — with full context pre-loaded and an intelligent assistant ready to help them resolve the case faster.

---

## Proposed Solution — How FERIA Works

### Stage 1 — Email Ingestion
Support teams upload incoming customer emails (in `.txt` format) via a batch ingestion interface. A mock inbox UI displays all ingested emails organized by insurance line, with sender, subject, urgency indicator, and timestamp — giving the familiar feel of a support inbox without requiring real email infrastructure.

### Stage 2 — PII Redaction
Before any AI processing begins, a redaction module automatically identifies and strips sensitive information:
- Policy numbers, claim reference numbers
- Aadhaar, PAN, driving licence, vehicle registration numbers
- Diagnosis codes, treatment details, hospital names (health insurance)
- Nominee details, sum assured amounts
- Phone numbers, email addresses, physical addresses

Redacted fields are logged by type (not value) in the audit trail. The redacted email is what all downstream agents process — never the original.

### Stage 3 — Triage Agent
A classification agent analyzes the redacted email and outputs a structured triage result:

- **Insurance Line** — Health / Motor / Life / Travel / Home
- **Query Type** — New claim intimation / Claim status / Coverage clarification / Premium dispute / Renewal / Nominee update / Grievance / General inquiry
- **Urgency** — Critical (hospitalisation, accident) / High / Medium / Low
- **Risk Flags** — Claim rejection dispute / Legal threat / Regulatory grievance / Repeated follow-up / Death claim / None
- **Escalation Decision** — Auto-resolve or escalate, with reason
- **SLA Tag** — Based on IRDAI mandated turnaround times for the query type

### Stage 4 — RAG Retrieval Agent
Based on the classified insurance line and query type, a retrieval agent queries a vector database of insurance policy documents. The knowledge base contains:
- Health insurance policy wording (coverage, exclusions, sub-limits, waiting periods, claim procedure)
- Motor insurance policy wording (OD vs TP coverage, NCB terms, cashless claim procedure)
- Life insurance policy wording (sum assured, premium payment terms, nominee conditions, death claim process)
- Travel insurance policy wording (coverage scope, emergency evacuation, trip cancellation terms)
- Home insurance policy wording (structure vs contents coverage, natural disaster exclusions)
- IRDAI grievance handling guidelines
- Internal FAQ and escalation SOPs

The agent returns the most relevant clauses with source metadata (policy name, section, clause number) for citation.

### Stage 5 — Resolution Agent
For non-escalated cases, a response drafting agent uses the retrieved policy context to generate an accurate, grounded response. Every response:
- Is written in plain language appropriate for a distressed or confused customer
- Cites the specific policy section it draws from
- Includes next steps where applicable (e.g., documents required for claim, how to submit via portal)
- Is assigned a confidence score — low confidence automatically triggers escalation regardless of triage output

### Stage 6 — Escalation Handler Bot *(Key Differentiator)*
For escalated cases — claim rejection disputes, grievances, death claims, legal threats, low-confidence responses — FERIA opens an intelligent chat thread for the human agent. The Escalation Handler Bot pre-loads full case context and is ready to answer the agent's questions immediately.

**What the bot knows:**
- Full case summary (what the customer is asking, why FERIA escalated it)
- The original redacted email
- Insurance line, query type, urgency, and risk flags from triage
- Policy clauses retrieved during the pipeline, with citations
- The draft response attempted, if any
- Confidence score and escalation reason
- Applicable IRDAI guideline for this case type

**What the agent can ask:**
- *"What exactly is the customer disputing?"*
- *"What does our health policy say about pre-existing disease waiting periods?"*
- *"Is this a valid grievance under IRDAI guidelines?"*
- *"What documents should we request from the customer?"*
- *"Draft a response I can review and send."*
- *"What is the IRDAI mandated turnaround time for this case type?"*

The bot answers from policy documents and case context — with citations — and explicitly defers all final decisions to the human agent. The agent logs a resolution note and closes the case. The entire interaction is stored in the audit trail.

This is **human-in-the-loop AI** — automation where it is safe, intelligent augmentation where human judgment is required.

### Stage 7 — Audit Trail
Every case generates a structured, immutable audit log:
- PII types redacted (not values)
- Full triage classification output
- Policy chunks retrieved (document, section, clause, snippet)
- Confidence score and escalation decision
- Escalation chat thread history (if applicable)
- SLA tag and time-to-resolution
- Final resolution note and agent sign-off

Viewable per case. Exportable. Directly supports IRDAI compliance documentation requirements.

---

## Business Value

| Metric | Current State | FERIA Target |
|---|---|---|
| Email triage | Manual, inconsistent | Automated, structured, multi-line |
| Policy lookup | Manual per case | RAG-retrieved, cited, cross-product |
| Average response time | Hours | Seconds (auto-resolved cases) |
| IRDAI SLA adherence | Best effort, untracked | Tracked per case, flagged on breach |
| Escalation handoff | Context lost, re-read from scratch | Full context pre-loaded via Escalation Bot |
| Audit trail | None or email threads | Structured, per-case, exportable |
| PII / health data handling | Unstructured | Redacted before any processing |
| Auto-resolution rate | 0% | 70%+ target |
| Grievance documentation | Manual | Auto-generated audit trail per case |

---

## Insurance Lines & Document Corpus

FERIA's knowledge base covers five insurance product lines:

| Insurance Line | Key Document Sections for RAG |
|---|---|
| Health Insurance | Coverage scope, sub-limits, exclusions, waiting periods, co-payment, cashless vs reimbursement, claim procedure |
| Motor Insurance | OD vs TP coverage, NCB conditions, cashless claim procedure, exclusions, total loss terms |
| Life Insurance | Sum assured, premium payment terms, lapse/revival conditions, nominee process, death claim documents |
| Travel Insurance | Coverage scope, trip cancellation, medical emergency, baggage loss, exclusions, claim filing process |
| Home Insurance | Structure vs contents coverage, natural disaster terms, exclusions, valuation method, claim procedure |

Plus: IRDAI Grievance Handling Guidelines and Internal Support SOPs.

---

## Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Backend | Python |
| LLM | Claude API (Anthropic) |
| Vector Database | ChromaDB (local) |
| Document Parsing | PyMuPDF |
| PII Redaction | Regex + spaCy |
| Case Storage | SQLite / JSON |
| Deployment | Fully local — no cloud infra required |

---

*Document version: 1.0 | Project: FERIA | Team: Nexus AI*