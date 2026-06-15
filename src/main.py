"""
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
"""
