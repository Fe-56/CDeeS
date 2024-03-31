import streamlit as st
from extraction import extract_features
from prediction import predict

uploaded_audio = st.file_uploader("Choose an audio file", type=['mp3', 'wav'])

if uploaded_audio is not None:
    st.audio(uploaded_audio, format='audio/mp3')

if st.button("Recommend me music"):
    features = extract_features(uploaded_audio)
    valence, arousal = predict(features)
    print(valence, arousal)