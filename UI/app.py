import streamlit as st
from extraction import extract_features
from prediction import predict
import tempfile
import os

uploaded_audio = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

if uploaded_audio:
    st.audio(uploaded_audio, format='audio/mp3')

    uploaded_audio_path = f'./UI/uploaded_audio/{uploaded_audio.name}'

    with open(uploaded_audio_path, "wb") as f:
        f.write(uploaded_audio.getvalue())

if st.button("Recommend me music"):
    features = extract_features(uploaded_audio_path)
    valence, arousal = predict(features)
    print(valence, arousal)