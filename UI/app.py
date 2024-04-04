import streamlit as st
from extraction_opensmile import extract_features
from prediction import predict
import tempfile
import os
import math

uploaded_audio = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

if uploaded_audio:
    st.audio(uploaded_audio, format='audio/mp3')

    uploaded_audio_path = f'./UI/uploaded_audio/{uploaded_audio.name}'

    with open(uploaded_audio_path, "wb") as f:
        f.write(uploaded_audio.getvalue())

if st.button("Recommend me music"):
    features = extract_features(uploaded_audio_path)
    valence, arousal = predict(features)

    rounded_valence = round(valence.item(), 4)
    rounded_arousal = round(arousal.item(), 4)

    st.write(f"Valence: {rounded_valence}")
    st.write(f"Arousal: {rounded_arousal}")