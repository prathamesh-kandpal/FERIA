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
