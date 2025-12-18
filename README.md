# OmniAssist AI

## Setup Instructions

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Setup**:
    - Copy `.env.example` to `.env`.
    - Add your `OPENAI_API_KEY` to `.env`.
    - Add your `ELEVENLABS_API_KEY` to `.env` (for voice features).

3.  **Ingest Data**:
    Run the ingestion script to create the knowledge base:
    ```bash
    python -m api.services.ingest
    ```

4.  **Run the Application**:
    Start the FastAPI server:
    ```bash
    uvicorn api.index:app --reload
    ```

5.  **Access the Chat**:
    Open your browser and navigate to: [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)
    - **Text**: Type and send.
    - **Voice**: Click 🎤 to record.
    - **Image**: Click 📎 to upload an image (screenshot, chart, etc.) with your query.

## API Documentation
You can view the API docs at [http://localhost:8000/docs](http://localhost:8000/docs).
