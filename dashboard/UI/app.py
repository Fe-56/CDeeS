import streamlit as st
from feature_extraction import extract_features
from preprocess import process_song
from prediction import predict
import tempfile
import os
import math

import sys
sys.path.insert(1, './research/utils')
from paths import *

# write the name of the best model here!
best_model = 'opensmile_gemaps_normalised'

# helper functions
def write_audio_file(uploaded_file):
    uploaded_audio_path = None

    if uploaded_file:
        st.audio(uploaded_audio, format='audio/mp3')

        uploaded_audio_path = f'{UPLOADED_AUDIO_PATH}/{uploaded_audio.name}'

        with open(uploaded_audio_path, "wb") as f:
            f.write(uploaded_audio.getvalue())

    return uploaded_audio_path

uploaded_audio = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])
uploaded_audio_path = write_audio_file(uploaded_audio)

if st.button("Recommend me music"):
    features = extract_features(uploaded_audio_path, best_model)
    processed_features = process_song(features, best_model)
    valence, arousal = predict(processed_features, best_model)

    rounded_valence = round(valence.item(), 4)
    rounded_arousal = round(arousal.item(), 4)

    st.write(f"Valence: {rounded_valence}")
    st.write(f"Arousal: {rounded_arousal}")
