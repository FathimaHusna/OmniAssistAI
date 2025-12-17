from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    image: str = None  # Base64 encoded image string

class ChatResponse(BaseModel):
    response: str
