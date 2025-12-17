import requests
from openai import OpenAI
from app.core.config import settings
import io

class VoiceService:
    def __init__(self):
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.elevenlabs_api_key = settings.ELEVENLABS_API_KEY
        # Using a default voice ID (e.g., "Rachel")
        self.voice_id = "21m00Tcm4TlvDq8ikWAM" 

    def transcribe_audio(self, audio_file) -> str:
        """
        Transcribes audio file using OpenAI Whisper.
        """
        try:
            transcript = self.openai_client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcript.text
        except Exception as e:
            print(f"Transcription error: {e}")
            raise e

    def text_to_speech(self, text: str) -> bytes:
        """
        Converts text to speech using ElevenLabs API.
        """
        if not self.elevenlabs_api_key:
            print("ElevenLabs API key not found.")
            return None

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.elevenlabs_api_key
        }
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"TTS error: {e}")
            return None

voice_service = VoiceService()
