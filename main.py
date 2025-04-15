from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn
import requests
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables from .env file
load_dotenv()



# Read the API key from the environment
API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
if not API_KEY:
    raise RuntimeError("ASSEMBLYAI_API_KEY not found in environment variables")

HEADERS = {"authorization": API_KEY}

class TranscriptionResult(BaseModel):
    utterances: list

@app.post("/transcribe", response_model=TranscriptionResult)
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        audio_bytes = await file.read()

        # Upload audio file to AssemblyAI
        upload_response = requests.post(
            "https://api.assemblyai.com/v2/upload",
            headers=HEADERS,
            data=audio_bytes
        )

        if upload_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Upload failed")

        audio_url = upload_response.json()['upload_url']

        # Request transcription with diarization and auto-language detection
        transcript_request = {
            "audio_url": audio_url,
            "speaker_labels": True,
            "language_detection": True
        }

        transcript_response = requests.post(
            "https://api.assemblyai.com/v2/transcript",
            json=transcript_request,
            headers=HEADERS
        )

        if transcript_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Transcription request failed")
        transcript_id = transcript_response.json()['id']

        # Poll for result
        while True:
            status_response = requests.get(
                f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
                headers=HEADERS
            ).json()

            if status_response['status'] == 'completed':
                return {"utterances": status_response.get("utterances", [])}
            elif status_response['status'] == 'error':
                raise HTTPException(status_code=500, detail=status_response.get("error", "Unknown error"))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
