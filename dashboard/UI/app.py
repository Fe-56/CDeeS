import streamlit as st
from feature_extraction import extract_features
from preprocess import process_song
from prediction import predict
from visualisations import plot_va_graph
import tempfile
import os
import math
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, './research/utils')
from paths import *

sys.path.insert(1, './dashboard/VectorDB_prod')
from VectorDB_prod import *

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

if st.button("Recommend me music!"):
    # MER phase
    features = extract_features(uploaded_audio_path, best_model)
    processed_features = process_song(features, best_model)
    valence, arousal = predict(processed_features, best_model)

    rounded_valence = round(valence.item(), 4)
    rounded_arousal = round(arousal.item(), 4)

    st.write(f"Valence: {rounded_valence}")
    st.write(f"Arousal: {rounded_arousal}")
    st.pyplot(plot_va_graph(valence, arousal))

    # personalised music recommendation phase
    num_recommendations = 5
    collection = get_chromadb_collection()
    recommended_metadatas, recommended_audio_paths, recommended_va_values = get_recommendations(rounded_valence, rounded_arousal, num_recommendations, collection)

    for i in range(num_recommendations):
        artist = recommended_metadatas[i]['artist']
        title = recommended_metadatas[i]['title']
        audio_path = recommended_audio_paths[i]
        recommended_valence = round(recommended_va_values[i][0], 4)
        recommended_arousal = round(recommended_va_values[i][1], 4)
        
        st.write(f'Song {i+1}')
        st.write(f'Artist: {artist}')
        st.write(f'Song Title: {title}')
        st.write(f'Valence: {recommended_valence}, Arousal: {recommended_arousal}')
        st.audio(audio_path, format='audio/mp3')