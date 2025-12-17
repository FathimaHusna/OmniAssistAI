# OmniAssist AI - Portfolio Demo Script

**Goal**: Record a 2-3 minute video showcasing the capabilities of OmniAssist AI.

## Setup
1.  Ensure the server is running: `uvicorn app.main:app --reload`
2.  Open the frontend: `http://localhost:8000/static/index.html`
3.  Have a sample image ready (e.g., a chart or screenshot).
4.  Start your screen recorder (OBS, Loom, etc.).

## Scene 1: Introduction & Text Chat (0:00 - 0:30)
-   **Action**: Open the page. Point out the clean "OmniAssist AI" interface.
-   **Voiceover**: "Hi, I'm [Your Name], and this is OmniAssist, an intelligent enterprise AI assistant I built."
-   **Action**: Type: "Hello, who are you?"
-   **Observation**: Watch the response stream in (typewriter effect).
-   **Voiceover**: "It uses a streaming interface for low-latency responses."

## Scene 2: RAG & Knowledge Base (0:30 - 1:00)
-   **Action**: Type: "What is the policy on remote work?"
-   **Observation**: Agent retrieves info from the vector DB.
-   **Voiceover**: "It has access to company documents via a RAG pipeline. Here it retrieves the specific remote work policy."

## Scene 3: Multimodal (Image) (1:00 - 1:30)
-   **Action**: Click the 📎 icon and upload your sample image.
-   **Action**: Type: "Explain this image to me."
-   **Observation**: Agent analyzes the image.
-   **Voiceover**: "It's multimodal. I can upload charts or screenshots, and the agent uses GPT-4o to understand them."

## Scene 4: Agentic Tools (Ticketing/Email) (1:30 - 2:15)
-   **Action**: Type: "Create a high priority ticket for a server outage."
-   **Observation**: Agent confirms ticket creation.
-   **Voiceover**: "It's not just a chatbot; it's an agent. It can take actions like creating tickets."
-   **Action**: Type: "Send an email to admin@example.com about the outage."
-   **Observation**: Agent asks for confirmation.
-   **Action**: Type: "Yes, proceed."
-   **Voiceover**: "It also handles sensitive actions safely by asking for confirmation before sending emails."

## Scene 5: Voice Interaction (2:15 - 2:45)
-   **Action**: Click the 🎤 button.
-   **Speak**: "Schedule a meeting with the team tomorrow at 10am to discuss the incident."
-   **Observation**: Agent listens, transcribes, and schedules the meeting.
-   **Voiceover**: "Finally, it supports full voice interaction using Whisper for STT and ElevenLabs for TTS."

## Closing
-   **Voiceover**: "This project demonstrates RAG, Agents, Multimodal AI, and full-stack engineering. Thanks for watching!"
