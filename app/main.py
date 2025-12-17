from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import rag_service
from app.services.voice_service import voice_service
import base64

app = FastAPI(title="OmniAssist AI")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response_text = rag_service.chat(request.message, request.image)
        return ChatResponse(response=response_text)
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat/stream")
async def chat_stream_endpoint(request: ChatRequest):
    return StreamingResponse(
        rag_service.astream_chat(request.message, request.image),
        media_type="text/plain"
    )

@app.post("/api/chat/voice")
async def chat_voice_endpoint(
    file: UploadFile = File(...),
    image: UploadFile = File(None) 
):
    try:
        # 1. Transcribe
        content = await file.read()
        import io
        audio_file = io.BytesIO(content)
        audio_file.name = "audio.wav" 
        
        transcribed_text = voice_service.transcribe_audio(audio_file)
        print(f"Transcribed: {transcribed_text}")

        # 2. Process Image if present
        image_base64 = None
        if image:
            image_content = await image.read()
            image_base64 = base64.b64encode(image_content).decode('utf-8')

        # 3. Get RAG Response
        response_text = rag_service.chat(transcribed_text, image_base64)
        print(f"Response: {response_text}")

        # 4. Text to Speech
        audio_bytes = voice_service.text_to_speech(response_text)
        
        audio_base64_resp = None
        if audio_bytes:
            audio_base64_resp = base64.b64encode(audio_bytes).decode('utf-8')

        return JSONResponse(content={
            "response": response_text,
            "audio": audio_base64_resp,
            "transcription": transcribed_text
        })

    except Exception as e:
        print(f"Error in voice endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
