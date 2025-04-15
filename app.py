import streamlit as st
import requests

st.set_page_config(page_title="Audio Transcription with Diarization", page_icon="🎙️")
st.title("🎙️ Audio Transcription with Diarization")

audio_file = st.file_uploader("📂 Upload an audio file", type=["mp3", "wav", "m4a"])

if st.button("Transcribe"):
    if audio_file is None:
        st.warning("Please upload an audio file.")
    else:
        with st.spinner("Uploading and transcribing..."):
            try:
                api_url = "https://darwixai-production.up.railway.app/transcribe"
                files = {'file': (audio_file.name, audio_file, audio_file.type)}
                response = requests.post(api_url, files=files)

                if response.status_code == 200:
                    data = response.json()
                    utterances = data["utterances"]

                    if utterances:
                        st.success("✅ Transcription Completed with Speaker Diarization")
                        for u in utterances:
                            speaker = u.get("speaker", "Unknown")
                            text = u.get("text", "")
                            st.markdown(f"**🧑 Speaker {speaker}:** {text}")
                    else:
                        st.info("No utterances detected or diarization unavailable.")
                else:
                    st.error(f"API error: {response.status_code} — {response.text}")

            except Exception as e:
                st.error(f"Error during transcription: {e}")
