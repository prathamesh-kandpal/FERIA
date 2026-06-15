"""
app.py — Application bootstrap file

Responsibilities:
- Launch the FastAPI application
- Import app instance from src.main
- Serve as the project's execution entrypoint

Run:

    uvicorn app:app --reload
"""

from src.main import app
