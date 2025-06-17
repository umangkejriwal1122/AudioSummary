from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Audio Summary App", page_icon="🤖")

st.header("My Audio Summary Web Application 🤖")

uploaded_audio = st.file_uploader("Upload an audio file..",type=["mp3"])

if uploaded_audio is not None:
    audio_file_name = uploaded_audio.name
    with open(audio_file_name,'wb') as f:
        f.write(uploaded_audio.getbuffer())

    st.audio(audio_file_name)

    st.write("Uploading file...")

    audio_file = genai.upload_file(path=audio_file_name)

    st.write("Upload Completed")

    st.write("Generating summary.....")

    prompt = """Listen carefully to the following audio and provide me the brief summary in 
                English and hindi both"""
    
    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content([prompt,audio_file])

    st.write(response.text)

    os.remove(audio_file_name)