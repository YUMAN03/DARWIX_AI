# 🎙️ Audio Transcription & Speaker Diarization

A full-stack AI-powered tool for transcribing audio files and distinguishing between speakers using diarization. Supports multilingual audio and returns structured JSON output for easy downstream processing.

---

## 🚀 Features

- 🎧 Audio file upload for transcription  
- 🗣️ Automatic speaker diarization to distinguish between multiple speakers  
- 📦 Returns a clean, structured JSON format  
- 🌍 Multilingual audio support (language auto-detection and transcription)  
- ⚡ FastAPI backend for efficient API serving  
- 🖥️ Streamlit-based frontend for easy interaction  

---

## 🛠️ Tech Stack

- **Python**
- **Transcription & Diarization:** `AssemblyAI API`
- **Frontend:** `Streamlit`
- **Backend:** `FastAPI`, `Uvicorn`
- **Deployment Ready:** Compatible with Railway, Render, or localhost

---

## 📥 Installation & Usage

### 1. Clone this repo and install dependencies

```bash
git clone https://github.com/YUMAN03/DARWIX_AI.git
cd DARWIX_AI
pip install -r requirements.txt


ASSEMBLYAI_API_KEY=your_assemblyai_api_key


uvicorn app:app --reload

streamlit run frontend.py

{
  "utterances": [
    {
      "speaker": 1,
      "text": "Hello, how are you?"
    },
    {
      "speaker": 2,
      "text": "I'm good, thank you!"
    }
  ]
}
